# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis\dxlmx.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 328)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        self.groupBox_7.setStyleSheet("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_17 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_17.setObjectName("radioButton_17")
        self.verticalLayout_3.addWidget(self.radioButton_17)
        self.radioButton_18 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_18.setObjectName("radioButton_18")
        self.verticalLayout_3.addWidget(self.radioButton_18)
        self.radioButton_19 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_19.setChecked(True)
        self.radioButton_19.setObjectName("radioButton_19")
        self.verticalLayout_3.addWidget(self.radioButton_19)
        self.radioButton_20 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_20.setEnabled(False)
        self.radioButton_20.setChecked(False)
        self.radioButton_20.setObjectName("radioButton_20")
        self.verticalLayout_3.addWidget(self.radioButton_20)
        self.verticalLayout_11.addWidget(self.groupBox_7)
        self.groupBox_9 = QtWidgets.QGroupBox(Form)
        self.groupBox_9.setStyleSheet("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_19.addWidget(self.checkBox_2)
        self.verticalLayout_11.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(Form)
        self.groupBox_10.setStyleSheet("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_20.addWidget(self.checkBox_3)
        self.verticalLayout_11.addWidget(self.groupBox_10)
        self.verticalLayout_22.addLayout(self.verticalLayout_11)
        self.groupBox_15 = QtWidgets.QGroupBox(Form)
        self.groupBox_15.setStyleSheet("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.groupBox_15)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.radioButton_2d = QtWidgets.QRadioButton(self.groupBox_15)
        self.radioButton_2d.setChecked(True)
        self.radioButton_2d.setObjectName("radioButton_2d")
        self.verticalLayout_45.addWidget(self.radioButton_2d)
        self.radioButton_3d = QtWidgets.QRadioButton(self.groupBox_15)
        self.radioButton_3d.setEnabled(True)
        self.radioButton_3d.setChecked(False)
        self.radioButton_3d.setObjectName("radioButton_3d")
        self.verticalLayout_45.addWidget(self.radioButton_3d)
        self.verticalLayout_22.addWidget(self.groupBox_15)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_22)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.groupBox_8 = QtWidgets.QGroupBox(Form)
        self.groupBox_8.setStyleSheet("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_8)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 32))
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_18.addWidget(self.spinBox)
        self.verticalLayout_21.addWidget(self.groupBox_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_21)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_7.setTitle(_translate("Form", "Model"))
        self.radioButton_17.setText(_translate("Form", "OFF"))
        self.radioButton_18.setText(_translate("Form", "Volume of Fluid"))
        self.radioButton_19.setText(_translate("Form", "Mixture"))
        self.radioButton_20.setText(_translate("Form", "Eulerian"))
        self.groupBox_9.setTitle(_translate("Form", "Mixture Parameters"))
        self.checkBox_2.setText(_translate("Form", "Slip Velocity"))
        self.groupBox_10.setTitle(_translate("Form", "Body Force Formulation"))
        self.checkBox_3.setText(_translate("Form", "Implicit Body Force"))
        self.groupBox_15.setTitle(_translate("Form", "Dimension"))
        self.radioButton_2d.setText(_translate("Form", "2D"))
        self.radioButton_3d.setText(_translate("Form", "3D"))
        self.groupBox_8.setTitle(_translate("Form", "Number of Eulerian Phases"))