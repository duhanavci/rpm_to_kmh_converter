# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calisma.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo1 = QtWidgets.QComboBox(self.centralwidget)
        self.combo1.setGeometry(QtCore.QRect(110, 60, 211, 81))
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo2 = QtWidgets.QComboBox(self.centralwidget)
        self.combo2.setGeometry(QtCore.QRect(440, 60, 211, 81))
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("")
        self.combo2.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 200, 291, 141))
        self.label.setObjectName("label")
        self.hesapla_button = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla_button.setGeometry(QtCore.QRect(300, 360, 161, 71))
        self.hesapla_button.setObjectName("hesapla_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.hesapla_button.clicked.connect(self.pressed)

    def pressed(self):
        x = int(self.combo1.currentText())
        y = int(self.combo2.currentText())
        xor = (x and not y) or (not x and y)

        print(self.combo1.currentİnde())
        self.label.setText("x or y" + "  = " + str(xor))

        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo1.setItemText(0, _translate("MainWindow", "1"))
        self.combo1.setItemText(1, _translate("MainWindow", "0"))
        self.combo2.setItemText(0, _translate("MainWindow", "1"))
        self.combo2.setItemText(1, _translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "ve operatorü cevabı = "))
        self.hesapla_button.setText(_translate("MainWindow", "hesapla"))

    
           
         

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
