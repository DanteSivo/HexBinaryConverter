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
        MainWindow.resize(528, 312)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HexLabel = QtWidgets.QLabel(self.centralwidget)
        self.HexLabel.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HexLabel.setFont(font)
        self.HexLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HexLabel.setObjectName("HexLabel")
        self.DecLabel = QtWidgets.QLabel(self.centralwidget)
        self.DecLabel.setGeometry(QtCore.QRect(10, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DecLabel.setFont(font)
        self.DecLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DecLabel.setObjectName("DecLabel")

        self.HexToDec = QtWidgets.QPushButton(self.centralwidget)
        self.HexToDec.setGeometry(QtCore.QRect(280, 140, 111, 51))
        self.HexToDec.setObjectName("HexToDec")
        self.HexToDec.clicked.connect(self.ConvertHexToDec)

        self.DecToHex = QtWidgets.QPushButton(self.centralwidget)
        self.DecToHex.setGeometry(QtCore.QRect(410, 140, 111, 51))
        self.DecToHex.setObjectName("DecToHex")
        self.DecToHex.clicked.connect(self.ConvertDecToHex)

        self.LengthLabel = QtWidgets.QLabel(self.centralwidget)
        self.LengthLabel.setGeometry(QtCore.QRect(10, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LengthLabel.setFont(font)
        self.LengthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LengthLabel.setObjectName("LengthLabel")
        self.HexResult = QtWidgets.QLabel(self.centralwidget)
        self.HexResult.setGeometry(QtCore.QRect(30, 210, 221, 61))
        self.HexResult.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.HexResult.setFrameShape(QtWidgets.QFrame.Box)
        self.HexResult.setText("")
        self.HexResult.setAlignment(QtCore.Qt.AlignCenter)
        self.HexResult.setObjectName("HexResult")
        self.DecResult = QtWidgets.QLabel(self.centralwidget)
        self.DecResult.setGeometry(QtCore.QRect(300, 210, 221, 61))
        self.DecResult.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DecResult.setFrameShape(QtWidgets.QFrame.Box)
        self.DecResult.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DecResult.setText("")
        self.DecResult.setAlignment(QtCore.Qt.AlignCenter)
        self.DecResult.setWordWrap(False)
        self.DecResult.setObjectName("DecResult")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 210, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.DecText = QtWidgets.QLineEdit(self.centralwidget)
        self.DecText.setGeometry(QtCore.QRect(140, 80, 381, 51))
        self.DecText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DecText.setAlignment(QtCore.Qt.AlignCenter)
        self.DecText.setObjectName("DecText")
        self.HexText = QtWidgets.QLineEdit(self.centralwidget)
        self.HexText.setGeometry(QtCore.QRect(140, 20, 381, 51))
        self.HexText.setAlignment(QtCore.Qt.AlignCenter)
        self.HexText.setObjectName("HexText")
        self.LengthText = QtWidgets.QLineEdit(self.centralwidget)
        self.LengthText.setGeometry(QtCore.QRect(140, 140, 121, 51))
        self.LengthText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LengthText.setAlignment(QtCore.Qt.AlignCenter)
        self.LengthText.setObjectName("LengthText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 21))
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
        self.label.setText(_translate("MainWindow", "<-->"))

    def ConvertHexToDec(self):
        #self.HexText.text()  Determine the hexadecimal text
        dec_val = 0 # Value of Decimal Conversion, start at 0.
        hex_value = list(self.HexText.text())
        if self.LengthText.text() is not None:
            counter = int(self.LengthText.text())
            for i in range(0, counter):
                dec_val += int(hex_value[i])
        self.DecResult.setText(str(dec_val))

    def ConvertDecToHex(self):
        # Fill out once HexToDec is completed
        print(None)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
