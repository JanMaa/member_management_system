# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(350, 45, 771, 671)

        # Creating size policy for MainWindow
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        # Set size policy for Mainwindow
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(771, 676))
        MainWindow.setMaximumSize(QtCore.QSize(771, 676))

        # Creat centralwidget and its size policy
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        # Set size policy for centralwidget
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(771, 676))
        self.centralwidget.setMaximumSize(QtCore.QSize(771, 676))
        self.centralwidget.setObjectName("centralwidget")

        # Create verticalLayout for centralwidget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create scrollArea widget inside centralwidget
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())

        # Set size policy for scrollArea widget
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(771, 676))
        self.scrollArea.setMaximumSize(QtCore.QSize(771, 676))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")

        # Create scrollAreaWidgetContents widget
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -176, 771, 850))

        # Create size policy for scrollAreaWidgetContents
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())

        # Set scrollAreaWidgetContents size policy
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(771, 850))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(771, 850))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Create verticalLayout_2 for scrollAreaWidgetContents
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Create widget1 inside scrollAreaWidgetContents
        self.widget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)

        # Create size policy for widget1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())

        # Set size policy for widget1
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMaximumSize(QtCore.QSize(753, 40))
        self.widget1.setAutoFillBackground(False)
        self.widget1.setStyleSheet("border-color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.widget1.setObjectName("widget1")

        # Create horizontalLayout_3 for widget1
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(25, 8, 10, 8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Create formTitle inside widget1
        self.formTitle = QtWidgets.QLabel(self.widget1)
        self.formTitle.setMinimumSize(QtCore.QSize(0, 0))
        self.formTitle.setMaximumSize(QtCore.QSize(260, 40))
        self.formTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formTitle.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.formTitle.setScaledContents(False)
        self.formTitle.setIndent(0)
        self.formTitle.setObjectName("formTitle")

        # Add formTitle inside widget1 with layout horizontalLayout_3
        self.horizontalLayout_3.addWidget(self.formTitle)

        # Add widget1 inside scrollAreaWidgetContents with layout verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget1)

        # Create widgets2 inside scrollAreaWidgetContents
        self.widget2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget2.setMaximumSize(QtCore.QSize(753, 197))
        self.widget2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget2.setObjectName("widget2")

        # Create horizontalLayout_2 for widget2
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Create logoWidget inside widget2
        self.logoWidget = QtWidgets.QWidget(self.widget2)
        self.logoWidget.setMaximumSize(QtCore.QSize(192, 192))
        self.logoWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.logoWidget.setObjectName("logoWidget")

        # Create logoImage inside logoWidget
        self.logoImage = QtWidgets.QLabel(self.logoWidget)
        self.logoImage.setGeometry(QtCore.QRect(10, 10, 171, 161))
        self.logoImage.setText("")
        self.logoImage.setPixmap(QtGui.QPixmap("../../Downloads/OFWTSMPC (1).png"))
        self.logoImage.setScaledContents(True)
        self.logoImage.setObjectName("logoImage")

        # Add logo widget to widget2 with layout horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.logoWidget)

        # Create headingWidget inside widget2
        self.headingWidget = QtWidgets.QWidget(self.widget2)
        self.headingWidget.setObjectName("headingWidget")

        # Create headingLabel inside headingWidget
        self.headingLabel = QtWidgets.QLabel(self.headingWidget)
        self.headingLabel.setGeometry(QtCore.QRect(10, 10, 311, 161))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")

        # Add headingWidget inside widget2 with layout horizontalLayout2
        self.horizontalLayout_2.addWidget(self.headingWidget)

        # Create uploadImgWidget inside widget2
        self.uploadImgWidget = QtWidgets.QWidget(self.widget2)
        self.uploadImgWidget.setMaximumSize(QtCore.QSize(192, 192))
        self.uploadImgWidget.setObjectName("uploadImgWidget")

        # Create imgDefault inside uploadImgWidget
        self.imgDefault = QtWidgets.QLabel(self.uploadImgWidget)
        self.imgDefault.setGeometry(QtCore.QRect(0, 0, 192, 192))
        self.imgDefault.setText("")
        self.imgDefault.setPixmap(QtGui.QPixmap("img/default_avatar.png"))
        self.imgDefault.setScaledContents(True)
        self.imgDefault.setObjectName("imgDefault")

        # Add uploadImgWidget inside widget2 with layout horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.uploadImgWidget)

        # Add widget2 inside scrollAreaWidgetContents with layout verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget2)

        # Create widget3 inside scrollAreWidgetContents
        self.widget3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)

        # Create size policy for widget3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget3.sizePolicy().hasHeightForWidth())

        # Set size policy for widget3
        self.widget3.setSizePolicy(sizePolicy)
        self.widget3.setMinimumSize(QtCore.QSize(753, 608))
        self.widget3.setMaximumSize(QtCore.QSize(753, 608))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.widget3.setFont(font)
        self.widget3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget3.setObjectName("widget3")

        # Create ofwAbroadLabel inside widget3
        self.ofwAbroadLabel = QtWidgets.QLabel(self.widget3)
        self.ofwAbroadLabel.setGeometry(QtCore.QRect(20, 30, 75, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ofwAbroadLabel.setFont(font)
        self.ofwAbroadLabel.setObjectName("ofwAbroadLabel")

        # Create ofwNameInput inside widget3
        self.ofwNameInput = QtWidgets.QLineEdit(self.widget3)
        self.ofwNameInput.setGeometry(QtCore.QRect(100, 50, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ofwNameInput.setFont(font)
        self.ofwNameInput.setObjectName("ofwNameInput")

        # Create ofwNameLabel inside widget3
        self.ofwNameLabel = QtWidgets.QLabel(self.widget3)
        self.ofwNameLabel.setGeometry(QtCore.QRect(50, 50, 38, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ofwNameLabel.setFont(font)
        self.ofwNameLabel.setObjectName("ofwNameLabel")

        # Create ofwAdressInput inside widget3
        self.ofwAddressInput = QtWidgets.QLineEdit(self.widget3)
        self.ofwAddressInput.setGeometry(QtCore.QRect(440, 50, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ofwAddressInput.setFont(font)
        self.ofwAddressInput.setObjectName("ofwAddressInput")

        # Create ofwAddressLabel inside widget3
        self.ofwAddressLabel = QtWidgets.QLabel(self.widget3)
        self.ofwAddressLabel.setGeometry(QtCore.QRect(385, 50, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ofwAddressLabel.setFont(font)
        self.ofwAddressLabel.setObjectName("ofwAddressLabel")

        # Create dateLabel inside widget3
        self.dateLabel = QtWidgets.QLabel(self.widget3)
        self.dateLabel.setGeometry(QtCore.QRect(403, 17, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")

        # Create beneficiariesLabel inside widget3
        self.beneficiariesLabel = QtWidgets.QLabel(self.widget3)
        self.beneficiariesLabel.setGeometry(QtCore.QRect(20, 70, 82, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.beneficiariesLabel.setFont(font)
        self.beneficiariesLabel.setObjectName("beneficiariesLabel")

        # Create beneficiaryNameLabel inside widget3
        self.beneficiaryNameLabel = QtWidgets.QLabel(self.widget3)
        self.beneficiaryNameLabel.setGeometry(QtCore.QRect(50, 90, 38, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.beneficiaryNameLabel.setFont(font)
        self.beneficiaryNameLabel.setObjectName("beneficiaryNameLabel")

        # Create beneficiaryNameInput inside widget3
        self.beneficiaryNameInput = QtWidgets.QLineEdit(self.widget3)
        self.beneficiaryNameInput.setGeometry(QtCore.QRect(100, 90, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.beneficiaryNameInput.setFont(font)
        self.beneficiaryNameInput.setText("")
        self.beneficiaryNameInput.setObjectName("beneficiaryNameInput")

        # Create beneficiaryAddressLabel inside widget3
        self.beneficiaryAddressLabel = QtWidgets.QLabel(self.widget3)
        self.beneficiaryAddressLabel.setGeometry(QtCore.QRect(384, 90, 53, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.beneficiaryAddressLabel.setFont(font)
        self.beneficiaryAddressLabel.setObjectName("beneficiaryAddressLabel")

        # Create beneficiaryAddressInput inside widget3
        self.beneficiaryAddresInput = QtWidgets.QLineEdit(self.widget3)
        self.beneficiaryAddresInput.setGeometry(QtCore.QRect(440, 90, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.beneficiaryAddresInput.setFont(font)
        self.beneficiaryAddresInput.setObjectName("beneficiaryAddresInput")

        # Create placeOfBirthInput inside widget3
        self.placeOfBirthInput = QtWidgets.QLineEdit(self.widget3)
        self.placeOfBirthInput.setGeometry(QtCore.QRect(100, 120, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.placeOfBirthInput.setFont(font)
        self.placeOfBirthInput.setObjectName("placeOfBirthInput")

        # Create placeOfBirthLabel inside widget3
        self.placeOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.placeOfBirthLabel.setGeometry(QtCore.QRect(15, 120, 80, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.placeOfBirthLabel.setFont(font)
        self.placeOfBirthLabel.setObjectName("placeOfBirthLabel")

        # Create placeOfBirthLabel inside widget3
        self.provincialAddressLabel = QtWidgets.QLabel(self.widget3)
        self.provincialAddressLabel.setGeometry(QtCore.QRect(367, 120, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.provincialAddressLabel.setFont(font)
        self.provincialAddressLabel.setObjectName("provincialAddressLabel")

        # Create religionLabel inside widget3
        self.religionLabel = QtWidgets.QLabel(self.widget3)
        self.religionLabel.setGeometry(QtCore.QRect(426, 150, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.religionLabel.setFont(font)
        self.religionLabel.setObjectName("religionLabel")

        # Create provincialAddressInput inside widget3
        self.provincialAddressInput = QtWidgets.QLineEdit(self.widget3)
        self.provincialAddressInput.setGeometry(QtCore.QRect(480, 120, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.provincialAddressInput.setFont(font)
        self.provincialAddressInput.setObjectName("provincialAddressInput")

        # Create dateOfBirthLabel inside widget3
        self.dateOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.dateOfBirthLabel.setGeometry(QtCore.QRect(19, 150, 79, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dateOfBirthLabel.setFont(font)
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")

        # Create religionInput inside widget3
        self.religionInput = QtWidgets.QLineEdit(self.widget3)
        self.religionInput.setGeometry(QtCore.QRect(480, 150, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.religionInput.setFont(font)
        self.religionInput.setObjectName("religionInput")

        # Create contactInput inside widget3
        self.contactInput = QtWidgets.QLineEdit(self.widget3)
        self.contactInput.setGeometry(QtCore.QRect(100, 180, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.contactInput.setFont(font)
        self.contactInput.setObjectName("contactInput")

        # Create contactLabel inside widget3
        self.contactLabel = QtWidgets.QLabel(self.widget3)
        self.contactLabel.setGeometry(QtCore.QRect(23, 180, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.contactLabel.setFont(font)
        self.contactLabel.setObjectName("contactLabel")

        # Create emailAddLabel inside widget3
        self.emailAddLabel = QtWidgets.QLabel(self.widget3)
        self.emailAddLabel.setGeometry(QtCore.QRect(222, 180, 33, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.emailAddLabel.setFont(font)
        self.emailAddLabel.setObjectName("emailAddLabel")

        # Create emailAddInput inside widget3
        self.emailAddInput = QtWidgets.QLineEdit(self.widget3)
        self.emailAddInput.setGeometry(QtCore.QRect(260, 180, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.emailAddInput.setFont(font)
        self.emailAddInput.setObjectName("emailAddInput")

        # Create ageLabel inside widget3
        self.ageLabel = QtWidgets.QLabel(self.widget3)
        self.ageLabel.setGeometry(QtCore.QRect(175, 150, 27, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ageLabel.setFont(font)
        self.ageLabel.setObjectName("ageLabel")

        # Create ageInput inside widget3
        self.ageInput = QtWidgets.QLineEdit(self.widget3)
        self.ageInput.setGeometry(QtCore.QRect(203, 150, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ageInput.setFont(font)
        self.ageInput.setText("")
        self.ageInput.setObjectName("ageInput")

        # Create sexLabel inside widget3
        self.sexLabel = QtWidgets.QLabel(self.widget3)
        self.sexLabel.setGeometry(QtCore.QRect(227, 150, 27, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sexLabel.setFont(font)
        self.sexLabel.setObjectName("sexLabel")

        # Create maleRBtn inside widget3
        self.maleRBtn = QtWidgets.QRadioButton(self.widget3)
        self.maleRBtn.setGeometry(QtCore.QRect(255, 150, 50, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.maleRBtn.setFont(font)
        self.maleRBtn.setObjectName("maleRBtn")

        # Create femaleRBtn inside widget3
        self.femaleRBtn = QtWidgets.QRadioButton(self.widget3)
        self.femaleRBtn.setGeometry(QtCore.QRect(306, 150, 61, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.femaleRBtn.setFont(font)
        self.femaleRBtn.setObjectName("femaleRBtn")

        # Create civilStatusLabel inside widget3
        self.civilStatusLabel = QtWidgets.QLabel(self.widget3)
        self.civilStatusLabel.setGeometry(QtCore.QRect(219, 210, 66, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.civilStatusLabel.setFont(font)
        self.civilStatusLabel.setObjectName("civilStatusLabel")

        # Create civilStatusInput inside widget3
        self.civilStatusInput = QtWidgets.QLineEdit(self.widget3)
        self.civilStatusInput.setGeometry(QtCore.QRect(290, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.civilStatusInput.setFont(font)
        self.civilStatusInput.setText("")
        self.civilStatusInput.setObjectName("civilStatusInput")

        # Create citizenshipLabel inside widget3
        self.citizenshipLabel = QtWidgets.QLabel(self.widget3)
        self.citizenshipLabel.setGeometry(QtCore.QRect(30, 210, 67, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.citizenshipLabel.setFont(font)
        self.citizenshipLabel.setObjectName("citizenshipLabel")

        # Create citizenshipInput inside widget3
        self.citizenshipInput = QtWidgets.QLineEdit(self.widget3)
        self.citizenshipInput.setGeometry(QtCore.QRect(100, 210, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.citizenshipInput.setFont(font)
        self.citizenshipInput.setObjectName("citizenshipInput")

        # Create tinLabel inside widget3
        self.tinLabel = QtWidgets.QLabel(self.widget3)
        self.tinLabel.setGeometry(QtCore.QRect(430, 180, 45, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tinLabel.setFont(font)
        self.tinLabel.setObjectName("tinLabel")

        # Create tinInput inside widget3
        self.tinInput = QtWidgets.QLineEdit(self.widget3)
        self.tinInput.setGeometry(QtCore.QRect(480, 180, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.tinInput.setFont(font)
        self.tinInput.setObjectName("tinInput")

        # Create sssLabel inside widget3
        self.sssLabel = QtWidgets.QLabel(self.widget3)
        self.sssLabel.setGeometry(QtCore.QRect(430, 210, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sssLabel.setFont(font)
        self.sssLabel.setObjectName("sssLabel")

        # Create sssInput inside widget3
        self.sssInput = QtWidgets.QLineEdit(self.widget3)
        self.sssInput.setGeometry(QtCore.QRect(480, 210, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.sssInput.setFont(font)
        self.sssInput.setObjectName("sssInput")

        # Create hwLabel inside widget3
        self.hwLabel = QtWidgets.QLabel(self.widget3)
        self.hwLabel.setGeometry(QtCore.QRect(10, 240, 96, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hwLabel.setFont(font)
        self.hwLabel.setObjectName("hwLabel")

        # Create hwNameLabel inside widget3
        self.hwNameLabel = QtWidgets.QLabel(self.widget3)
        self.hwNameLabel.setGeometry(QtCore.QRect(60, 260, 37, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hwNameLabel.setFont(font)
        self.hwNameLabel.setObjectName("hwNameLabel")

        # Create hwNameInput inside widget3
        self.hwNameInput = QtWidgets.QLineEdit(self.widget3)
        self.hwNameInput.setGeometry(QtCore.QRect(100, 260, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hwNameInput.setFont(font)
        self.hwNameInput.setObjectName("hwNameInput")

        # Create hwPlaceOFBirthLabel inside widget3
        self.hwPlaceOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.hwPlaceOfBirthLabel.setGeometry(QtCore.QRect(398, 260, 80, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hwPlaceOfBirthLabel.setFont(font)
        self.hwPlaceOfBirthLabel.setObjectName("hwPlaceOfBirthLabel")

        # Create hwPlaceOfBirthInput inside widget3
        self.hwPllaceOfBirthInput = QtWidgets.QLineEdit(self.widget3)
        self.hwPllaceOfBirthInput.setGeometry(QtCore.QRect(480, 260, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hwPllaceOfBirthInput.setFont(font)
        self.hwPllaceOfBirthInput.setObjectName("hwPlaceOfBirthInput")

        # Create hwOccupationLabel inside widget3
        self.hwOccupationLabel = QtWidgets.QLabel(self.widget3)
        self.hwOccupationLabel.setGeometry(QtCore.QRect(409, 290, 69, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hwOccupationLabel.setFont(font)
        self.hwOccupationLabel.setObjectName("hwOccupationLabel")

        # Create hwOccupationInput inside widget3
        self.hwOccupationInput = QtWidgets.QLineEdit(self.widget3)
        self.hwOccupationInput.setGeometry(QtCore.QRect(480, 290, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hwOccupationInput.setFont(font)
        self.hwOccupationInput.setObjectName("hwOccupationInput")

        # Create hwDateOfBirthLabel inside widget3
        self.hwDateOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.hwDateOfBirthLabel.setGeometry(QtCore.QRect(23, 290, 76, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hwDateOfBirthLabel.setFont(font)
        self.hwDateOfBirthLabel.setObjectName("hwDateOfBirthLabel")

        # Create hwAgeLabel inside widget3
        self.hwAgeLabel = QtWidgets.QLabel(self.widget3)
        self.hwAgeLabel.setGeometry(QtCore.QRect(185, 290, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hwAgeLabel.setFont(font)
        self.hwAgeLabel.setObjectName("hwAgeLabel")

        # Create hwAgeInput inside widget3
        self.hwAgeInput = QtWidgets.QLineEdit(self.widget3)
        self.hwAgeInput.setGeometry(QtCore.QRect(220, 290, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hwAgeInput.setFont(font)
        self.hwAgeInput.setObjectName("hwAgeInput")

        # Create childrenLabel inside widget3
        self.childrenLabel = QtWidgets.QLabel(self.widget3)
        self.childrenLabel.setGeometry(QtCore.QRect(50, 329, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.childrenLabel.setFont(font)
        self.childrenLabel.setObjectName("childrenLabel")

        # Create chNameLabel inside widget3
        self.chNameLabel = QtWidgets.QLabel(self.widget3)
        self.chNameLabel.setGeometry(QtCore.QRect(60, 350, 37, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chNameLabel.setFont(font)
        self.chNameLabel.setObjectName("chNameLabel")

        # Create chNameInput inside widget3
        self.chNameInput = QtWidgets.QLineEdit(self.widget3)
        self.chNameInput.setGeometry(QtCore.QRect(100, 350, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.chNameInput.setFont(font)
        self.chNameInput.setObjectName("chNameInput")

        # Create emDateLabel inside widget3
        self.empDateLabel = QtWidgets.QLabel(self.widget3)
        self.empDateLabel.setGeometry(QtCore.QRect(387, 440, 92, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.empDateLabel.setFont(font)
        self.empDateLabel.setObjectName("empDateLabel")

        # Create chAdressInput inside widget3
        self.chAdressInput = QtWidgets.QLineEdit(self.widget3)
        self.chAdressInput.setGeometry(QtCore.QRect(390, 350, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.chAdressInput.setFont(font)
        self.chAdressInput.setText("")
        self.chAdressInput.setObjectName("chAdressInput")

        # Create chAgeLabel inside widget3
        self.chAgeLabel = QtWidgets.QLabel(self.widget3)
        self.chAgeLabel.setGeometry(QtCore.QRect(640, 350, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chAgeLabel.setFont(font)
        self.chAgeLabel.setObjectName("chAgeLabel")

        # Create chAgeInput inside widget3
        self.chAgeInput = QtWidgets.QLineEdit(self.widget3)
        self.chAgeInput.setGeometry(QtCore.QRect(670, 350, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.chAgeInput.setFont(font)
        self.chAgeInput.setObjectName("chAgeInput")

        # Create chAddBtn inside widget3
        self.chAddBtn = QtWidgets.QPushButton(self.widget3)
        self.chAddBtn.setGeometry(QtCore.QRect(700, 350, 31, 21))
        self.chAddBtn.setObjectName("chAddBtn")

        # Create empInfoLabel inside widget3
        self.empInfoLabel = QtWidgets.QLabel(self.widget3)
        self.empInfoLabel.setGeometry(QtCore.QRect(11, 390, 148, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.empInfoLabel.setFont(font)
        self.empInfoLabel.setObjectName("empInfoLabel")

        # Create empNameLabel inside widget3
        self.empNameLabel = QtWidgets.QLabel(self.widget3)
        self.empNameLabel.setGeometry(QtCore.QRect(58, 410, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.empNameLabel.setFont(font)
        self.empNameLabel.setObjectName("empNameLabel")

        # Create empNameInput inside widget3
        self.empNameInput = QtWidgets.QLineEdit(self.widget3)
        self.empNameInput.setGeometry(QtCore.QRect(100, 410, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.empNameInput.setFont(font)
        self.empNameInput.setObjectName("empNameInput")

        # Create empPositionLabel inside widget3
        self.empPositionLabel = QtWidgets.QLabel(self.widget3)
        self.empPositionLabel.setGeometry(QtCore.QRect(45, 440, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.empPositionLabel.setFont(font)
        self.empPositionLabel.setObjectName("empPositionLabel")

        # Create empPositionInput inside widget3
        self.empPositionInput = QtWidgets.QLineEdit(self.widget3)
        self.empPositionInput.setGeometry(QtCore.QRect(100, 440, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.empPositionInput.setFont(font)
        self.empPositionInput.setText("")
        self.empPositionInput.setObjectName("empPositionInput")

        # Create incaseLabel inside widget3
        self.incaseLabel = QtWidgets.QLabel(self.widget3)
        self.incaseLabel.setGeometry(QtCore.QRect(13, 480, 170, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.incaseLabel.setFont(font)
        self.incaseLabel.setObjectName("incaseLabel")

        # Create incaseNameLabel inside widget3
        self.incaseNameLabel = QtWidgets.QLabel(self.widget3)
        self.incaseNameLabel.setGeometry(QtCore.QRect(60, 505, 38, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.incaseNameLabel.setFont(font)
        self.incaseNameLabel.setObjectName("incaseNameLabel")

        # Create incaseNameInput inside widget3
        self.incaseNameInput = QtWidgets.QLineEdit(self.widget3)
        self.incaseNameInput.setGeometry(QtCore.QRect(100, 505, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.incaseNameInput.setFont(font)
        self.incaseNameInput.setObjectName("incaseNameInput")

        # Create incaseAddressLabel inside widget3
        self.incaseAddressLabel = QtWidgets.QLabel(self.widget3)
        self.incaseAddressLabel.setGeometry(QtCore.QRect(46, 535, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.incaseAddressLabel.setFont(font)
        self.incaseAddressLabel.setObjectName("incaseAddressLabel")

        # Create incaseContactInput inside widget3
        self.incaseContactInput = QtWidgets.QLineEdit(self.widget3)
        self.incaseContactInput.setGeometry(QtCore.QRect(480, 505, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.incaseContactInput.setFont(font)
        self.incaseContactInput.setObjectName("incaseContactInput")

        # Create incaseAddressInput inside widget3
        self.incaseAdressInput = QtWidgets.QLineEdit(self.widget3)
        self.incaseAdressInput.setGeometry(QtCore.QRect(100, 535, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.incaseAdressInput.setFont(font)
        self.incaseAdressInput.setObjectName("incaseAdressInput")

        # Create incaseContactLabel inside widget3
        self.incaseContactLabel = QtWidgets.QLabel(self.widget3)
        self.incaseContactLabel.setGeometry(QtCore.QRect(410, 505, 70, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.incaseContactLabel.setFont(font)
        self.incaseContactLabel.setObjectName("incaseContactLabel")

        # Create chAdressLabel inside widget3
        self.chAddressLabel = QtWidgets.QLabel(self.widget3)
        self.chAddressLabel.setGeometry(QtCore.QRect(337, 350, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chAddressLabel.setFont(font)
        self.chAddressLabel.setObjectName("chAddressLabel")

        # Create empAdressInput inside widget3
        self.empAdressInput = QtWidgets.QLineEdit(self.widget3)
        self.empAdressInput.setGeometry(QtCore.QRect(480, 410, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.empAdressInput.setFont(font)
        self.empAdressInput.setText("")
        self.empAdressInput.setObjectName("empAdressInput")

        # Create empAdressLabel inside widget3
        self.empAddressLabel = QtWidgets.QLabel(self.widget3)
        self.empAddressLabel.setGeometry(QtCore.QRect(425, 410, 52, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.empAddressLabel.setFont(font)
        self.empAddressLabel.setObjectName("empAddressLabel")

        # Create dateInput inside widget3
        self.dateInput = QtWidgets.QDateEdit(self.widget3)
        self.dateInput.setGeometry(QtCore.QRect(440, 14, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.dateInput.setFont(font)
        self.dateInput.setObjectName("dateInput")

        # Create dateOfBirthInput inside widget3
        self.dateOfBirthInput = QtWidgets.QDateEdit(self.widget3)
        self.dateOfBirthInput.setGeometry(QtCore.QRect(100, 150, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.dateOfBirthInput.setFont(font)
        self.dateOfBirthInput.setObjectName("dateOfBirthInput")

        # Create hwDateOfBirthInput inside widget3
        self.hwDateOfBirthInput = QtWidgets.QDateEdit(self.widget3)
        self.hwDateOfBirthInput.setGeometry(QtCore.QRect(100, 290, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.hwDateOfBirthInput.setFont(font)
        self.hwDateOfBirthInput.setObjectName("hwDateOfBirthInput")

        # Create dateOfBirthInput inside widget3
        self.empDateInput = QtWidgets.QDateEdit(self.widget3)
        self.empDateInput.setGeometry(QtCore.QRect(480, 440, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.empDateInput.setFont(font)
        self.empDateInput.setObjectName("empDateInput")

        # Create fileSelectBtn inside widget3
        self.fileSelectBtn = QtWidgets.QToolButton(self.widget3)
        self.fileSelectBtn.setGeometry(QtCore.QRect(659, 14, 25, 19))
        self.fileSelectBtn.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.fileSelectBtn.setObjectName("fileSelectBtn")

        # Create uploadBtn inside widget3
        self.uploadBtn = QtWidgets.QPushButton(self.widget3)
        self.uploadBtn.setGeometry(QtCore.QRect(690, 10, 41, 23))
        self.uploadBtn.setObjectName("uploadBtn")

        # Create fileNameText inside widget3
        self.filenameText = QtWidgets.QLineEdit(self.widget3)
        self.filenameText.setGeometry(QtCore.QRect(521, 14, 131, 20))
        self.filenameText.setObjectName("filenameText")

        # Create clickLabel inside widget3
        self.clickLabel = QtWidgets.QLabel(self.widget3)
        self.clickLabel.setGeometry(QtCore.QRect(450, 565, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clickLabel.setFont(font)
        self.clickLabel.setObjectName("clickLabel")

        # Add widget3 inside scrollAreaWidgetContents with layout verticalLayour_2
        self.verticalLayout_2.addWidget(self.widget3)

        # Set scrollArea widget to scrollAreaWidgetContents
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Add scrollArea inside centralwidget with layout verticalLayout
        self.verticalLayout.addWidget(self.scrollArea)

        # Set centralwidget as Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Create Menus insaide MainWindow
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 15))
        self.menubar.setObjectName("menubar")

        # Create menuNew inside menubar
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")

        # Create menuEdit inside menubar
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        # Create menuView inside menubar
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        # Set menubar as MainWindow Menu
        MainWindow.setMenuBar(self.menubar)

        # Create statusbar inside MainWindow
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        # Sub Menus
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.actionPreview = QtWidgets.QAction(MainWindow)
        self.actionPreview.setObjectName("actionPreview")

        # Menu Actions
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuView.addAction(self.actionPreview)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.formTitle.setText(_translate("MainWindow", "MEMBERSHIP FORM"))
        self.headingLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">#34 LegendSt. Village East Cainta, Rizal</span></p><p align=\"center\"><span style=\" font-size:9pt;\">(02) 8400-8066 / (02) 8470-7475</span></p><p align=\"center\"><span style=\" font-size:9pt;\">09171829430 / 09985609443</span></p><p align=\"center\"><span style=\" font-size:9pt;\">ofw.transport.cooperative@gmail.com </span></p><p align=\"center\"><span style=\" font-size:9pt;\">Registration No.: 9520-16021151</span></p><p align=\"center\"><span style=\" font-size:9pt;\">Ammendment No.: 9520-16021151-5</span></p></body></html>"))
        self.ofwAbroadLabel.setText(_translate("MainWindow", "OFW Abroad:"))
        self.ofwNameLabel.setText(_translate("MainWindow", "Name:"))
        self.ofwAddressLabel.setText(_translate("MainWindow", "Address:"))
        self.dateLabel.setText(_translate("MainWindow", "Date:"))
        self.beneficiariesLabel.setText(_translate("MainWindow", "Benefeciaries:"))
        self.beneficiaryNameLabel.setText(_translate("MainWindow", "Name:"))
        self.beneficiaryAddressLabel.setText(_translate("MainWindow", "Address:"))
        self.placeOfBirthLabel.setText(_translate("MainWindow", "Place of Birth:"))
        self.provincialAddressLabel.setText(_translate("MainWindow", "Provincial Address:"))
        self.religionLabel.setText(_translate("MainWindow", "Religion:"))
        self.dateOfBirthLabel.setText(_translate("MainWindow", "Date of Birth:"))
        self.contactLabel.setText(_translate("MainWindow", "Contact No.:"))
        self.emailAddLabel.setText(_translate("MainWindow", "Email:"))
        self.ageLabel.setText(_translate("MainWindow", "Age:"))
        self.sexLabel.setText(_translate("MainWindow", "Sex:"))
        self.maleRBtn.setText(_translate("MainWindow", "Male"))
        self.femaleRBtn.setText(_translate("MainWindow", "Female"))
        self.civilStatusLabel.setText(_translate("MainWindow", "Civil Status:"))
        self.citizenshipLabel.setText(_translate("MainWindow", "Citizenship:"))
        self.tinLabel.setText(_translate("MainWindow", "TIN No.:"))
        self.sssLabel.setText(_translate("MainWindow", "SSS No.:"))
        self.hwLabel.setText(_translate("MainWindow", "Husband or Wife:"))
        self.hwNameLabel.setText(_translate("MainWindow", "Name:"))
        self.hwPlaceOfBirthLabel.setText(_translate("MainWindow", "Place of Birth:"))
        self.hwOccupationLabel.setText(_translate("MainWindow", "Occupation:"))
        self.hwDateOfBirthLabel.setText(_translate("MainWindow", "Date of Birth:"))
        self.hwAgeLabel.setText(_translate("MainWindow", "Age:"))
        self.childrenLabel.setText(_translate("MainWindow", "Children:"))
        self.chNameLabel.setText(_translate("MainWindow", "Name:"))
        self.empDateLabel.setText(_translate("MainWindow", "Date employed:"))
        self.chAgeLabel.setText(_translate("MainWindow", "Age:"))
        self.chAddBtn.setText(_translate("MainWindow", "Add"))
        self.empInfoLabel.setText(_translate("MainWindow", "Employment Information:"))
        self.empNameLabel.setText(_translate("MainWindow", "Name:"))
        self.empPositionLabel.setText(_translate("MainWindow", "Position:"))
        self.incaseLabel.setText(_translate("MainWindow", "Contact Incase of Emergency:"))
        self.incaseNameLabel.setText(_translate("MainWindow", "Name:"))
        self.incaseAddressLabel.setText(_translate("MainWindow", "Address:"))
        self.incaseContactLabel.setText(_translate("MainWindow", "Contact No.:"))
        self.clickLabel.setText(_translate("MainWindow", "Clicked"))
        self.chAddressLabel.setText(_translate("MainWindow", "Address:"))
        self.empAddressLabel.setText(_translate("MainWindow", "Address:"))
        self.fileSelectBtn.setText(_translate("MainWindow", "..."))
        self.uploadBtn.setText(_translate("MainWindow", "Upload"))
        self.menuNew.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setStatusTip(_translate("MainWindow", "Move file"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionPreview.setText(_translate("MainWindow", "Preview"))
        self.actionPreview.setStatusTip(_translate("MainWindow", "Preview a file"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
