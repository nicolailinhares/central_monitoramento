# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarms.ui'
#
# Created: Thu Oct 31 11:57:25 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AlarmsForm(object):
    def setupUi(self, AlarmsForm):
        AlarmsForm.setObjectName(_fromUtf8("AlarmsForm"))
        AlarmsForm.resize(571, 146)
        self.verticalLayout = QtGui.QVBoxLayout(AlarmsForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_alarms = QtGui.QGridLayout()
        self.gridLayout_alarms.setObjectName(_fromUtf8("gridLayout_alarms"))
        self.edtMinTemp_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMinTemp_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMinTemp_3.setObjectName(_fromUtf8("edtMinTemp_3"))
        self.gridLayout_alarms.addWidget(self.edtMinTemp_3, 1, 3, 1, 1)
        self.label_30 = QtGui.QLabel(AlarmsForm)
        self.label_30.setMinimumSize(QtCore.QSize(270, 0))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_alarms.addWidget(self.label_30, 2, 1, 1, 1)
        self.label_29 = QtGui.QLabel(AlarmsForm)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_alarms.addWidget(self.label_29, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem, 2, 6, 1, 1)
        self.label_36 = QtGui.QLabel(AlarmsForm)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_alarms.addWidget(self.label_36, 1, 2, 1, 1)
        self.label_39 = QtGui.QLabel(AlarmsForm)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_alarms.addWidget(self.label_39, 3, 2, 1, 1)
        self.label_32 = QtGui.QLabel(AlarmsForm)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_alarms.addWidget(self.label_32, 0, 4, 1, 1)
        self.label_38 = QtGui.QLabel(AlarmsForm)
        self.label_38.setMinimumSize(QtCore.QSize(270, 0))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_alarms.addWidget(self.label_38, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem1, 3, 6, 1, 1)
        self.label_31 = QtGui.QLabel(AlarmsForm)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_alarms.addWidget(self.label_31, 0, 2, 1, 1)
        self.edtMinPres_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMinPres_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMinPres_3.setObjectName(_fromUtf8("edtMinPres_3"))
        self.gridLayout_alarms.addWidget(self.edtMinPres_3, 0, 3, 1, 1)
        self.edtMinOxi_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMinOxi_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMinOxi_3.setObjectName(_fromUtf8("edtMinOxi_3"))
        self.gridLayout_alarms.addWidget(self.edtMinOxi_3, 2, 3, 1, 1)
        self.label_40 = QtGui.QLabel(AlarmsForm)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_alarms.addWidget(self.label_40, 3, 4, 1, 1)
        self.edtMaxFc_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMaxFc_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMaxFc_3.setObjectName(_fromUtf8("edtMaxFc_3"))
        self.gridLayout_alarms.addWidget(self.edtMaxFc_3, 3, 5, 1, 1)
        self.label_37 = QtGui.QLabel(AlarmsForm)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_alarms.addWidget(self.label_37, 2, 4, 1, 1)
        self.label_33 = QtGui.QLabel(AlarmsForm)
        self.label_33.setMinimumSize(QtCore.QSize(270, 0))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_alarms.addWidget(self.label_33, 1, 1, 1, 1)
        self.edtMaxPres_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMaxPres_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMaxPres_3.setObjectName(_fromUtf8("edtMaxPres_3"))
        self.gridLayout_alarms.addWidget(self.edtMaxPres_3, 0, 5, 1, 1)
        self.edtMaxTemp_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMaxTemp_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMaxTemp_3.setObjectName(_fromUtf8("edtMaxTemp_3"))
        self.gridLayout_alarms.addWidget(self.edtMaxTemp_3, 1, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem2, 0, 6, 1, 1)
        self.edtMinFc_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMinFc_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMinFc_3.setObjectName(_fromUtf8("edtMinFc_3"))
        self.gridLayout_alarms.addWidget(self.edtMinFc_3, 3, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem3, 1, 6, 1, 1)
        self.label_35 = QtGui.QLabel(AlarmsForm)
        self.label_35.setMinimumSize(QtCore.QSize(270, 0))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_alarms.addWidget(self.label_35, 0, 1, 1, 1)
        self.label_34 = QtGui.QLabel(AlarmsForm)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_alarms.addWidget(self.label_34, 1, 4, 1, 1)
        self.edtMaxOxi_3 = QtGui.QLineEdit(AlarmsForm)
        self.edtMaxOxi_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edtMaxOxi_3.setObjectName(_fromUtf8("edtMaxOxi_3"))
        self.gridLayout_alarms.addWidget(self.edtMaxOxi_3, 2, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem6, 2, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_alarms.addItem(spacerItem7, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_alarms)

        self.retranslateUi(AlarmsForm)
        QtCore.QMetaObject.connectSlotsByName(AlarmsForm)

    def retranslateUi(self, AlarmsForm):
        AlarmsForm.setWindowTitle(_translate("AlarmsForm", "Form", None))
        self.edtMinTemp_3.setText(_translate("AlarmsForm", "35", None))
        self.label_30.setText(_translate("AlarmsForm", "SPO2", None))
        self.label_29.setText(_translate("AlarmsForm", "Minimum", None))
        self.label_36.setText(_translate("AlarmsForm", "Minimum", None))
        self.label_39.setText(_translate("AlarmsForm", "Minimum", None))
        self.label_32.setText(_translate("AlarmsForm", "Maximum", None))
        self.label_38.setText(_translate("AlarmsForm", "Cardiac Frequency", None))
        self.label_31.setText(_translate("AlarmsForm", "Minimum", None))
        self.edtMinPres_3.setText(_translate("AlarmsForm", "90/70", None))
        self.edtMinOxi_3.setText(_translate("AlarmsForm", "90", None))
        self.label_40.setText(_translate("AlarmsForm", "Maximum", None))
        self.edtMaxFc_3.setText(_translate("AlarmsForm", "95", None))
        self.label_37.setText(_translate("AlarmsForm", "Maximum", None))
        self.label_33.setText(_translate("AlarmsForm", "Temperature", None))
        self.edtMaxPres_3.setText(_translate("AlarmsForm", "140/90", None))
        self.edtMaxTemp_3.setText(_translate("AlarmsForm", "38", None))
        self.edtMinFc_3.setText(_translate("AlarmsForm", "45", None))
        self.label_35.setText(_translate("AlarmsForm", "Pressure", None))
        self.label_34.setText(_translate("AlarmsForm", "Maximum", None))
        self.edtMaxOxi_3.setText(_translate("AlarmsForm", "100", None))

