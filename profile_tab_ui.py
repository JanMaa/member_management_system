from PyQt5.QtCore import QSize, QRect, Qt, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QWidget, QScrollArea, QSizePolicy, QVBoxLayout, QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QLineEdit, QTabWidget
from PyQt5.QtGui import QFont, QPixmap

class ProfileUI(QTabWidget):

    def __init__(self, ProfileTab):
        super().__init__()

        ProfileTab.setObjectName("ProfileTab")

        # Create scrollArea widget inside centralwidget
        self.scrollArea = QScrollArea(ProfileTab)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())

        # Set size policy for scrollArea widget
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(767, 620))
        self.scrollArea.setMaximumSize(QSize(767, 620))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")

        # Create scrollAreaWidgetContents widget
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -176, 771, 1380))

        # Create size policy for scrollAreaWidgetContents
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())

        # Set scrollAreaWidgetContents size policy
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(771, 1380))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(771, 1380))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Create verticalLayout_2 for scrollAreaWidgetContents
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Create widget1 inside scrollAreaWidgetContents
        self.widget1 = QWidget(self.scrollAreaWidgetContents)

        # Create size policy for widget1
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())

        # Set size policy for widget1
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMaximumSize(QSize(753, 40))
        self.widget1.setAutoFillBackground(False)
        self.widget1.setStyleSheet("border-color: rgb(0, 0, 255);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.widget1.setObjectName("widget1")

        # Create horizontalLayout_3 for widget1
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(25, 8, 10, 8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Create profileHeading inside widget1
        self.profileHeading = QLabel(self.widget1)
        self.profileHeading.setMinimumSize(QSize(0, 0))
        self.profileHeading.setMaximumSize(QSize(305, 40))
        self.profileHeading.setLayoutDirection(Qt.LeftToRight)
        self.profileHeading.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.profileHeading.setScaledContents(False)
        self.profileHeading.setIndent(0)
        self.profileHeading.setObjectName("profileHeading")

        # Add formTitle inside widget1 with layout horizontalLayout_3
        self.horizontalLayout_3.addWidget(self.profileHeading)

        # Add widget1 inside scrollAreaWidgetContents with layout verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget1)

        # Create widgets2 inside scrollAreaWidgetContents
        self.widget2 = QWidget(self.scrollAreaWidgetContents)
        self.widget2.setMaximumSize(QSize(753, 197))
        self.widget2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget2.setObjectName("widget2")

        # Create horizontalLayout_2 for widget2
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Create logoWidget inside widget2
        self.logoWidget = QWidget(self.widget2)
        self.logoWidget.setMaximumSize(QSize(192, 192))
        self.logoWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "gridline-color: rgb(0, 0, 0);\n"
                                      "border-color: rgb(0, 0, 0);")
        self.logoWidget.setObjectName("logoWidget")

        # Create logoImage inside logoWidget
        self.logoImage = QLabel(self.logoWidget)
        self.logoImage.setGeometry(QRect(10, 10, 171, 161))
        self.logoImage.setText("")
        self.logoImage.setPixmap(QPixmap("../../Downloads/OFWTSMPC (1).png"))
        self.logoImage.setScaledContents(True)
        self.logoImage.setObjectName("logoImage")

        # Add logo widget to widget2 with layout horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.logoWidget)

        # Create headingWidget inside widget2
        self.headingWidget = QWidget(self.widget2)
        self.headingWidget.setObjectName("headingWidget")

        # Create headingLabel inside headingWidget
        self.headingLabel = QLabel(self.headingWidget)
        self.headingLabel.setGeometry(QRect(10, 10, 311, 161))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")

        # Add headingWidget inside widget2 with layout horizontalLayout2
        self.horizontalLayout_2.addWidget(self.headingWidget)

        # Create uploadImgWidget inside widget2
        self.uploadImgWidget = QWidget(self.widget2)
        self.uploadImgWidget.setMaximumSize(QSize(192, 192))
        self.uploadImgWidget.setObjectName("uploadImgWidget")

        # Create imgDefault inside uploadImgWidget
        self.imgDefault = QLabel(self.uploadImgWidget)
        self.imgDefault.setGeometry(QRect(0, 0, 192, 192))
        self.imgDefault.setPixmap(QPixmap("img/default_avatar.png"))
        self.imgDefault.setScaledContents(True)
        self.imgDefault.setObjectName("imgDefault")

        # Add uploadImgWidget inside widget2 with layout horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.uploadImgWidget)

        # Add widget2 inside scrollAreaWidgetContents with layout verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget2)

        # Create widget3 inside scrollAreWidgetContents
        self.widget3 = QWidget(self.scrollAreaWidgetContents)

        # Create size policy for widget3
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget3.sizePolicy().hasHeightForWidth())

        # Set size policy for widget3
        self.widget3.setSizePolicy(sizePolicy)
        self.widget3.setMinimumSize(QSize(753, 1143))
        self.widget3.setMaximumSize(QSize(753, 1143))
        font = QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.widget3.setFont(font)
        self.widget3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget3.setObjectName("widget3")

        #################################

        self.dateRegistered = QLabel(self.widget3)
        self.dateRegistered.setGeometry(QRect(550, 7, 110, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateRegistered.setFont(font)
        self.dateRegistered.setObjectName("dateRegistered")

        self.date_registered = QLabel(self.widget3)
        self.date_registered.setGeometry(QRect(660, 8, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.date_registered.setFont(font)

        self.date_registered.setObjectName("date_registered")

        self.ofwName = QLabel(self.widget3)
        self.ofwName.setGeometry(QRect(48, 42, 79, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ofwName.setFont(font)
        self.ofwName.setObjectName("ofwName")

        self.ofw_name = QLabel(self.widget3)
        self.ofw_name.setGeometry(QRect(130, 41, 64, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ofw_name.setFont(font)
        self.ofw_name.setObjectName("ofw_name")

        self.ofwAddress = QLabel(self.widget3)
        self.ofwAddress.setGeometry(QRect(66, 67, 60, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ofwAddress.setFont(font)
        self.ofwAddress.setObjectName("ofwAddress")

        self.ofw_address = QLabel(self.widget3)
        self.ofw_address.setGeometry(QRect(130, 66, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ofw_address.setFont(font)
        self.ofw_address.setObjectName("ofw_address")

        self.name = QLabel(self.widget3)
        self.name.setGeometry(QRect(82, 92, 45, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")

        self.name_ = QLabel(self.widget3)
        self.name_.setGeometry(QRect(130, 91, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name_.setFont(font)
        self.name_.setObjectName("name_")

        self.address = QLabel(self.widget3)
        self.address.setGeometry(QRect(67, 117, 60, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.address.setFont(font)
        self.address.setObjectName("address")

        self.address_ = QLabel(self.widget3)
        self.address_.setGeometry(QRect(130, 116, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.address_.setFont(font)
        self.address_.setObjectName("address_")

        self.pob = QLabel(self.widget3)
        self.pob.setGeometry(QRect(36, 142, 92, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pob.setFont(font)
        self.pob.setObjectName("pob")

        self.pob_ = QLabel(self.widget3)
        self.pob_.setGeometry(QRect(130, 141, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pob_.setFont(font)
        self.pob_.setObjectName("pob_")

        self.pAddress = QLabel(self.widget3)
        self.pAddress.setGeometry(QRect(1, 167, 129, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pAddress.setFont(font)
        self.pAddress.setObjectName("pAddress")

        self.p_address = QLabel(self.widget3)
        self.p_address.setGeometry(QRect(130, 166, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.p_address.setFont(font)
        self.p_address.setObjectName("p_address")

        self.dob = QLabel(self.widget3)
        self.dob.setGeometry(QRect(43, 192, 86, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dob.setFont(font)
        self.dob.setObjectName("dob")

        self.dob_ = QLabel(self.widget3)
        self.dob_.setGeometry(QRect(130, 191, 64, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dob_.setFont(font)
        self.dob_.setObjectName("dob_")

        self.age = QLabel(self.widget3)
        self.age.setGeometry(QRect(95, 214, 33, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.age.setFont(font)
        self.age.setObjectName("age")

        self.age_ = QLabel(self.widget3)
        self.age_.setGeometry(QRect(130, 213, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.age_.setFont(font)
        self.age_.setObjectName("age_")

        self.sex = QLabel(self.widget3)
        self.sex.setGeometry(QRect(99, 239, 29, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sex.setFont(font)
        self.sex.setObjectName("sex")

        self.sex_ = QLabel(self.widget3)
        self.sex_.setGeometry(QRect(130, 239, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sex_.setFont(font)
        self.sex_.setObjectName("sex_")

        self.religion = QLabel(self.widget3)
        self.religion.setGeometry(QRect(68, 261, 60, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.religion.setFont(font)
        self.religion.setObjectName("religion")

        self.religion_ = QLabel(self.widget3)
        self.religion_.setGeometry(QRect(130, 260, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.religion_.setFont(font)
        self.religion_.setObjectName("religion_")

        self.contactNo = QLabel(self.widget3)
        self.contactNo.setGeometry(QRect(50, 286, 80, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.contactNo.setFont(font)
        self.contactNo.setObjectName("contactNo")

        self.contact_no = QLabel(self.widget3)
        self.contact_no.setGeometry(QRect(130, 286, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.contact_no.setFont(font)
        self.contact_no.setObjectName("contact_no")

        self.email = QLabel(self.widget3)
        self.email.setGeometry(QRect(87, 311, 43, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")

        self.email_ = QLabel(self.widget3)
        self.email_.setGeometry(QRect(130, 310, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.email_.setFont(font)
        self.email_.setObjectName("email_")

        self.tinNo = QLabel(self.widget3)
        self.tinNo.setGeometry(QRect(77, 336, 53, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tinNo.setFont(font)
        self.tinNo.setObjectName("tinNo")

        self.tin_no = QLabel(self.widget3)
        self.tin_no.setGeometry(QRect(130, 336, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tin_no.setFont(font)
        self.tin_no.setObjectName("tin_no")

        self.citizenship = QLabel(self.widget3)
        self.citizenship.setGeometry(QRect(52, 358, 78, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.citizenship.setFont(font)
        self.citizenship.setObjectName("citizenship")

        self.citizenship_ = QLabel(self.widget3)
        self.citizenship_.setGeometry(QRect(130, 358, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.citizenship_.setFont(font)
        self.citizenship_.setObjectName("citizenship_")

        self.status = QLabel(self.widget3)
        self.status.setGeometry(QRect(50, 383, 78, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")

        self.status_ = QLabel(self.widget3)
        self.status_.setGeometry(QRect(130, 383, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.status_.setFont(font)
        self.status_.setObjectName("status_")

        self.sssNo = QLabel(self.widget3)
        self.sssNo.setGeometry(QRect(73, 408, 54, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sssNo.setFont(font)
        self.sssNo.setObjectName("sssNo")

        self.sss_no = QLabel(self.widget3)
        self.sss_no.setGeometry(QRect(130, 408, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sss_no.setFont(font)
        self.sss_no.setObjectName("sss_no")

        self.hwName = QLabel(self.widget3)
        self.hwName.setGeometry(QRect(10, 433, 142, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hwName.setFont(font)
        self.hwName.setObjectName("hwName")

        self.hw_name = QLabel(self.widget3)
        self.hw_name.setGeometry(QRect(154, 434, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hw_name.setFont(font)
        self.hw_name.setObjectName("hw_name")

        self.hwPob = QLabel(self.widget3)
        self.hwPob.setGeometry(QRect(59, 458, 92, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hwPob.setFont(font)
        self.hwPob.setObjectName("hwPob")

        self.hw_pob = QLabel(self.widget3)
        self.hw_pob.setGeometry(QRect(154, 459, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hw_pob.setFont(font)
        self.hw_pob.setObjectName("hw_pob")

        self.hwDob = QLabel(self.widget3)
        self.hwDob.setGeometry(QRect(64, 483, 86, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hwDob.setFont(font)
        self.hwDob.setObjectName("hwDob")

        self.hw_dob = QLabel(self.widget3)
        self.hw_dob.setGeometry(QRect(154, 484, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hw_dob.setFont(font)
        self.hw_dob.setObjectName("hw_dob")

        self.hwAge = QLabel(self.widget3)
        self.hwAge.setGeometry(QRect(116, 505, 34, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hwAge.setFont(font)
        self.hwAge.setObjectName("hwAge")

        self.hw_age = QLabel(self.widget3)
        self.hw_age.setGeometry(QRect(154, 506, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hw_age.setFont(font)
        self.hw_age.setObjectName("hw_age")

        self.occupation = QLabel(self.widget3)
        self.occupation.setGeometry(QRect(65, 527, 84, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.occupation.setFont(font)
        self.occupation.setObjectName("occupation")

        self.occupation_ = QLabel(self.widget3)
        self.occupation_.setGeometry(QRect(154, 527, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.occupation_.setFont(font)
        self.occupation_.setObjectName("occupation_")

        self.children = QLabel(self.widget3)
        self.children.setGeometry(QRect(340, 558, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.children.setFont(font)
        self.children.setObjectName("children")

        self.creatingTables()

        self.employerInfo = QLabel(self.widget3)
        self.employerInfo.setGeometry(QRect(2, 750, 145, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.employerInfo.setFont(font)
        self.employerInfo.setObjectName("employerInfo")

        self.empName = QLabel(self.widget3)
        self.empName.setGeometry(QRect(73, 770, 47, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.empName.setFont(font)
        self.empName.setObjectName("empName")

        self.emp_name = QLabel(self.widget3)
        self.emp_name.setGeometry(QRect(120, 770, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emp_name.setFont(font)
        self.emp_name.setObjectName("emp_name")

        self.position = QLabel(self.widget3)
        self.position.setGeometry(QRect(63, 796, 56, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.position.setFont(font)
        self.position.setObjectName("position")

        self.position_ = QLabel(self.widget3)
        self.position_.setGeometry(QRect(120, 795, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.position_.setFont(font)
        self.position_.setObjectName("position_")

        self.empAddress = QLabel(self.widget3)
        self.empAddress.setGeometry(QRect(59, 821, 60, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.empAddress.setFont(font)
        self.empAddress.setObjectName("empAddress")

        self.emp_address = QLabel(self.widget3)
        self.emp_address.setGeometry(QRect(120, 820, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emp_address.setFont(font)
        self.emp_address.setObjectName("emp_address")

        self.empDate = QLabel(self.widget3)
        self.empDate.setGeometry(QRect(15, 846, 106, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.empDate.setFont(font)
        self.empDate.setObjectName("empDate")

        self.emp_date = QLabel(self.widget3)
        self.emp_date.setGeometry(QRect(120, 846, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emp_date.setFont(font)
        self.emp_date.setObjectName("emp_date")

        self.empContactNo = QLabel(self.widget3)
        self.empContactNo.setGeometry(QRect(36, 871, 84, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.empContactNo.setFont(font)
        self.empContactNo.setObjectName("empContactNo")

        self.emp_cn = QLabel(self.widget3)
        self.emp_cn.setGeometry(QRect(120, 871, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emp_cn.setFont(font)
        self.emp_cn.setObjectName("emp_cn")

        self.empEmail = QLabel(self.widget3)
        self.empEmail.setGeometry(QRect(77, 896, 41, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.empEmail.setFont(font)
        self.empEmail.setObjectName("empEmail")

        self.emp_email = QLabel(self.widget3)
        self.emp_email.setGeometry(QRect(120, 895, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emp_email.setFont(font)
        self.emp_email.setObjectName("emp_email")

        self.contactPerson = QLabel(self.widget3)
        self.contactPerson.setGeometry(QRect(2, 936, 262, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.contactPerson.setFont(font)
        self.contactPerson.setObjectName("contactPerson")

        self.cpName = QLabel(self.widget3)
        self.cpName.setGeometry(QRect(43, 961, 47, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cpName.setFont(font)
        self.cpName.setObjectName("cpName")

        self.cp_name = QLabel(self.widget3)
        self.cp_name.setGeometry(QRect(90, 961, 64, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cp_name.setFont(font)
        self.cp_name.setObjectName("cp_name")

        self.cpAddress = QLabel(self.widget3)
        self.cpAddress.setGeometry(QRect(29, 986, 60, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cpAddress.setFont(font)
        self.cpAddress.setObjectName("cpAddress")

        self.cp_address = QLabel(self.widget3)
        self.cp_address.setGeometry(QRect(90, 985, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cp_address.setFont(font)
        self.cp_address.setObjectName("cp_address")

        self.cpContactNo = QLabel(self.widget3)
        self.cpContactNo.setGeometry(QRect(10, 1011, 80, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cpContactNo.setFont(font)
        self.cpContactNo.setObjectName("cpContactNo")

        self.cp_cn = QLabel(self.widget3)
        self.cp_cn.setGeometry(QRect(90, 1011, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cp_cn.setFont(font)
        self.cp_cn.setObjectName("cp_cn")

        self.opDrName = QLabel(self.widget3)
        self.opDrName.setGeometry(QRect(10, 1041, 168, 16))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.opDrName.setFont(font)
        self.opDrName.setObjectName("opDrName")

        self.opdr_name = QLabel(self.widget3)
        self.opdr_name.setGeometry(QRect(180, 1041, 63, 13))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.opdr_name.setFont(font)
        self.opdr_name.setObjectName("opdr_name")

        # Create showBtn inside widget3
        self.showBtn = QPushButton(self.widget3)
        self.showBtn.setGeometry(QRect(380, 1060, 41, 23))
        self.showBtn.setObjectName("showBtn")
        self.showBtn.setText("Show")

        # Create ageInput inside widget3
        self.inputId = QLineEdit(self.widget3)
        self.inputId.setGeometry(QRect(380, 1100, 21, 20))
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.inputId.setFont(font)
        self.inputId.setText("")
        self.inputId.setObjectName("ageInput")

        ###########################

        self.verticalLayout_2.addWidget(self.widget3)

        # Set scrollArea widget to scrollAreaWidgetContents
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(ProfileTab)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.profileHeading.setText(_translate("ProfileTab", "MEMBER INFORMATION"))
        self.headingLabel.setText(_translate("ProfileTab",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">#34 Legend St. Village East Cainta, Rizal</span></p><p align=\"center\"><span style=\" font-size:9pt;\">(02) 8400-8066 / (02) 8470-7475</span></p><p align=\"center\"><span style=\" font-size:9pt;\">09171829430 / 09985609443</span></p><p align=\"center\"><span style=\" font-size:9pt;\">ofw.transport.cooperative@gmail.com </span></p><p align=\"center\"><span style=\" font-size:9pt;\">Registration No.: 9520-16021151</span></p><p align=\"center\"><span style=\" font-size:9pt;\">Ammendment No.: 9520-16021151-5</span></p></body></html>"))
        self.dateRegistered.setText(_translate("ProfileTab", "Date Registered:"))
        self.ofwName.setText(_translate("ProfileTab", "OFW Name:"))
        self.ofwAddress.setText(_translate("ProfileTab", "Address:"))
        self.name.setText(_translate("ProfileTab", "Name:"))
        self.address.setText(_translate("ProfileTab", "Address:"))
        self.pob.setText(_translate("ProfileTab", "Place of Birth:"))
        self.pAddress.setText(_translate("ProfileTab", "Provincial Address:"))
        self.dob.setText(_translate("ProfileTab", "Date of Birth:"))
        self.age.setText(_translate("ProfileTab", "Age:"))
        self.sex.setText(_translate("ProfileTab", "Sex:"))
        self.religion.setText(_translate("ProfileTab", "Religion:"))
        self.contactNo.setText(_translate("ProfileTab", "Contact No:"))
        self.email.setText(_translate("ProfileTab", "Email:"))
        self.tinNo.setText(_translate("ProfileTab", "TIN No.:"))
        self.citizenship.setText(_translate("ProfileTab", "Citizenship:"))
        self.status.setText(_translate("ProfileTab", "Civil Status:"))
        self.sssNo.setText(_translate("ProfileTab", "SSS No.:"))
        self.hwName.setText(_translate("ProfileTab", "Husband/Wife Name:"))
        self.hwPob.setText(_translate("ProfileTab", "Place of Birth:"))
        self.hwDob.setText(_translate("ProfileTab", "Date of Birth:"))
        self.hwAge.setText(_translate("ProfileTab", "Age:"))
        self.occupation.setText(_translate("ProfileTab", "Occupation:"))
        self.children.setText(_translate("ProfileTab", "Children"))
        self.employerInfo.setText(_translate("ProfileTab", "Employer Information:"))
        self.empName.setText(_translate("ProfileTab", "Name:"))
        self.position.setText(_translate("ProfileTab", "Position:"))
        self.empAddress.setText(_translate("ProfileTab", "Address:"))
        self.empDate.setText(_translate("ProfileTab", "Date Employed:"))
        self.empContactNo.setText(_translate("ProfileTab", "Contact No.:"))
        self.empEmail.setText(_translate("ProfileTab", "Email:"))
        self.contactPerson.setText(_translate("ProfileTab", "Person to contact in case of Emergency:"))
        self.cpName.setText(_translate("ProfileTab", "Name:"))
        self.cpAddress.setText(_translate("ProfileTab", "Address:"))
        self.cpContactNo.setText(_translate("ProfileTab", "Contact No:"))
        self.opDrName.setText(_translate("ProfileTab", "Operator or Driver Name:"))



    def creatingTables(self):
        self.tableWidget = QTableWidget(self.widget3)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setMinimumWidth(753)
        self.tableWidget.setFixedHeight(132)

        self.tableWidget.setHorizontalHeaderLabels(["Name", "Address", "Age"])

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setMinimumSectionSize(246)

        self.tableWidget.move(0, 578)

