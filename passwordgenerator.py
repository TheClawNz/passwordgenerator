# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordgenerator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: #141414;\n"
"color: #fff")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget") 
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(180, 160, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: none;")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.buttonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerate.setGeometry(QtCore.QRect(200, 270, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buttonGenerate.setFont(font)
        self.buttonGenerate.setStyleSheet("background-color: #5539cc;\n"
"color: #fff;")
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.buttonCopy = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCopy.setGeometry(QtCore.QRect(400, 270, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buttonCopy.setFont(font)
        self.buttonCopy.setStyleSheet("background-color: #5539cc;\n"
"color: #fff;")
        self.buttonCopy.setObjectName("buttonCopy")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(190, 400, 111, 22))
        self.spinBox.setMinimum(5)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox") 

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 360, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;")
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Şifre Oluşturucu - By TheClawNz#7987")) 
        self.password.setText(_translate("MainWindow", "Şifre"))
        self.buttonGenerate.setText(_translate("MainWindow", "Oluştur"))
        self.buttonCopy.setText(_translate("MainWindow", "Kopyala"))
        self.label.setText(_translate("MainWindow", "Uzunluk"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
