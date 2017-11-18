from PyQt4 import QtGui
from fabdvr import fabdvr


class QFabDVR(fabdvr, QtGui.QWidget):

    def __init__(self, **kwargs):
        super(QFabDVR, self).__init__(**kwargs)
        self.initUI()

    def initUI(self):
        layout = QtGui.QHBoxLayout(self)
        self.brecord = QtGui.QPushButton('Record', self)
        self.bstop = QtGui.QPushButton('Stop', self)
        self.wframe = QtGui.QLCDNumber(self)
        self.wframe.setNumDigits(5)
        layout.addWidget(self.brecord)
        layout.addWidget(self.bstop)
        layout.addWidget(self.wframe)
        self.setLayout(layout)
        self.brecord.clicked.connect(self.handleRecord)
        self.bstop.clicked.connect(self.handleStop)

    def write(self, frame):
        super(QFabDVR, self).write(frame)
        self.wframe.display(self.framenumber)

    def handleRecord(self):
        super(QFabDVR, self).record(1000)

    def handleStop(self):
        super(QFabDVR, self).stop()

        
def main():
    import sys
    from QCameraItem import QCameraDevice, QCameraItem, QCameraWidget
    
    app = QtGui.QApplication(sys.argv)
    device = QCameraDevice(size=(640, 480), gray=True)
    camera = QCameraItem(device)
    widget = QCameraWidget(camera, background='w')
    widget.show()
    dvr = QFabDVR(camera=camera)
    dvr.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()