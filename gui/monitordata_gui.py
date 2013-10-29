# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitordata.ui'
#
# Created: Tue Oct 29 14:53:17 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(246, 312)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.panel = QtGui.QWidget(Form)
        self.panel.setStyleSheet(_fromUtf8("QWidget#panel{\n"
"border-radius: 5px; \n"
"border: 1px solid black;}"))
        self.panel.setObjectName(_fromUtf8("panel"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.panel)
        self.verticalLayout_2.setContentsMargins(15, 10, 15, 10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.glMonitor = QtGui.QGridLayout()
        self.glMonitor.setMargin(0)
        self.glMonitor.setObjectName(_fromUtf8("glMonitor"))
        self.lbPaciente = QtGui.QLabel(self.panel)
        self.lbPaciente.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbPaciente.setFont(font)
        self.lbPaciente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbPaciente.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);\n"
"text-decoration: underline;"))
        self.lbPaciente.setObjectName(_fromUtf8("lbPaciente"))
        self.glMonitor.addWidget(self.lbPaciente, 1, 1, 1, 1)
        self.imgPaciente = QtGui.QLabel(self.panel)
        self.imgPaciente.setMaximumSize(QtCore.QSize(32, 32))
        self.imgPaciente.setText(_fromUtf8(""))
        self.imgPaciente.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_paciente.png")))
        self.imgPaciente.setObjectName(_fromUtf8("imgPaciente"))
        self.glMonitor.addWidget(self.imgPaciente, 1, 0, 1, 1)
        self.lbO2 = QtGui.QLabel(self.panel)
        self.lbO2.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbO2.setFont(font)
        self.lbO2.setObjectName(_fromUtf8("lbO2"))
        self.glMonitor.addWidget(self.lbO2, 3, 1, 1, 1)
        self.alertTemperatura = QtGui.QLabel(self.panel)
        self.alertTemperatura.setMaximumSize(QtCore.QSize(32, 32))
        self.alertTemperatura.setText(_fromUtf8(""))
        self.alertTemperatura.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_alert.png")))
        self.alertTemperatura.setObjectName(_fromUtf8("alertTemperatura"))
        self.glMonitor.addWidget(self.alertTemperatura, 4, 2, 1, 1)
        self.alertPressao = QtGui.QLabel(self.panel)
        self.alertPressao.setMinimumSize(QtCore.QSize(32, 0))
        self.alertPressao.setMaximumSize(QtCore.QSize(32, 32))
        self.alertPressao.setText(_fromUtf8(""))
        self.alertPressao.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_alert.png")))
        self.alertPressao.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.alertPressao.setObjectName(_fromUtf8("alertPressao"))
        self.glMonitor.addWidget(self.alertPressao, 2, 2, 1, 1)
        self.imgPressao = QtGui.QLabel(self.panel)
        self.imgPressao.setMaximumSize(QtCore.QSize(32, 32))
        self.imgPressao.setText(_fromUtf8(""))
        self.imgPressao.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_pressao1.png")))
        self.imgPressao.setObjectName(_fromUtf8("imgPressao"))
        self.glMonitor.addWidget(self.imgPressao, 2, 0, 1, 1)
        self.lbPressao = QtGui.QLabel(self.panel)
        self.lbPressao.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbPressao.setFont(font)
        self.lbPressao.setObjectName(_fromUtf8("lbPressao"))
        self.glMonitor.addWidget(self.lbPressao, 2, 1, 1, 1)
        self.lbFC = QtGui.QLabel(self.panel)
        self.lbFC.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbFC.setFont(font)
        self.lbFC.setTextFormat(QtCore.Qt.RichText)
        self.lbFC.setObjectName(_fromUtf8("lbFC"))
        self.glMonitor.addWidget(self.lbFC, 5, 1, 1, 1)
        self.alertFC = QtGui.QLabel(self.panel)
        self.alertFC.setMaximumSize(QtCore.QSize(32, 32))
        self.alertFC.setText(_fromUtf8(""))
        self.alertFC.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_alert.png")))
        self.alertFC.setObjectName(_fromUtf8("alertFC"))
        self.glMonitor.addWidget(self.alertFC, 5, 2, 1, 1)
        self.imgECGStatus = QtGui.QLabel(self.panel)
        self.imgECGStatus.setMaximumSize(QtCore.QSize(32, 32))
        self.imgECGStatus.setText(_fromUtf8(""))
        self.imgECGStatus.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_ecg0.png")))
        self.imgECGStatus.setObjectName(_fromUtf8("imgECGStatus"))
        self.glMonitor.addWidget(self.imgECGStatus, 6, 0, 1, 1)
        self.lbTemperatura = QtGui.QLabel(self.panel)
        self.lbTemperatura.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbTemperatura.setFont(font)
        self.lbTemperatura.setObjectName(_fromUtf8("lbTemperatura"))
        self.glMonitor.addWidget(self.lbTemperatura, 4, 1, 1, 1)
        self.alertECGStatus = QtGui.QLabel(self.panel)
        self.alertECGStatus.setMaximumSize(QtCore.QSize(32, 32))
        self.alertECGStatus.setText(_fromUtf8(""))
        self.alertECGStatus.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_alert.png")))
        self.alertECGStatus.setObjectName(_fromUtf8("alertECGStatus"))
        self.glMonitor.addWidget(self.alertECGStatus, 6, 2, 1, 1)
        self.imgTemperatura = QtGui.QLabel(self.panel)
        self.imgTemperatura.setMaximumSize(QtCore.QSize(32, 32))
        self.imgTemperatura.setText(_fromUtf8(""))
        self.imgTemperatura.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_temperatura2.png")))
        self.imgTemperatura.setObjectName(_fromUtf8("imgTemperatura"))
        self.glMonitor.addWidget(self.imgTemperatura, 4, 0, 1, 1)
        self.imgFC = QtGui.QLabel(self.panel)
        self.imgFC.setMaximumSize(QtCore.QSize(32, 32))
        self.imgFC.setText(_fromUtf8(""))
        self.imgFC.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_fc.png")))
        self.imgFC.setObjectName(_fromUtf8("imgFC"))
        self.glMonitor.addWidget(self.imgFC, 5, 0, 1, 1)
        self.imgO2 = QtGui.QLabel(self.panel)
        self.imgO2.setMaximumSize(QtCore.QSize(32, 32))
        self.imgO2.setText(_fromUtf8(""))
        self.imgO2.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_spo.png")))
        self.imgO2.setObjectName(_fromUtf8("imgO2"))
        self.glMonitor.addWidget(self.imgO2, 3, 0, 1, 1)
        self.imgMonitor = QtGui.QLabel(self.panel)
        self.imgMonitor.setMaximumSize(QtCore.QSize(32, 32))
        self.imgMonitor.setText(_fromUtf8(""))
        self.imgMonitor.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_monitor1.png")))
        self.imgMonitor.setObjectName(_fromUtf8("imgMonitor"))
        self.glMonitor.addWidget(self.imgMonitor, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(37, 32, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.glMonitor.addItem(spacerItem, 1, 2, 1, 1)
        self.lbECGStatus = QtGui.QLabel(self.panel)
        self.lbECGStatus.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbECGStatus.setFont(font)
        self.lbECGStatus.setObjectName(_fromUtf8("lbECGStatus"))
        self.glMonitor.addWidget(self.lbECGStatus, 6, 1, 1, 1)
        self.alertO2 = QtGui.QLabel(self.panel)
        self.alertO2.setMaximumSize(QtCore.QSize(32, 32))
        self.alertO2.setText(_fromUtf8(""))
        self.alertO2.setPixmap(QtGui.QPixmap(_fromUtf8("icones/img_alert.png")))
        self.alertO2.setObjectName(_fromUtf8("alertO2"))
        self.glMonitor.addWidget(self.alertO2, 3, 2, 1, 1)
        self.lbMonitor = QtGui.QLabel(self.panel)
        self.lbMonitor.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbMonitor.setFont(font)
        self.lbMonitor.setObjectName(_fromUtf8("lbMonitor"))
        self.glMonitor.addWidget(self.lbMonitor, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.glMonitor)
        self.horizontalLayout.addWidget(self.panel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPaciente.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p>John Doo</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbO2.setText(QtGui.QApplication.translate("Form", "00 %", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPressao.setText(QtGui.QApplication.translate("Form", "000/00 mmmHG", None, QtGui.QApplication.UnicodeUTF8))
        self.lbFC.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p>00 BPM</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTemperatura.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p>00 <span style=\" vertical-align:super;\">o</span>C</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbECGStatus.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p>Normal</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbMonitor.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p>01</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

