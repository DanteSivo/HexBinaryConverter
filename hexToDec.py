# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HexText = QtWidgets.QLineEdit(self.centralwidget)
        self.HexText.setGeometry(QtCore.QRect(150, 10, 371, 51))
        self.HexText.setObjectName("HexText")
        self.DecText = QtWidgets.QLineEdit(self.centralwidget)
        self.DecText.setGeometry(QtCore.QRect(150, 80, 371, 51))
        self.DecText.setObjectName("DecText")
        self.HexLabel = QtWidgets.QLabel(self.centralwidget)
        self.HexLabel.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HexLabel.setFont(font)
        self.HexLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HexLabel.setObjectName("HexLabel")
        self.DecLabel = QtWidgets.QLabel(self.centralwidget)
        self.DecLabel.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DecLabel.setFont(font)
        self.DecLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DecLabel.setObjectName("DecLabel")
        self.HexToDec = QtWidgets.QPushButton(self.centralwidget)
        self.HexToDec.setGeometry(QtCore.QRect(280, 140, 111, 51))
        self.HexToDec.setObjectName("HexToDec")
        self.DecToHex = QtWidgets.QPushButton(self.centralwidget)
        self.DecToHex.setGeometry(QtCore.QRect(410, 140, 111, 51))
        self.DecToHex.setObjectName("DecToHex")
        self.LegnthText = QtWidgets.QLineEdit(self.centralwidget)
        self.LegnthText.setGeometry(QtCore.QRect(150, 140, 111, 51))
        self.LegnthText.setObjectName("LegnthText")
        self.LengthLabel = QtWidgets.QLabel(self.centralwidget)
        self.LengthLabel.setGeometry(QtCore.QRect(20, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LengthLabel.setFont(font)
        self.LengthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LengthLabel.setObjectName("LengthLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.HexLabel.setText(_translate("MainWindow", "Hexadecimal"))
        self.DecLabel.setText(_translate("MainWindow", "Decimal"))
        self.HexToDec.setText(_translate("MainWindow", "Hex->Decimal"))
        self.DecToHex.setText(_translate("MainWindow", "Decimal->Hex"))
        self.LengthLabel.setText(_translate("MainWindow", "Length"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
