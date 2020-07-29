import sys
from logic import MyUi
from login_ui import LoginUI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtCore import Qt, QTimer

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OFWTMC MANAGEMENT SYSTEM")
        self.setGeometry(350, 45, 771, 681)
        self.login_ui = LoginUI()
        self.my_ui = MyUi()
        self.login_ui.login_btn.clicked.connect(self.showMainWindow)

    def showSplashScreen(self):
        self.pix = QPixmap("img/ofwtmc_splash_screen.PNG")
        self.splash = QSplashScreen(self.pix, Qt.WindowStaysOnTopHint)
        self.splash.show()

    def showMainWindow(self):
        self.setCentralWidget(self.my_ui)
        self.show()

    def showLoginUI(self):
        self.splash.close()
        self.setCentralWidget(self.login_ui)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)

    #create a new object
    main_ui = MainUI()
    main_ui.showSplashScreen()
    QTimer.singleShot(3000, main_ui.showLoginUI)
    sys.exit(app.exec_())

if __name__ == "__main__": main()