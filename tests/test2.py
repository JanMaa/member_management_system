# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(350, 45, 771, 671)
        #MainWindow.resize(771, 671)

        #Creating size policy for MainWindow
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        #Set size policy for Mainwindow
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(771, 671))
        MainWindow.setMaximumSize(QtCore.QSize(771, 671))

        #Creat centralwidget and its size policy
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        #Set size policy for centralwidget
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(771, 655))
        self.centralwidget.setMaximumSize(QtCore.QSize(771, 655))
        self.centralwidget.setObjectName("centralwidget")

        #Create verticalLayout for centralwidget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        #Create scrollArea widget inside centralwidget
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())

        #Set size policy for scrollArea widget
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(771, 655))
        self.scrollArea.setMaximumSize(QtCore.QSize(771, 655))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")

        #Create scrollAreaWidgetContents widget
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 771, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(771, 800))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(771, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Create verticalLayout_2 for scrollAreaWidgetContents
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #Create widget1 inside scrollAreaWidgetContents
        self.widget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())

        #Set size policy of widget1
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMaximumSize(QtCore.QSize(753, 40))
        self.widget1.setAutoFillBackground(False)
        self.widget1.setStyleSheet("border-color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.widget1.setObjectName("widget1")

        #Create horizontalLayout_3 for widget1
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        #Create forTitle widget inside widget1
        self.formTitle = QtWidgets.QLabel(self.widget1)
        self.formTitle.setMaximumSize(QtCore.QSize(200, 30))
        self.formTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formTitle.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 75 16pt \"Times New Roman\";")
        self.formTitle.setScaledContents(False)
        self.formTitle.setIndent(0)
        self.formTitle.setObjectName("formTitle")

        #Create horizontalLayout_3 for formTitle
        self.horizontalLayout_3.addWidget(self.formTitle)

        #Add widget1 inside scrollAreaWidgetContents with layout verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget1)

        #Create widgets2 inside scrollAreaWidgetContents
        self.widget2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget2.setMaximumSize(QtCore.QSize(753, 197))
        self.widget2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget2.setObjectName("widget2")

        #Create horizontalLayout_2 for widget2
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(350)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #Create logoWidget inside widget2
        self.logoWidget = QtWidgets.QWidget(self.widget2)
        self.logoWidget.setMaximumSize(QtCore.QSize(192, 192))
        self.logoWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.logoWidget.setObjectName("logoWidget")

        #Create logoLabel onside logoWidget
        self.logoLabel = QtWidgets.QLabel(self.logoWidget)
        self.logoLabel.setGeometry(QtCore.QRect(80, 80, 31, 16))
        self.logoLabel.setObjectName("logoLabel")

        #Add logo widget to widget2 with layout horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.logoWidget)

        #Create uploadImgWidget inside widget2
        self.uploadImgWidget = QtWidgets.QWidget(self.widget2)
        self.uploadImgWidget.setMaximumSize(QtCore.QSize(192, 192))
        self.uploadImgWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.uploadImgWidget.setObjectName("uploadImgWidget")

        #Create uploadImgLabel inside uploadImgWidget
        self.uploadImgLabel = QtWidgets.QLabel(self.uploadImgWidget)
        self.uploadImgLabel.setGeometry(QtCore.QRect(60, 80, 71, 16))
        self.uploadImgLabel.setObjectName("uploadImgLabel")

        #Add uploadImgWidget inside widget2 with layout horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.uploadImgWidget)

        #Add widget2 inside scrollAreaWidgetContents with layout verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget2)

        #Create widget3 inside scrollAreWidgetContents
        self.widget3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)

        #Create size policy for widget3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget3.sizePolicy().hasHeightForWidth())

        #Set size policy for widget3
        self.widget3.setSizePolicy(sizePolicy)
        self.widget3.setMinimumSize(QtCore.QSize(753, 558))
        self.widget3.setMaximumSize(QtCore.QSize(753, 558))
        self.widget3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget3.setObjectName("widget3")

        #Create ofwAbroadLabel inside widget3
        self.ofwAbroadLabel = QtWidgets.QLabel(self.widget3)
        self.ofwAbroadLabel.setGeometry(QtCore.QRect(20, 30, 66, 16))
        self.ofwAbroadLabel.setObjectName("ofwAbroadLabel")

        #Create ofwNameInput inside widget3
        self.ofwNameInput = QtWidgets.QLineEdit(self.widget3)
        self.ofwNameInput.setGeometry(QtCore.QRect(100, 50, 261, 20))
        self.ofwNameInput.setObjectName("ofwNameInput")

        #Create ofwNameLabel inside widget3
        self.ofwNameLabel = QtWidgets.QLabel(self.widget3)
        self.ofwNameLabel.setGeometry(QtCore.QRect(50, 50, 31, 16))
        self.ofwNameLabel.setObjectName("ofwNameLabel")

        #Create ofwAdressInput inside widget3
        self.ofwAddressInput = QtWidgets.QLineEdit(self.widget3)
        self.ofwAddressInput.setGeometry(QtCore.QRect(440, 50, 291, 20))
        self.ofwAddressInput.setObjectName("ofwAddressInput")

        #Create ofwAddressLabel inside widget3
        self.ofwAddressLabel = QtWidgets.QLabel(self.widget3)
        self.ofwAddressLabel.setGeometry(QtCore.QRect(390, 50, 41, 16))
        self.ofwAddressLabel.setObjectName("ofwAddressLabel")

        #Create dateLabel inside widget3
        self.dateLabel = QtWidgets.QLabel(self.widget3)
        self.dateLabel.setGeometry(QtCore.QRect(570, 20, 31, 16))
        self.dateLabel.setObjectName("dateLabel")

        #Create dateInput inside widget3
        self.dateInput = QtWidgets.QLineEdit(self.widget3)
        self.dateInput.setGeometry(QtCore.QRect(600, 20, 131, 20))
        self.dateInput.setObjectName("dateInput")

        #Create beneficiariesLabel inside widget3
        self.beneficiariesLabel = QtWidgets.QLabel(self.widget3)
        self.beneficiariesLabel.setGeometry(QtCore.QRect(20, 70, 66, 16))
        self.beneficiariesLabel.setObjectName("beneficiariesLabel")

        #Create beneficiaryNameLabel inside widget3
        self.beneficiaryNameLabel = QtWidgets.QLabel(self.widget3)
        self.beneficiaryNameLabel.setGeometry(QtCore.QRect(50, 90, 31, 16))
        self.beneficiaryNameLabel.setObjectName("beneficiaryNameLabel")

        #Create beneficiaryNameInput inside widget3
        self.beneficiaryNameInput = QtWidgets.QLineEdit(self.widget3)
        self.beneficiaryNameInput.setGeometry(QtCore.QRect(100, 90, 261, 20))
        self.beneficiaryNameInput.setObjectName("beneficiaryNameInput")

        #Create beneficiaryAddressLabel inside widget3
        self.beneficiaryAddressLabel = QtWidgets.QLabel(self.widget3)
        self.beneficiaryAddressLabel.setGeometry(QtCore.QRect(390, 90, 41, 16))
        self.beneficiaryAddressLabel.setObjectName("beneficiaryAddressLabel")

        #Create beneficiaryAddressInput inside widget3
        self.beneficiaryAddresInput = QtWidgets.QLineEdit(self.widget3)
        self.beneficiaryAddresInput.setGeometry(QtCore.QRect(440, 90, 291, 20))
        self.beneficiaryAddresInput.setObjectName("beneficiaryAddresInput")

        # Create placeOfBirthInput inside widget3
        self.placeOfBirthInput = QtWidgets.QLineEdit(self.widget3)
        self.placeOfBirthInput.setGeometry(QtCore.QRect(100, 120, 261, 20))
        self.placeOfBirthInput.setObjectName("placeOfBirthInput")

        # Create placeOfBirthLabel inside widget3
        self.placeOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.placeOfBirthLabel.setGeometry(QtCore.QRect(20, 120, 71, 16))
        self.placeOfBirthLabel.setObjectName("placeOfBirthLabel")

        # Create provincialAddressInput inside widget3
        self.provincialAddressInput = QtWidgets.QLineEdit(self.widget3)
        self.provincialAddressInput.setGeometry(QtCore.QRect(480, 120, 251, 20))
        self.provincialAddressInput.setObjectName("provincialAddressInput")

        # Create provincialAddressLabel inside widget3
        self.provincialAddressLabel = QtWidgets.QLabel(self.widget3)
        self.provincialAddressLabel.setGeometry(QtCore.QRect(380, 120, 91, 16))
        self.provincialAddressLabel.setObjectName("provincialAddressLabel")

        # Create religionInput inside widget3
        self.religionInput = QtWidgets.QLineEdit(self.widget3)
        self.religionInput.setGeometry(QtCore.QRect(480, 150, 251, 20))
        self.religionInput.setObjectName("religionInput")

        #Create religionLabel inside widget3
        self.religionLabel = QtWidgets.QLabel(self.widget3)
        self.religionLabel.setGeometry(QtCore.QRect(430, 150, 41, 16))
        self.religionLabel.setObjectName("religionLabel")

        # Create dateOfBirthInput inside widget3
        self.dateOfBirthInput = QtWidgets.QLineEdit(self.widget3)
        self.dateOfBirthInput.setGeometry(QtCore.QRect(100, 150, 261, 20))
        self.dateOfBirthInput.setObjectName("dateOfBirthInput")

        # Create dateOfBirthLabel inside widget3
        self.dateOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.dateOfBirthLabel.setGeometry(QtCore.QRect(20, 150, 71, 16))
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")


        # Create contactInput inside widget3
        self.contactInput = QtWidgets.QLineEdit(self.widget3)
        self.contactInput.setGeometry(QtCore.QRect(100, 180, 261, 20))
        self.contactInput.setObjectName("contactInput")

        # Create contactLabel inside widget3
        self.contactLabel = QtWidgets.QLabel(self.widget3)
        self.contactLabel.setGeometry(QtCore.QRect(20, 180, 71, 16))
        self.contactLabel.setObjectName("contactLabel")

        # Create emailAddInput inside widget3
        self.emailAddInput = QtWidgets.QLineEdit(self.widget3)
        self.emailAddInput.setGeometry(QtCore.QRect(480, 180, 251, 20))
        self.emailAddInput.setObjectName("emailAddInput")

        # Create emailAddLabel inside widget3
        self.emailAddLabel = QtWidgets.QLabel(self.widget3)
        self.emailAddLabel.setGeometry(QtCore.QRect(400, 180, 81, 16))
        self.emailAddLabel.setObjectName("emailAddLabel")

        # Create ageLabel inside widget3
        self.ageLabel = QtWidgets.QLabel(self.widget3)
        self.ageLabel.setGeometry(QtCore.QRect(60, 210, 31, 16))
        self.ageLabel.setObjectName("ageLabel")

        # Create ageInput inside widget3
        self.ageInput = QtWidgets.QLineEdit(self.widget3)
        self.ageInput.setGeometry(QtCore.QRect(100, 210, 51, 20))
        self.ageInput.setObjectName("ageInput")

        # Create sexLabel inside widget3
        self.sexLabel = QtWidgets.QLabel(self.widget3)
        self.sexLabel.setGeometry(QtCore.QRect(180, 210, 31, 16))
        self.sexLabel.setObjectName("sexLabel")

        # Create maleRBtn inside widget3
        self.maleRBtn = QtWidgets.QRadioButton(self.widget3)
        self.maleRBtn.setGeometry(QtCore.QRect(210, 210, 41, 17))
        self.maleRBtn.setObjectName("maleRBtn")

        # Create femaleRBtn inside widget3
        self.femaleRBtn = QtWidgets.QRadioButton(self.widget3)
        self.femaleRBtn.setGeometry(QtCore.QRect(260, 210, 61, 17))
        self.femaleRBtn.setObjectName("femaleRBtn")

        # Create civilStatusLabel inside widget3
        self.civilStatusLabel = QtWidgets.QLabel(self.widget3)
        self.civilStatusLabel.setGeometry(QtCore.QRect(410, 210, 61, 16))
        self.civilStatusLabel.setObjectName("civilStatusLabel")

        # Create civilStatusInput inside widget3
        self.civilStatusInput = QtWidgets.QLineEdit(self.widget3)
        self.civilStatusInput.setGeometry(QtCore.QRect(480, 210, 251, 20))
        self.civilStatusInput.setObjectName("civilStatusInput")

        # Create citizenshipLabel inside widget3
        self.citizenshipLabel = QtWidgets.QLabel(self.widget3)
        self.citizenshipLabel.setGeometry(QtCore.QRect(30, 240, 61, 16))
        self.citizenshipLabel.setObjectName("citizenshipLabel")

        # Create citizenshipInput inside widget3
        self.citizenshipInput = QtWidgets.QLineEdit(self.widget3)
        self.citizenshipInput.setGeometry(QtCore.QRect(100, 240, 261, 20))
        self.citizenshipInput.setObjectName("citizenshipInput")

        # Create tinLabel inside widget3
        self.tinLabel = QtWidgets.QLabel(self.widget3)
        self.tinLabel.setGeometry(QtCore.QRect(430, 240, 41, 20))
        self.tinLabel.setObjectName("tinLabel")

        # Create tinInput inside widget3
        self.tinInput = QtWidgets.QLineEdit(self.widget3)
        self.tinInput.setGeometry(QtCore.QRect(480, 240, 251, 20))
        self.tinInput.setObjectName("tinInput")

        # Create sssLabel inside widget3
        self.sssLabel = QtWidgets.QLabel(self.widget3)
        self.sssLabel.setGeometry(QtCore.QRect(430, 270, 51, 16))
        self.sssLabel.setObjectName("sssLabel")

        # Create sssInput inside widget3
        self.sssInput = QtWidgets.QLineEdit(self.widget3)
        self.sssInput.setGeometry(QtCore.QRect(480, 270, 251, 20))
        self.sssInput.setObjectName("sssInput")

        # Create hwLabel inside widget3
        self.hwLabel = QtWidgets.QLabel(self.widget3)
        self.hwLabel.setGeometry(QtCore.QRect(10, 280, 91, 16))
        self.hwLabel.setObjectName("hwLabel")

        # Create hwNameLabel inside widget3
        self.hwNameLabel = QtWidgets.QLabel(self.widget3)
        self.hwNameLabel.setGeometry(QtCore.QRect(60, 300, 31, 16))
        self.hwNameLabel.setObjectName("hwNameLabel")

        # Create hwNameInput inside widget3
        self.hwNameInput = QtWidgets.QLineEdit(self.widget3)
        self.hwNameInput.setGeometry(QtCore.QRect(100, 300, 261, 20))
        self.hwNameInput.setObjectName("hwNameInput")

        # Create hwPlaceOFBirthLabel inside widget3
        self.hwPlaceOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.hwPlaceOfBirthLabel.setGeometry(QtCore.QRect(410, 300, 71, 16))
        self.hwPlaceOfBirthLabel.setObjectName("hwPlaceOfBirthLabel")

        # Create hwPlaceOfBirthInput inside widget3
        self.hwPllaceOfBirthInput = QtWidgets.QLineEdit(self.widget3)
        self.hwPllaceOfBirthInput.setGeometry(QtCore.QRect(480, 300, 251, 20))
        self.hwPllaceOfBirthInput.setObjectName("hwPllaceOfBirthInput")

        # Create hwOccupationLabel inside widget3
        self.hwOccupationLabel = QtWidgets.QLabel(self.widget3)
        self.hwOccupationLabel.setGeometry(QtCore.QRect(420, 330, 61, 16))
        self.hwOccupationLabel.setObjectName("hwOccupationLabel")

        # Create hwOccupationInput inside widget3
        self.hwOccupationInput = QtWidgets.QLineEdit(self.widget3)
        self.hwOccupationInput.setGeometry(QtCore.QRect(480, 330, 251, 20))
        self.hwOccupationInput.setObjectName("hwOccupationInput")

        # Create hwDateOfBirthLabel inside widget3
        self.hwDateOfBirthLabel = QtWidgets.QLabel(self.widget3)
        self.hwDateOfBirthLabel.setGeometry(QtCore.QRect(30, 330, 71, 16))
        self.hwDateOfBirthLabel.setObjectName("hwDateOfBirthLabel")

        # Create hwDateOfBirthInput inside widget3
        self.hwDateOfBirthInput = QtWidgets.QLineEdit(self.widget3)
        self.hwDateOfBirthInput.setGeometry(QtCore.QRect(100, 330, 171, 20))
        self.hwDateOfBirthInput.setObjectName("hwDateOfBirthInput")

        # Create hwAgeLabel inside widget3
        self.hwAgeLabel = QtWidgets.QLabel(self.widget3)
        self.hwAgeLabel.setGeometry(QtCore.QRect(280, 330, 31, 16))
        self.hwAgeLabel.setObjectName("hwAgeLabel")

        # Create hwAgeInput inside widget3
        self.hwAgeInput = QtWidgets.QLineEdit(self.widget3)
        self.hwAgeInput.setGeometry(QtCore.QRect(310, 330, 51, 20))
        self.hwAgeInput.setObjectName("hwAgeInput")

        # Create childrenLabel inside widget3
        self.childrenLabel = QtWidgets.QLabel(self.widget3)
        self.childrenLabel.setGeometry(QtCore.QRect(50, 360, 51, 16))
        self.childrenLabel.setObjectName("childrenLabel")

        # Create chNameLabel inside widget3
        self.chNameLabel = QtWidgets.QLabel(self.widget3)
        self.chNameLabel.setGeometry(QtCore.QRect(60, 380, 31, 16))
        self.chNameLabel.setObjectName("chNameLabel")

        # Create chNameInput inside widget3
        self.chNameInput = QtWidgets.QLineEdit(self.widget3)
        self.chNameInput.setGeometry(QtCore.QRect(100, 380, 231, 20))
        self.chNameInput.setObjectName("chNameInput")

        # Create chAdressLabel inside widget3
        self.chAddressLabel = QtWidgets.QLabel(self.widget3)
        self.chAddressLabel.setGeometry(QtCore.QRect(340, 380, 41, 16))
        self.chAddressLabel.setObjectName("chAddressLabel")

        # Create chAdressInput inside widget3
        self.chAdressInput = QtWidgets.QLineEdit(self.widget3)
        self.chAdressInput.setGeometry(QtCore.QRect(390, 380, 231, 20))
        self.chAdressInput.setText("")
        self.chAdressInput.setObjectName("chAdressInput")

        # Create chAgeLabel inside widget3
        self.chAgeLabel = QtWidgets.QLabel(self.widget3)
        self.chAgeLabel.setGeometry(QtCore.QRect(630, 380, 31, 16))
        self.chAgeLabel.setObjectName("chAgeLabel")

        # Create chAgeInput inside widget3
        self.chAgeInput = QtWidgets.QLineEdit(self.widget3)
        self.chAgeInput.setGeometry(QtCore.QRect(660, 380, 31, 20))
        self.chAgeInput.setObjectName("chAgeInput")

        # Create chAddBtn inside widget3
        self.chAddBtn = QtWidgets.QPushButton(self.widget3)
        self.chAddBtn.setGeometry(QtCore.QRect(700, 380, 31, 21))
        self.chAddBtn.setObjectName("chAddBtn")

        # Create empInfoLabel inside widget3
        self.empInfoLabel = QtWidgets.QLabel(self.widget3)
        self.empInfoLabel.setGeometry(QtCore.QRect(20, 410, 131, 16))
        self.empInfoLabel.setObjectName("empInfoLabel")

        # Create empNameLabel inside widget3
        self.empNameLabel = QtWidgets.QLabel(self.widget3)
        self.empNameLabel.setGeometry(QtCore.QRect(10, 430, 81, 20))
        self.empNameLabel.setObjectName("empNameLabel")

        # Create empNameInput inside widget3
        self.empNameInput = QtWidgets.QLineEdit(self.widget3)
        self.empNameInput.setGeometry(QtCore.QRect(100, 430, 231, 20))
        self.empNameInput.setObjectName("empNameInput")

        # Create empDateLabel inside widget3
        self.empDateLabel = QtWidgets.QLabel(self.widget3)
        self.empDateLabel.setGeometry(QtCore.QRect(350, 430, 81, 16))
        self.empDateLabel.setObjectName("empDateLabel")

        # Create empDateInput inside widget3
        self.empDateInput = QtWidgets.QLineEdit(self.widget3)
        self.empDateInput.setGeometry(QtCore.QRect(430, 430, 71, 20))
        self.empDateInput.setText("")
        self.empDateInput.setObjectName("empDateInput")

        # Create empPositionLabel inside widget3
        self.empPositionLabel = QtWidgets.QLabel(self.widget3)
        self.empPositionLabel.setGeometry(QtCore.QRect(510, 430, 41, 16))
        self.empPositionLabel.setObjectName("empPositionLabel")

        # Create empPositionInput inside widget3
        self.empPositionInput = QtWidgets.QLineEdit(self.widget3)
        self.empPositionInput.setGeometry(QtCore.QRect(560, 430, 171, 20))
        self.empPositionInput.setText("")
        self.empPositionInput.setObjectName("empPositionInput")

        # Create incaseLabel inside widget3
        self.incaseLabel = QtWidgets.QLabel(self.widget3)
        self.incaseLabel.setGeometry(QtCore.QRect(10, 470, 151, 16))
        self.incaseLabel.setObjectName("incaseLabel")

        # Create incaseNameLabel inside widget3
        self.incaseNameLabel = QtWidgets.QLabel(self.widget3)
        self.incaseNameLabel.setGeometry(QtCore.QRect(60, 490, 31, 16))
        self.incaseNameLabel.setObjectName("incaseNameLabel")

        # Create incaseNameLabel inside widget3
        self.incaseNameInput = QtWidgets.QLineEdit(self.widget3)
        self.incaseNameInput.setGeometry(QtCore.QRect(100, 490, 251, 20))
        self.incaseNameInput.setObjectName("incaseNameInput")

        # Create incaseAddressLabel inside widget3
        self.incaseAddressLabel = QtWidgets.QLabel(self.widget3)
        self.incaseAddressLabel.setGeometry(QtCore.QRect(50, 520, 41, 16))
        self.incaseAddressLabel.setObjectName("incaseAddressLabel")

        # Create incaseContactInput inside widget3
        self.incaseContactInput = QtWidgets.QLineEdit(self.widget3)
        self.incaseContactInput.setGeometry(QtCore.QRect(480, 490, 161, 20))
        self.incaseContactInput.setObjectName("incaseContactInput")

        # Create incaseAddressInput inside widget3
        self.incaseAdressInput = QtWidgets.QLineEdit(self.widget3)
        self.incaseAdressInput.setGeometry(QtCore.QRect(100, 520, 251, 20))
        self.incaseAdressInput.setObjectName("incaseAdressInput")

        # Create incaseContactLabel inside widget3
        self.incaseContactLabel = QtWidgets.QLabel(self.widget3)
        self.incaseContactLabel.setGeometry(QtCore.QRect(410, 490, 61, 16))
        self.incaseContactLabel.setObjectName("incaseContactLabel")

        #Add widget3 inside scrollAreaWidgetContents with layout verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget3)

        #Set scrollAreaWidgetContents as scrollArea widget
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #Add scrollArea widget inside centralwidget with layout verticalLayout
        self.verticalLayout.addWidget(self.scrollArea)

        #Set cenralwidget as MainWindow Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        #Creat menubar for Mainwindow
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 21))
        self.menubar.setObjectName("menubar")

        #Set menubar as MainWindow menu
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.formTitle.setText(_translate("MainWindow", "MEMBERSHIP FORM"))
        self.logoLabel.setText(_translate("MainWindow", "Logo"))
        self.uploadImgLabel.setText(_translate("MainWindow", "Upload Image"))
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
        self.dateOfBirthLabel.setText(_translate("MainWindow", "Date of Birth.:"))
        self.contactLabel.setText(_translate("MainWindow", "Contact No.:"))
        self.emailAddLabel.setText(_translate("MainWindow", "Email Address:"))
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
        self.chAddressLabel.setText(_translate("MainWindow", "Address:"))
        self.chAgeLabel.setText(_translate("MainWindow", "Age:"))
        self.chAddBtn.setText(_translate("MainWindow", "Add"))
        self.empInfoLabel.setText(_translate("MainWindow", "Employment Information:"))
        self.empNameLabel.setText(_translate("MainWindow", "Employer Name:"))
        self.empDateLabel.setText(_translate("MainWindow", "Date employed:"))
        self.empPositionLabel.setText(_translate("MainWindow", "Position:"))
        self.incaseLabel.setText(_translate("MainWindow", "Contact Incase of Emergency:"))
        self.incaseNameLabel.setText(_translate("MainWindow", "Name:"))
        self.incaseAddressLabel.setText(_translate("MainWindow", "Address:"))
        self.incaseContactLabel.setText(_translate("MainWindow", "Contact No.:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
