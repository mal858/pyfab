# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QVisionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QVisionWidget(object):
    def setupUi(self, QVisionWidget):
        QVisionWidget.setObjectName("QVisionWidget")
        QVisionWidget.setEnabled(True)
        QVisionWidget.resize(600, 742)
        self.verticalLayout = QtWidgets.QVBoxLayout(QVisionWidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupProcess = QtWidgets.QGroupBox(QVisionWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupProcess.setFont(font)
        self.groupProcess.setObjectName("groupProcess")
        self.formLayout = QtWidgets.QFormLayout(self.groupProcess)
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.breal = QtWidgets.QRadioButton(self.groupProcess)
        self.breal.setObjectName("breal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.breal)
        self.bpost = QtWidgets.QRadioButton(self.groupProcess)
        self.bpost.setChecked(True)
        self.bpost.setObjectName("bpost")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bpost)
        self.skipBox = QtWidgets.QSpinBox(self.groupProcess)
        self.skipBox.setMaximum(50)
        self.skipBox.setProperty("value", 5)
        self.skipBox.setObjectName("skipBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.skipBox)
        self.checkNormalize = QtWidgets.QCheckBox(self.groupProcess)
        self.checkNormalize.setObjectName("checkNormalize")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkNormalize)
        self.verticalLayout.addWidget(self.groupProcess)
        self.groupPipeline = QtWidgets.QGroupBox(QVisionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupPipeline.sizePolicy().hasHeightForWidth())
        self.groupPipeline.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupPipeline.setFont(font)
        self.groupPipeline.setObjectName("groupPipeline")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupPipeline)
        self.horizontalLayout.setContentsMargins(-1, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bDetect = QtWidgets.QCheckBox(self.groupPipeline)
        self.bDetect.setObjectName("bDetect")
        self.horizontalLayout.addWidget(self.bDetect)
        self.bEstimate = QtWidgets.QCheckBox(self.groupPipeline)
        self.bEstimate.setObjectName("bEstimate")
        self.horizontalLayout.addWidget(self.bEstimate)
        self.bRefine = QtWidgets.QCheckBox(self.groupPipeline)
        self.bRefine.setObjectName("bRefine")
        self.horizontalLayout.addWidget(self.bRefine)
        self.verticalLayout.addWidget(self.groupPipeline)
        self.groupExport = QtWidgets.QGroupBox(QVisionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupExport.sizePolicy().hasHeightForWidth())
        self.groupExport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupExport.setFont(font)
        self.groupExport.setObjectName("groupExport")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupExport)
        self.formLayout_2.setContentsMargins(2, 2, 2, 2)
        self.formLayout_2.setHorizontalSpacing(12)
        self.formLayout_2.setVerticalSpacing(2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkFrames = QtWidgets.QCheckBox(self.groupExport)
        self.checkFrames.setChecked(False)
        self.checkFrames.setTristate(False)
        self.checkFrames.setObjectName("checkFrames")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.checkFrames)
        self.checkTrajectories = QtWidgets.QCheckBox(self.groupExport)
        self.checkTrajectories.setObjectName("checkTrajectories")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.checkTrajectories)
        self.label = QtWidgets.QLabel(self.groupExport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinTol = QtWidgets.QDoubleSpinBox(self.groupExport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinTol.sizePolicy().hasHeightForWidth())
        self.spinTol.setSizePolicy(sizePolicy)
        self.spinTol.setPrefix("")
        self.spinTol.setProperty("value", 5.0)
        self.spinTol.setObjectName("spinTol")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinTol)
        self.checkFeatureData = QtWidgets.QCheckBox(self.groupExport)
        self.checkFeatureData.setObjectName("checkFeatureData")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.checkFeatureData)
        self.verticalLayout.addWidget(self.groupExport)
        self.plot = PlotWidget(QVisionWidget)
        self.plot.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName("plot")
        self.verticalLayout.addWidget(self.plot)

        self.retranslateUi(QVisionWidget)
        QtCore.QMetaObject.connectSlotsByName(QVisionWidget)

    def retranslateUi(self, QVisionWidget):
        _translate = QtCore.QCoreApplication.translate
        QVisionWidget.setWindowTitle(_translate("QVisionWidget", "Form"))
        self.groupProcess.setTitle(_translate("QVisionWidget", "Processing"))
        self.breal.setText(_translate("QVisionWidget", "Real-time"))
        self.bpost.setText(_translate("QVisionWidget", "Post-process"))
        self.skipBox.setSuffix(_translate("QVisionWidget", " frames"))
        self.skipBox.setPrefix(_translate("QVisionWidget", "Skip "))
        self.checkNormalize.setText(_translate("QVisionWidget", "Normalize"))
        self.groupPipeline.setTitle(_translate("QVisionWidget", "Analysis pipeline"))
        self.bDetect.setText(_translate("QVisionWidget", "Detect"))
        self.bEstimate.setText(_translate("QVisionWidget", "Estimate"))
        self.bRefine.setText(_translate("QVisionWidget", "Refine"))
        self.groupExport.setTitle(_translate("QVisionWidget", "Save"))
        self.checkFrames.setText(_translate("QVisionWidget", "Frames"))
        self.checkTrajectories.setText(_translate("QVisionWidget", "Trajectories"))
        self.label.setText(_translate("QVisionWidget", "Link tolerance"))
        self.spinTol.setSuffix(_translate("QVisionWidget", " pixels"))
        self.checkFeatureData.setText(_translate("QVisionWidget", "Feature data"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QVisionWidget = QtWidgets.QWidget()
    ui = Ui_QVisionWidget()
    ui.setupUi(QVisionWidget)
    QVisionWidget.show()
    sys.exit(app.exec_())

