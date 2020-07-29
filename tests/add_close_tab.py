import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt


class TabExample(QMainWindow):
    def __init__(self):
        super(TabExample, self).__init__()
        self.setWindowTitle("Tab example")

        # Create widgets
        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Label's to fill widget
        self.label1 = QtWidgets.QLabel("Tab 1")
        self.label1.setTextFormat(Qt.RichText)
        self.label2 = QtWidgets.QLabel("Tab 2")

        # Adding tab's
        self.tab_widget.addTab(self.label1, "Tab 1")
        self.tab_widget.addTab(self.label2, "Tab 2")

        # Tab button's
        self.right = self.tab_widget.tabBar().RightSide
        self.tab_widget.tabBar().setTabButton(0, self.right, TabButtonWidget())
        self.tab_widget.tabBar().setTabButton(1, self.right, TabButtonWidget())
        self.tab_widget.setContentsMargins(0, 0, 0, 0)

        # Tab settings
        self.tab_widget.tabBar().setMovable(True)

        self.show()


class TabButtonWidget(QtWidgets.QWidget):
    def __init__(self):
        super(TabButtonWidget, self).__init__()
        # Create buttons

        self.button_remove = QtWidgets.QPushButton(u"\u2715")
        self.button_remove.setStyleSheet("QPushButton {background-color: #ffffff; color: #252525;}" "QPushButton:pressed { background: #252525; color: #ffffff; }")

        # Set button size
        self.button_remove.setFixedSize(16, 16)

        # Create layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Add button's to layout
        self.layout.addWidget(self.button_remove)

        # Use layout in widget
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TabExample()
    sys.exit(app.exec_())