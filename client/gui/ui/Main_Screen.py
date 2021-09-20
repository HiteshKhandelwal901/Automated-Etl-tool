# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImagrButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImagrButton.setGeometry(QtCore.QRect(150, 130, 191, 111))
        self.ImagrButton.setObjectName("ImagrButton")
        self.StructuredButton = QtWidgets.QPushButton(self.centralwidget)
        self.StructuredButton.setGeometry(QtCore.QRect(420, 130, 191, 111))
        self.StructuredButton.setObjectName("StructuredButton")
        self.AudioButton = QtWidgets.QPushButton(self.centralwidget)
        self.AudioButton.setGeometry(QtCore.QRect(150, 280, 191, 111))
        self.AudioButton.setObjectName("AudioButton")
        self.TextButton = QtWidgets.QPushButton(self.centralwidget)
        self.TextButton.setGeometry(QtCore.QRect(420, 280, 191, 111))
        self.TextButton.setObjectName("TextButton")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(210, 49, 321, 31))
        self.Title.setObjectName("Title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 20))
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
        self.ImagrButton.setText(_translate("MainWindow", "IMAGE DATASET"))
        self.StructuredButton.setText(_translate("MainWindow", "STRUCTURED DATASET"))
        self.AudioButton.setText(_translate("MainWindow", "AUDIO DATASET"))
        self.TextButton.setText(_translate("MainWindow", "TEXT DATASET"))
        self.Title.setText(_translate("MainWindow", "PLEASE CHOOSE ONE OF THE FOLLOWING OPTIONS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
