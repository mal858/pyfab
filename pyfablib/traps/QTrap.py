# -*- coding: utf-8 -*-

"""QTrap.py: Base class for an optical trap."""

from PyQt5.QtCore import (pyqtSignal, pyqtSlot, pyqtProperty,
                          QObject, QPointF)
from PyQt5.QtGui import QVector3D
import numpy as np
import pyqtgraph as pg
from enum import Enum
from collections import OrderedDict

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)


class states(Enum):
    static = 0
    normal = 1
    selected = 2
    grouping = 3
    special = 4


class QTrap(QObject):
    """Base class for optical traps

    A trap has physical properties, including three-dimensional
    position, relative amplitude and relative phase.  A structuring
    field can change its optical properties. A trap also has a graphical 
    representation as presented on the QFabScreen.

    Inherits QObject

    Parameters
    ----------
    r : :obj:`QVector3D`
        Three-dimensional position of trap relative to the image
        origin. Default: (0, 0, 0)
    alpha : float
        Relative amplitude of the trap. Default: 1.
    phi : float
        Relative phase of the trap. Default: random.
    cgh : :obj:`QCGH`
        Computational pipeline used to compute the complex
        electric field associated with this trap.
        Default: None
    structure : :obj:`numpy.ndarray` of :obj:`numpy.complex`
        Field used to convert optical tweezer into a structured trap.
        Default: None (optical tweezer).
    state : :obj:`Enum`
        State of the trap, which reflects current operations
        and is reflected in the graphical representation.
    """

    propertyChanged = pyqtSignal(QObject)
    appearanceChanged = pyqtSignal()
    hologramChanged = pyqtSignal()

    def __init__(self,
                 r=QVector3D(),
                 alpha=1.,             # relative amplitude
                 phi=None,             # relative phase
                 structure=None,       # structuring field
                 state=None,           # graphical representation
                 *args, **kwargs):
        super(QTrap, self).__init__(*args, **kwargs)

        # operational state
        self._state = state or states.normal

        # appearance
        self.brush = {states.static: pg.mkBrush(255, 255, 255, 120),
                      states.normal: pg.mkBrush(100, 255, 100, 120),
                      states.selected: pg.mkBrush(255, 105, 180, 120),
                      states.grouping: pg.mkBrush(255, 255, 100, 120),
                      states.special: pg.mkBrush(238, 130, 238, 120)}
        self.baseSize = 15.
        self.spot = {'pos': QPointF(),
                     'size': self.baseSize,
                     'pen': pg.mkPen('w', width=0.2),
                     'brush': self.brush[self._state],
                     'symbol': self.plotSymbol()}

        # physical properties
        self.r = r
        self._alpha = alpha
        self.phi = phi or np.random.uniform(low=0., high=2.*np.pi)
        self.registerProperties()

        # hologram calculation
        self._structure = None
        self.psi = None

    def initialize(self):
        self.psi = self.cgh.psi().copy()
        self.updateStructure()
        self.updateAppearance()
        logger.info('Initialized')

    def computeHologram(self):
        try:
            self.cgh.compute_displace(self.amp, self.r, self.psi)
            if self.structure is not None:
                self.psi = self.psi * self.structure
            logger.debug('computeHologram')
            self.hologramChanged.emit()
            self.propertyChanged.emit(self)
        except Exception as ex:
            logger.debug('Could not compute hologram: ', ex)

    # Customizable methods for subclassed traps

    def plotSymbol(self):
        """Graphical representation of trap"""
        return 'o'

    def updateAppearance(self):
        """Adapt trap appearance to trap motion and property changes"""
        self.spot['pos'] = self.coords()
        self.spot['size'] = np.clip(self.baseSize - self.r.z()/20., 10., 35.)
        logger.debug('updateAppearance')
        self.appearanceChanged.emit()

    def updateStructure(self):
        """Update structuring field.

        Note: This should be overridden by subclasses.
        """
        logger.debug('updateStructure')
        self.structure = None

    # Computational pipeline for calculating structure field
    @pyqtProperty(object)
    def cgh(self):
        return self._cgh

    @cgh.setter
    def cgh(self, cgh):
        self._cgh = cgh
        if cgh is None:
            return
        self._cgh.sigUpdateGeometry.connect(self.initialize)
        self.initialize()

    @pyqtProperty(object)
    def structure(self):
        return self._structure

    @structure.setter
    def structure(self, field):
        if self.cgh:
            self._structure = self.cgh.bless(field)
            self.computeHologram()
        else:
            self._structure = field

    # Methods for moving the trap
    def moveBy(self, dr):
        """Translate trap by specified displacement vector"""
        self.r = self.r + dr

    def moveTo(self, r):
        """Move trap to position r"""
        self.r = r

    def coords(self):
        """In-plane position of trap for plotting"""
        return self._r.toPointF()

    def isWithin(self, rect):
        """Return True if this trap lies within the specified rectangle"""
        return rect.contains(self.coords())

    # Methods for editing properties with QTrapWidget
    def registerProperty(self, name, decimals=2, tooltip=False):
        """Register a property so that it can be edited"""
        self.properties[name] = {'decimals': decimals,
                                 'tooltip': tooltip}

    @pyqtSlot(str, float)
    def setProperty(self, name, value):
        """Thread-safe method to change a specified property without
        emitting signals.  This is called by QTrapWidget when the
        user edits a property.  Blocking signals prevents a loop.
        """
        self.blockSignals(True)
        setattr(self, name, value)
        self.blockSignals(False)

    # Trap properties
    def registerProperties(self):
        self.properties = OrderedDict()
        self.registerProperty('x')
        self.registerProperty('y')
        self.registerProperty('z')
        self.registerProperty('alpha', decimals=2)
        self.registerProperty('phi', decimals=2)

    @pyqtProperty(QVector3D)
    def r(self):
        """Three-dimensional position of trap"""
        return self._r

    @r.setter
    def r(self, r):
        self._r = QVector3D(r)
        self.updateAppearance()
        self.computeHologram()
        logger.debug('setting r')

    @pyqtProperty(float)
    def x(self):
        return self._r.x()

    @x.setter
    def x(self, x):
        r = self._r
        r.setX(x)
        self.r = r

    @pyqtProperty(float)
    def y(self):
        return self._r.y()

    @y.setter
    def y(self, y):
        r = self._r
        r.setY(y)
        self.r = r

    @pyqtProperty(float)
    def z(self):
        return self._r.z()

    @z.setter
    def z(self, z):
        r = self._r
        r.setZ(z)
        self.r = r

    @pyqtProperty(float)
    def alpha(self):
        """Relative amplitude of trap"""
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        self._alpha = alpha
        self.amp = alpha * np.exp(1j * self.phi)
        self.computeHologram()

    @pyqtProperty(float)
    def phi(self):
        """Relative phase of trap"""
        return self._phi

    @phi.setter
    def phi(self, phi):
        self._phi = phi
        self.amp = self.alpha * np.exp(1j * phi)
        self.computeHologram()

    @pyqtProperty(object)
    def state(self):
        """Current state of trap"""
        return self._state

    @state.setter
    def state(self, state):
        if self.state is not states.static:
            self._state = state
            self.spot['brush'] = self.brush[state]
            self.appearanceChanged.emit()
