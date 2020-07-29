def main():
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = Test_Dialog()
    window.show()
    exit(app.exec())

class Ui_Dialog(object) :
    def setupUi (self, Dialog) :
        from PyQt5 import QtCore, QtWidgets

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 181, 121))
        self.tab = QtWidgets.QWidget()
        self.pushButton_remove = QtWidgets.QPushButton("remove", self.tab)
        self.pushButton_remove.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton_add = QtWidgets.QPushButton("add", self.tab)
        self.pushButton_add.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.tabWidget.addTab(self.tab, "Tab 1")
        self.tab_2 = QtWidgets.QWidget()
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.tabWidget.addTab(self.tab_2, "Tab 2")  # remove this for approach #1

from PyQt5.QtWidgets import QDialog
class Test_Dialog(QDialog, Ui_Dialog) :
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.hideTab()
        self.pushButton_remove.clicked.connect(self.hideTab)
        self.pushButton_add.clicked.connect(self.showTab)
    def hideTab(self):
        if self.tabWidget.widget(1):
            self.save = self.tabWidget.widget(1)  # save it for later
            self.tabWidget.removeTab(1)
    def showTab (self) :
        self.tabWidget.insertTab(1, self.save, 'Tab 2') # restore
        self.tabWidget.setCurrentIndex(1)

main()