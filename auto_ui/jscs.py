# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jscs.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.pushButton_31 = QtWidgets.QPushButton(Form)
        self.pushButton_31.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_31.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_31.setObjectName("pushButton_31")
        self.verticalLayout_38.addWidget(self.pushButton_31)
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_38.addWidget(self.label_23)
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.verticalLayout_38.addWidget(self.comboBox_4)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_34 = QtWidgets.QPushButton(Form)
        self.pushButton_34.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_34.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_17.addWidget(self.pushButton_34)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_38.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_19.addLayout(self.verticalLayout_38)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.pushButton_32 = QtWidgets.QPushButton(Form)
        self.pushButton_32.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_32.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_32.setObjectName("pushButton_32")
        self.verticalLayout_39.addWidget(self.pushButton_32)
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_39.addWidget(self.label_24)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_18.addWidget(self.comboBox_5)
        self.pushButton_33 = QtWidgets.QPushButton(Form)
        self.pushButton_33.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_33.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_18.addWidget(self.pushButton_33)
        self.verticalLayout_39.addLayout(self.horizontalLayout_18)
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_39.addWidget(self.label_28)
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setMaximum(100000)
        self.spinBox_2.setProperty("value", 6000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_39.addWidget(self.spinBox_2)
        self.horizontalLayout_19.addLayout(self.verticalLayout_39)
        self.verticalLayout_43.addLayout(self.horizontalLayout_19)
        self.groupBox_14 = QtWidgets.QGroupBox(Form)
        self.groupBox_14.setStyleSheet("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.groupBox_14)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_42.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_14)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_42.addWidget(self.checkBox_5)
        self.label_29 = QtWidgets.QLabel(self.groupBox_14)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_42.addWidget(self.label_29)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_14)
        self.spinBox_3.setMaximum(100000)
        self.spinBox_3.setProperty("value", 1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_21.addWidget(self.spinBox_3)
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_35.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_35.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_21.addWidget(self.pushButton_35)
        self.verticalLayout_42.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_30 = QtWidgets.QLabel(self.groupBox_14)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_20.addWidget(self.label_30)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_14)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_20.addWidget(self.lineEdit_8)
        self.verticalLayout_42.addLayout(self.horizontalLayout_20)
        self.verticalLayout_43.addWidget(self.groupBox_14)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 2, 0, 1, 1)
        self.pushButton_run = QtWidgets.QPushButton(Form)
        self.pushButton_run.setObjectName("pushButton_run")
        self.gridLayout_5.addWidget(self.pushButton_run, 5, 0, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(Form)
        self.pushButton_36.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_36.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_5.addWidget(self.pushButton_36, 4, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 0, 1, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(Form)
        self.spinBox_4.setMaximum(100000)
        self.spinBox_4.setProperty("value", 20)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_5.addWidget(self.spinBox_4, 1, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 0, 0, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(Form)
        self.spinBox_5.setMaximum(100000)
        self.spinBox_5.setProperty("value", 5)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_5.addWidget(self.spinBox_5, 1, 1, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(Form)
        self.pushButton_37.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_37.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_5.addWidget(self.pushButton_37, 4, 1, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(Form)
        self.spinBox_6.setMaximum(100000)
        self.spinBox_6.setProperty("value", 10)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_5.addWidget(self.spinBox_6, 3, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(Form)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_5.addWidget(self.pushButton_stop, 6, 0, 1, 1)
        self.verticalLayout_43.addLayout(self.gridLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_43.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.verticalLayout_43)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_31.setText(_translate("Form", "Check Case..."))
        self.label_23.setText(_translate("Form", "Time Stepping Method"))
        self.comboBox_4.setItemText(0, _translate("Form", "Fixed"))
        self.pushButton_34.setText(_translate("Form", "Setting..."))
        self.pushButton_32.setText(_translate("Form", "Preview Mesh Motion..."))
        self.label_24.setText(_translate("Form", "Time Stepping Method"))
        self.comboBox_5.setItemText(0, _translate("Form", "Steady"))
        self.comboBox_5.setItemText(1, _translate("Form", "Fixed"))
        self.pushButton_33.setText(_translate("Form", "p"))
        self.label_28.setText(_translate("Form", "Number of Time Steps"))
        self.groupBox_14.setTitle(_translate("Form", "Options"))
        self.checkBox_4.setText(_translate("Form", "Extrapolate Variables"))
        self.checkBox_5.setText(_translate("Form", "Data Sampling for Time Statistics"))
        self.label_29.setText(_translate("Form", "Sampling Interval"))
        self.pushButton_35.setText(_translate("Form", "Sampling Options"))
        self.label_30.setText(_translate("Form", "Sampling Interval"))
        self.lineEdit_8.setText(_translate("Form", "0"))
        self.label_33.setText(_translate("Form", "Profile Update Interval"))
        self.pushButton_run.setText(_translate("Form", "Calculate"))
        self.pushButton_36.setText(_translate("Form", "Data File Quantities..."))
        self.label_32.setText(_translate("Form", "Reporting Interval"))
        self.label_31.setText(_translate("Form", "Max Iterations/Itme Step"))
        self.pushButton_37.setText(_translate("Form", "Acoustic Signals..."))
        self.pushButton_stop.setText(_translate("Form", "Stop"))
