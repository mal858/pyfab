from PyQt4 import QtCore, QtGui
import os
import numpy as np
from .ipglaser import ipglaser as ipg


class indicator(QtGui.QWidget):

    def __init__(self, title, states, **kwargs):
        super(indicator, self).__init__(**kwargs)
        self.title = title
        self.states = states
        self.init_ui()

    def init_ui(self):
        layout = QtGui.QVBoxLayout()
        layout.setMargin(0)
        layout.setSpacing(1)
        w = QtGui.QLabel(self.title)
        w.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(w)
        self.led = QtGui.QLabel()
        self.led.setAlignment(QtCore.Qt.AlignCenter)
        self.led.setPixmap(self.states[0])
        layout.addWidget(self.led)
        self.setLayout(layout)

    def set(self, state):
        self.led.setPixmap(self.states[state])


class status_widget(QtGui.QFrame):

    def __init__(self):
        super(status_widget, self).__init__()
        self.dir = os.path.dirname(__file__)
        self.led_size = 16
        self.init_ui()
        self.status(ipg.flag['AIM'])  # FIXME -- display purposes

    def init_ui(self):
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
        green_on = self.led_pixmap('green-led-on').scaledToWidth(self.led_size)
        green_off = self.led_pixmap(
            'green-led-off').scaledToWidth(self.led_size)
        amber_on = self.led_pixmap('amber-led-on').scaledToWidth(self.led_size)
        amber_off = self.led_pixmap(
            'amber-led-off').scaledToWidth(self.led_size)
        red_on = self.led_pixmap('red-led-on').scaledToWidth(self.led_size)
        red_off = self.led_pixmap('red-led-off').scaledToWidth(self.led_size)
        layout = QtGui.QHBoxLayout()
        self.led_key = indicator('keyswitch', [green_off, green_on])
        self.led_aim = indicator('  aiming ', [amber_off, amber_on])
        self.led_emx = indicator(' emission', [red_off, red_on, amber_on])
        self.led_flt = indicator('  fault  ', [amber_off, amber_on])
        layout.setMargin(2)
        layout.setSpacing(1)
        layout.addWidget(self.led_key)
        layout.addWidget(self.led_aim)
        layout.addWidget(self.led_emx)
        layout.addWidget(self.led_flt)
        self.setLayout(layout)

    def led_pixmap(self, name):
        filename = os.path.join(self.dir, 'icons/' + name + '.png')
        w = QtGui.QPixmap(filename)
        return w

    def status(self, flags):
        self.led_key.set(not bool(flags & ipg.flag['KEY']))
        self.led_aim.set(bool(flags & ipg.flag['AIM']))
        if (flags & ipg.flag['EMS']):
            self.led_emx.set(2)
        else:
            self.led_emx.set(bool(flags & ipg.flag['EMX']))
        error = bool(flags & ipg.flag['ERR'])
        self.led_flt.set(error)
        # if error:
        #    self.instrument.error(flags)


class power_widget(QtGui.QWidget):

    def __init__(self, **kwargs):
        super(power_widget, self).__init__(**kwargs)
        self.min = 0.
        self.max = 10.
        self.init_ui()
        self.value = 0

    def init_ui(self):
        layout = QtGui.QVBoxLayout()
        layout.setMargin(2)
        layout.setSpacing(1)
        title = QtGui.QLabel('power [W]')
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        v = QtGui.QDoubleValidator(self.min, self.max, 4.)
        v.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.wvalue = QtGui.QLineEdit()
        self.wvalue.setValidator(v)
        self.wvalue.setAlignment(QtCore.Qt.AlignRight)
        self.wvalue.setMaxLength(6)
        self.wvalue.setReadOnly(True)
        layout.addWidget(self.wvalue)
        self.setLayout(layout)

    @property
    def value(self):
        self._value

    @value.setter
    def value(self, _value):
        value = np.clip(float(_value), self.min, self.max)
        self._value = value
        self.wvalue.setText(QtCore.QString('%.4f' % value))


class QIPGLaser(QtGui.QFrame):

    def __init__(self):
        super(QIPGLaser, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setFrameShape(QtGui.QFrame.Box)
        layout = QtGui.QVBoxLayout()
        layout.setMargin(0)
        layout.setSpacing(0)
        layout.addWidget(QtGui.QLabel(' Trapping Laser'))
        layout.addWidget(self.display_widget())
        self.setLayout(layout)

    def display_widget(self):
        self.wstatus = status_widget()
        self.wpower = power_widget()
        w = QtGui.QWidget()
        layout = QtGui.QHBoxLayout()
        layout.setSpacing(1)
        layout.addWidget(self.wstatus)
        layout.addWidget(self.wpower)
        w.setLayout(layout)
        return w


def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    w = status_widget()
    w.show()
    sys.exit(app.exec_())