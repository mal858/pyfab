# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore


def tabLayout(parent):
    """Standard layout for tab widgets."""

    layout = QtGui.QVBoxLayout(parent)
    layout.setAlignment(QtCore.Qt.AlignTop)
    layout.setSpacing(1)
    layout.setContentsMargins(1, 1, 1, 1)
    return layout
