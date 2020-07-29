from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setMouseTracking(True)

        hlayout = QHBoxLayout()
        self.label = QLabel()
        self.label.setStyleSheet("background: green; color: yellow; border: red 1px solid red;")
        self.label.setText("Hello World!")
        hlayout.addWidget(self.label)
        hlayout.addStretch()
        self.setLayout(hlayout)

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.label.move(event.globalPos().x(), 0)
            print(event.globalPos().x(), event.globalPos().y())

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 150, 100, 100)
    window.show()
    sys.exit(app.exec_())