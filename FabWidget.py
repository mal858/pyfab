# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FabWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyFab(object):
    def setupUi(self, PyFab):
        PyFab.setObjectName("PyFab")
        PyFab.resize(1120, 610)
        self.centralwidget = QtWidgets.QWidget(PyFab)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.screen = QJansenScreen(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen.sizePolicy().hasHeightForWidth())
        self.screen.setSizePolicy(sizePolicy)
        self.screen.setMinimumSize(QtCore.QSize(640, 480))
        self.screen.setObjectName("screen")
        self.horizontalLayout_2.addWidget(self.screen)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.tabVideo = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabVideo.sizePolicy().hasHeightForWidth())
        self.tabVideo.setSizePolicy(sizePolicy)
        self.tabVideo.setMinimumSize(QtCore.QSize(0, 0))
        self.tabVideo.setAccessibleName("")
        self.tabVideo.setAccessibleDescription("")
        self.tabVideo.setObjectName("tabVideo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabVideo)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupSource = QtWidgets.QGroupBox(self.tabVideo)
        self.groupSource.setObjectName("groupSource")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupSource)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bcamera = QtWidgets.QRadioButton(self.groupSource)
        self.bcamera.setChecked(True)
        self.bcamera.setObjectName("bcamera")
        self.horizontalLayout.addWidget(self.bcamera)
        self.bfilters = QtWidgets.QRadioButton(self.groupSource)
        self.bfilters.setObjectName("bfilters")
        self.horizontalLayout.addWidget(self.bfilters)
        spacerItem = QtWidgets.QSpacerItem(283, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupSource)
        self.groupDvr = QtWidgets.QGroupBox(self.tabVideo)
        self.groupDvr.setMinimumSize(QtCore.QSize(0, 0))
        self.groupDvr.setObjectName("groupDvr")
        self.dvrLayout = QtWidgets.QVBoxLayout(self.groupDvr)
        self.dvrLayout.setContentsMargins(2, 2, 2, 2)
        self.dvrLayout.setSpacing(1)
        self.dvrLayout.setObjectName("dvrLayout")
        self.dvr = QDVR(self.groupDvr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dvr.sizePolicy().hasHeightForWidth())
        self.dvr.setSizePolicy(sizePolicy)
        self.dvr.setMinimumSize(QtCore.QSize(0, 0))
        self.dvr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dvr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dvr.setObjectName("dvr")
        self.dvrLayout.addWidget(self.dvr)
        self.verticalLayout.addWidget(self.groupDvr)
        self.groupCamera = QtWidgets.QGroupBox(self.tabVideo)
        self.groupCamera.setMinimumSize(QtCore.QSize(0, 0))
        self.groupCamera.setObjectName("groupCamera")
        self.cameraLayout = QtWidgets.QVBoxLayout(self.groupCamera)
        self.cameraLayout.setContentsMargins(2, 2, 2, 2)
        self.cameraLayout.setSpacing(1)
        self.cameraLayout.setObjectName("cameraLayout")
        self.camera = QtWidgets.QFrame(self.groupCamera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera.sizePolicy().hasHeightForWidth())
        self.camera.setSizePolicy(sizePolicy)
        self.camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera.setObjectName("camera")
        self.cameraLayout.addWidget(self.camera)
        self.verticalLayout.addWidget(self.groupCamera)
        self.groupFilters = QtWidgets.QGroupBox(self.tabVideo)
        self.groupFilters.setMinimumSize(QtCore.QSize(0, 0))
        self.groupFilters.setObjectName("groupFilters")
        self.filterLayout = QtWidgets.QVBoxLayout(self.groupFilters)
        self.filterLayout.setContentsMargins(2, 2, 2, 2)
        self.filterLayout.setSpacing(1)
        self.filterLayout.setObjectName("filterLayout")
        self.filters = QVideoFilter(self.groupFilters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filters.sizePolicy().hasHeightForWidth())
        self.filters.setSizePolicy(sizePolicy)
        self.filters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filters.setObjectName("filters")
        self.filterLayout.addWidget(self.filters)
        self.verticalLayout.addWidget(self.groupFilters)
        spacerItem1 = QtWidgets.QSpacerItem(20, 338, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabVideo, "")
        self.tabHistogram = QtWidgets.QWidget()
        self.tabHistogram.setObjectName("tabHistogram")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabHistogram)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.histogram = QHistogramTab(self.tabHistogram)
        self.histogram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.histogram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.histogram.setObjectName("histogram")
        self.verticalLayout_3.addWidget(self.histogram)
        self.tabWidget.addTab(self.tabHistogram, "")
        self.tabHardware = QtWidgets.QWidget()
        self.tabHardware.setObjectName("tabHardware")
        self.tabWidget.addTab(self.tabHardware, "")
        self.tabTraps = QtWidgets.QWidget()
        self.tabTraps.setObjectName("tabTraps")
        self.tabWidget.addTab(self.tabTraps, "")
        self.tabCGH = QtWidgets.QWidget()
        self.tabCGH.setObjectName("tabCGH")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabCGH)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QCGHPropertyWidget(self.tabCGH)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4.addWidget(self.frame)
        self.tabWidget.addTab(self.tabCGH, "")
        self.tabSLM = QtWidgets.QWidget()
        self.tabSLM.setObjectName("tabSLM")
        self.tabWidget.addTab(self.tabSLM, "")
        self.tabHelp = QtWidgets.QWidget()
        self.tabHelp.setObjectName("tabHelp")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabHelp)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bback = QtWidgets.QPushButton(self.tabHelp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bback.sizePolicy().hasHeightForWidth())
        self.bback.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/go-previous.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bback.setIcon(icon)
        self.bback.setObjectName("bback")
        self.verticalLayout_2.addWidget(self.bback)
        self.browser = QtWebKitWidgets.QWebView(self.tabHelp)
        self.browser.setProperty("url", QtCore.QUrl("qrc:/help/help/jansen.html"))
        self.browser.setObjectName("browser")
        self.verticalLayout_2.addWidget(self.browser)
        self.tabWidget.addTab(self.tabHelp, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        PyFab.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyFab)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTasks = QtWidgets.QMenu(self.menubar)
        self.menuTasks.setObjectName("menuTasks")
        PyFab.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyFab)
        self.statusbar.setObjectName("statusbar")
        PyFab.setStatusBar(self.statusbar)
        self.actionSavePhoto = QtWidgets.QAction(PyFab)
        self.actionSavePhoto.setObjectName("actionSavePhoto")
        self.actionSavePhotoAs = QtWidgets.QAction(PyFab)
        self.actionSavePhotoAs.setObjectName("actionSavePhotoAs")
        self.actionQuit = QtWidgets.QAction(PyFab)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave_Hologram = QtWidgets.QAction(PyFab)
        self.actionSave_Hologram.setObjectName("actionSave_Hologram")
        self.actionSave_Settings = QtWidgets.QAction(PyFab)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.menuFile.addAction(self.actionSavePhoto)
        self.menuFile.addAction(self.actionSavePhotoAs)
        self.menuFile.addAction(self.actionSave_Hologram)
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTasks.menuAction())

        self.retranslateUi(PyFab)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(PyFab.close)
        self.bback.clicked.connect(self.browser.back)
        self.tabWidget.currentChanged['int'].connect(self.histogram.expose)
        self.dvr.recording['bool'].connect(self.camera.setDisabled)
        self.dvr.recording['bool'].connect(self.filters.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(PyFab)

    def retranslateUi(self, PyFab):
        _translate = QtCore.QCoreApplication.translate
        PyFab.setWindowTitle(_translate("PyFab", "MainWindow"))
        self.tabWidget.setStatusTip(_translate("PyFab", "Record from video camera directly"))
        self.groupSource.setTitle(_translate("PyFab", "Recording Source"))
        self.bcamera.setStatusTip(_translate("PyFab", "Record raw video from camera"))
        self.bcamera.setText(_translate("PyFab", "Camera"))
        self.bfilters.setStatusTip(_translate("PyFab", "Record filtered video stream"))
        self.bfilters.setText(_translate("PyFab", "Filters"))
        self.groupDvr.setTitle(_translate("PyFab", "Video Recorder"))
        self.groupCamera.setTitle(_translate("PyFab", "Video Camera"))
        self.groupFilters.setTitle(_translate("PyFab", "Video Filters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVideo), _translate("PyFab", "Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHistogram), _translate("PyFab", "Histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHardware), _translate("PyFab", "Hardware"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTraps), _translate("PyFab", "Traps"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCGH), _translate("PyFab", "CGH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSLM), _translate("PyFab", "SLM"))
        self.bback.setText(_translate("PyFab", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHelp), _translate("PyFab", "Help"))
        self.menuFile.setTitle(_translate("PyFab", "File"))
        self.menuTasks.setTitle(_translate("PyFab", "Tasks"))
        self.actionSavePhoto.setText(_translate("PyFab", "Save Photo"))
        self.actionSavePhoto.setShortcut(_translate("PyFab", "Ctrl+S"))
        self.actionSavePhotoAs.setText(_translate("PyFab", "Save Photo As ..."))
        self.actionSavePhotoAs.setShortcut(_translate("PyFab", "Ctrl+A"))
        self.actionQuit.setText(_translate("PyFab", "Quit"))
        self.actionSave_Hologram.setText(_translate("PyFab", "Save Hologram..."))
        self.actionSave_Settings.setText(_translate("PyFab", "Save Settings"))


from PyQt5 import QtWebKitWidgets
from jansenlib.QDVR.QDVR import QDVR
from jansenlib.QHistogramTab import QHistogramTab
from jansenlib.QJansenScreen import QJansenScreen
from jansenlib.video.QVideoFilter.QVideoFilter import QVideoFilter
from pyfablib.CGH.QCGHPropertyWidget import QCGHPropertyWidget
import help_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyFab = QtWidgets.QMainWindow()
    ui = Ui_PyFab()
    ui.setupUi(PyFab)
    PyFab.show()
    sys.exit(app.exec_())
