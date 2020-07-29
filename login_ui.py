from PyQt5.QtWidgets import QWidget, QPushButton,QLineEdit,QLabel,QVBoxLayout, QApplication, QSplashScreen, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class LoginUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(350, 45, 771, 681)

        vLayout = QVBoxLayout()
        self.vWidgetLayout = QVBoxLayout()

        container_widget = QWidget()

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(3)
        shadow.setColor(QColor("#010101"))
        shadow.setXOffset(3)
        shadow.setYOffset(3)

        username_label = QLabel("Username")
        username_label.setStyleSheet("border: none; font-size: 15px;")

        username_input = QLineEdit()
        username_input.setStyleSheet("background: none; border-top: none; border-left: none; border-right: none; border-bottom: 1px solid #010101; font-size: 14px;")
        username_input.setFixedWidth(200)

        password_label = QLabel("Password")
        password_label.setStyleSheet("border: none; font-size: 15px;")

        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setStyleSheet("border-top: none; border-left: none; border-right: none; border-bottom: 1px solid #010101; font-size: 14px;")
        password_input.setFixedWidth(200)

        self.login_btn = QPushButton("Login")
        self.login_btn.setStyleSheet("QPushButton { border-radius: 3px; font-size: 12px; }" "QPushButton:pressed { background: black; color: white; }")
        self.login_btn.setFixedWidth(50)
        self.login_btn.setFixedHeight(25)


        self._addWidgets(username_label, username_input, password_label, password_input, self.login_btn)

        container_widget.setStyleSheet("background: white; border: 0.5px solid #010101; border-radius: 10px; font-family: Lucida Console, Monaco, monospace; font-weight: bold;")
        container_widget.setLayout(self.vWidgetLayout)
        container_widget.setFixedHeight(200)
        container_widget.setFixedWidth(300)
        container_widget.setGraphicsEffect(shadow)
        self.vWidgetLayout.setSpacing(20)
        self.vWidgetLayout.setAlignment(Qt.AlignCenter)

        vLayout.addWidget(container_widget)
        vLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(vLayout)



    def _addWidgets(self, *widgets):
        for widget in widgets:
            self.vWidgetLayout.addWidget(widget, alignment=Qt.AlignHCenter)