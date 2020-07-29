from PyQt5.QtWidgets import QListWidget, QTabWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit, QComboBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class HomeTabUI(QTabWidget):

    def __init__(self, HomeTab):
        super().__init__()

        parent_horizontal_layout = QHBoxLayout(HomeTab)

        menu_vlayout = QVBoxLayout()
        frames_parent_vlayout = QVBoxLayout()

        frames_container = QFrame()
        frames_container.setLayout(frames_parent_vlayout)

        # Create scrollArea widget inside centralwidget
        self.scrollArea = QtWidgets.QScrollArea(frames_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())

        # Set size policy for scrollArea widget
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(767, 620))
        self.scrollArea.setMaximumSize(QtCore.QSize(767, 620))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")

        # Create scrollAreaWidgetContents widget
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -176, 771, 900))

        # Create size policy for scrollAreaWidgetContents
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())

        # Set scrollAreaWidgetContents size policy
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(771, 900))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(771, 900))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        menu_frame = QFrame()
        menu_frame.setFixedWidth(130)

        self.home_btn = QPushButton("Home")
        self.home_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.home_btn.clicked.connect(self.showHome)

        self.register_btn = QPushButton("Registration")
        self.register_btn.setStyleSheet(
            "QPushButton { background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold; }" "QPushButton:pressed { background: #f6c90e; }")

        self.member_profiles_btn = QPushButton("Member Profiles")
        self.member_profiles_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        #self.member_profiles_btn.clicked.connect(self.showMemberProfiles)

        self.units_btn = QPushButton("Units")
        self.units_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.clicked.connect(self.showUnits)

        self.files_btn = QPushButton("Files")
        self.files_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.clicked.connect(self.showFiles)

        self.accounts_btn = QPushButton("Accounts")
        self.accounts_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.clicked.connect(self.showAccounts)

        self.share_capital_btn = QPushButton("Share Capital")
        self.share_capital_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.clicked.connect(self.showShareCapital)

        menu_vlayout.addWidget(self.home_btn)
        menu_vlayout.addWidget(self.units_btn)
        menu_vlayout.addWidget(self.files_btn)
        menu_vlayout.addWidget(self.accounts_btn)
        menu_vlayout.addWidget(self.share_capital_btn)
        menu_vlayout.addWidget(self.register_btn)
        menu_vlayout.addWidget(self.member_profiles_btn)

        v_layout1 = QVBoxLayout()
        toolbar_Hlayout = QHBoxLayout()
        toolbar_Hlayout.setSpacing(0)
        toolbar_Hlayout.addStretch()
        toolbar_Hlayout.setContentsMargins(2, 1, 2, 1)
        sortby_label = QLabel("Sort by:")
        sortby_label.setStyleSheet("background: #e8e4e1; color: #1b1b2f; border: none; font-family: Verdana, Geneva, sans-serif; padding-left: 0.5px;")

        self.comboBox = QComboBox()
        self.comboBox.setStyleSheet("background: white; border: none; font-family: Verdana, Geneva, sans-serif;")
        self.comboBox.addItem("Date")
        self.comboBox.addItem("Name")
        self.comboBox.setFixedWidth(57)

        search_label = QLabel("Search:")
        search_label.setStyleSheet("background: #e8e4e1; color: #1b1b2f; border: none; font-family: Verdana, Geneva, sans-serif; padding-left: 0.5px;")
        self.search_input = QLineEdit()
        self.search_input.setStyleSheet("background: white; border: none; font-family: Verdana, Geneva, sans-serif;")
        self.search_input.setFixedWidth(150)
        toolbar_Hlayout.addWidget(search_label)
        toolbar_Hlayout.addWidget(self.search_input)
        toolbar_Hlayout.insertWidget(0, self.comboBox)
        toolbar_Hlayout.insertWidget(0, sortby_label)

        self.listwidget = QListWidget()
        self.listwidget.setSpacing(1)
        #self.listwidget.setStyleSheet("QListWidget {font-family: Verdana, Geneva, sans-serif;}" "QListWidget.item:hover {color: white; background: blue;}")
        self.listwidget.setFixedHeight(600)

        label_Hlayout = QHBoxLayout()
        label_Hlayout.setSpacing(1)
        label_Hlayout.setContentsMargins(2, 1, 2, 0)
        no_label, name_label, address_label, date_label = QLabel('No'), QLabel('Name'), QLabel('Address'), QLabel('Date')
        no_label.setStyleSheet("background: white; color: blue; font-family: Verdana, Geneva, sans-serif; font-weight: bold; padding-top: 3px; padding-bottom: 3px; border-left: none; border-right: none; border-top: none;")
        name_label.setStyleSheet("background: white; color: blue; font-family: Verdana, Geneva, sans-serif; font-weight: bold; padding-left: 65px; padding-right: 60px; padding-top: 3px; padding-bottom: 3px; border-left: none; border-right: none; border-top: none;")
        address_label.setStyleSheet("background: white; color: blue; font-family: Verdana, Geneva, sans-serif; font-weight: bold; padding-left: 145px; padding-right: 150px; padding-top: 3px; padding-bottom: 3px; border-left: none; border-right: none; border-top: none;")
        date_label.setStyleSheet("background: white; color: blue; font-family: Verdana, Geneva, sans-serif; font-weight: bold; border-left: none; padding-top: 3px; padding-bottom: 3px; padding-right: 15px;  padding-left: 11px; border-right: none; border-top: none;")
        label_Hlayout.addWidget(no_label, 0)
        label_Hlayout.addWidget(name_label, 1)
        label_Hlayout.addWidget(address_label, 2)
        label_Hlayout.addWidget(date_label, 0)
        v_layout1.addLayout(toolbar_Hlayout)
        v_layout1.addLayout(label_Hlayout)
        v_layout1.addWidget(self.listwidget)
        v_layout1.setContentsMargins(0, 0, 0, 0)
        v_layout1.setSpacing(0)

        v_layout2 = QVBoxLayout()
        units_label = QLabel("Units")
        units_label.setStyleSheet("border: 1px solid red;")
        v_layout2.addWidget(units_label)

        v_layout3 = QVBoxLayout()
        files_label = QLabel("Files")
        files_label.setStyleSheet("border: 1px solid red;")
        v_layout3.addWidget(files_label)

        v_layout4 = QVBoxLayout()
        accounts_label = QLabel("Accounts")
        accounts_label.setStyleSheet("border: 1px solid red;")
        v_layout4.addWidget(accounts_label)

        v_layout5 = QVBoxLayout()
        share_capitals_label = QLabel("Share Capitals")
        share_capitals_label.setStyleSheet("border: 1px solid red;")
        v_layout5.addWidget(share_capitals_label)

        self.frame1 = QFrame()
        self.frame1.setLayout(v_layout1)
        self.frame2 = QFrame()
        self.frame2.setStyleSheet("border: 1px solid blue;")
        self.frame2.setLayout(v_layout2)
        self.frame3 = QFrame()
        self.frame3.setStyleSheet("border: 1px solid blue;")
        self.frame3.setLayout(v_layout3)
        self.frame4 = QFrame()
        self.frame4.setStyleSheet("border: 1px solid blue;")
        self.frame4.setLayout(v_layout4)
        self.frame5 = QFrame()
        self.frame5.setStyleSheet("border: 1px solid blue;")
        self.frame5.setLayout(v_layout5)

        frames_parent_vlayout.addWidget(self.frame1)
        frames_parent_vlayout.addWidget(self.frame2)
        frames_parent_vlayout.addWidget(self.frame3)
        frames_parent_vlayout.addWidget(self.frame4)
        frames_parent_vlayout.addWidget(self.frame5)

        self.showHome()

        menu_frame.setLayout(menu_vlayout)
        menu_frame.setStyleSheet("background: #252525;")
        menu_vlayout.setContentsMargins(5, 5, 5, 0)
        parent_horizontal_layout.addWidget(menu_frame)
        parent_horizontal_layout.addWidget(frames_container)
        frames_parent_vlayout.addStretch()
        frames_parent_vlayout.setContentsMargins(0, 0, 0, 0)
        frames_container.setContentsMargins(0, 0, 0, 0)
        frames_container.setStyleSheet("background: #978d58;")
        menu_vlayout.addStretch()
        parent_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        parent_horizontal_layout.setSpacing(0)
        #parent_horizontal_layout.addStretch()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


    def showHomeWindow(self):
        self.show()

    def showHome(self):
        self.home_btn.setStyleSheet(
            "background: #f6c90e; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.register_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.member_profiles_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")

        self.frame2.hide()
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame1.show()

    def showRegister(self):
        self.register_btn.setStyleSheet(
            "background: #f6c90e; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.member_profiles_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")

        self.frame2.hide()
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame1.show()

    def showMemberProfiles(self):
        self.home_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.member_profiles_btn.setStyleSheet(
            "background: #f6c90e; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")

        self.frame1.hide()
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame2.show()

    def showUnits(self):
        self.home_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.member_profiles_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.setStyleSheet(
            "background: #f6c90e; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")

        self.frame1.hide()
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame2.show()

    def showFiles(self):
        self.home_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.member_profiles_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.setStyleSheet(
            "background: #f6c90e; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")

        self.frame1.hide()
        self.frame2.hide()
        self.frame4.hide()
        self.frame5.hide()
        self.frame3.show()

    def showAccounts(self):
        self.home_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.member_profiles_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.setStyleSheet(
            "background: #f6c90e; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")

        self.frame1.hide()
        self.frame2.hide()
        self.frame3.hide()
        self.frame5.hide()
        self.frame4.show()

    def showShareCapital(self):
        self.home_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.member_profiles_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.units_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.files_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.accounts_btn.setStyleSheet(
            "background: #14ffec; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        self.share_capital_btn.setStyleSheet(
            "background: #f6c90e; font-family: Verdana, Geneva, sans-serif; font-weight: bold;")
        
        self.frame1.hide()
        self.frame2.hide()
        self.frame3.hide()
        self.frame4.hide()
        self.frame5.show()