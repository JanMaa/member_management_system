from PyQt5 import QtWidgets

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