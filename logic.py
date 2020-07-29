from main_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QTableWidgetItem
import shutil
import ast
import os
from db_logic import create_connection, execute_query, execute_read_query
from profile_tab_ui import ProfileUI
from registration_tab_ui import RegistrationUI
from home_tab_ui import HomeTabUI
from TabButtonWidget import TabButtonWidget
from custom_widget import CustomWidget
from custom_list_item import CustomListItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSlot

class MyUi(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow(self)

        self.homeTab = HomeTabUI(self.ui.tab1)
        self.registration = RegistrationUI(self.ui.tab2)
        self.profile = ProfileUI(self.ui.tab3)

        self.connection = create_connection("localhost", "root", "", "ofwtmc_db")
        select_members = "SELECT id, mem_name, mem_address, contact_no FROM members"
        self.members_data = execute_read_query(self.connection, select_members)

        self.getMembersData()

        self.right = self.ui.tabWidget.tabBar().RightSide

        self.save_registration_tab = self.ui.tabWidget.widget(1)  # save it for later
        self.save_profile_tab = self.ui.tabWidget.widget(2)  # save Member Profile Tab for later
        self.removeRegistrationTab()
        self.removeMemberProfileTab()

        # Create actionsDict
        actionsDict = {
                       self.ui.menuHome: "Home",
                       self.ui.actionNew: "New",
                       self.ui.actionSave: "Save",
                       self.ui.actionCut: "Cut",
                       self.ui.actionCopy: "Copy",
                       self.ui.actionPaste: "Paste",
                       self.ui.actionPreview: "Preview"
                       }

        self.childrenData = []

        self.id = self.profile.inputId


        self.date = self.registration.dateInput
        self.id_picture = self.registration.filenameText
        self.ofw_name = self.registration.ofwNameInput
        self.ofw_address = self.registration.ofwAddressInput
        self.b_name = self.registration.beneficiaryNameInput
        self.b_address = self.registration.beneficiaryAddresInput
        self.pob = self.registration.placeOfBirthInput
        self.province_add = self.registration.provincialAddressInput
        self.religion = self.registration.religionInput
        self.contact_no = self.registration.contactInput
        self.email = self.registration.emailAddInput
        self.age = self.registration.ageInput
        self.status = self.registration.civilStatusInput
        self.citizenship = self.registration.citizenshipInput
        self.tin = self.registration.tinInput
        self.sss = self.registration.sssInput
        self.hw_name = self.registration.hwNameInput
        self.hw_pob = self.registration.hwPlaceOfBirthInput
        self.hw_occupation = self.registration.hwOccupationInput
        self.hw_dob = self.registration.hwDateOfBirthInput
        self.hw_age = self.registration.hwAgeInput
        self.emp_name = self.registration.empNameInput
        self.emp_position = self.registration.empPositionInput
        self.emp_address = self.registration.empAddressInput
        self.emp_date = self.registration.empDateInput
        self.emp_cn = self.registration.empContactInput
        self.emp_email = self.registration.empEmailInput
        self.incase_name = self.registration.incaseNameInput
        self.incase_contact = self.registration.incaseContactInput
        self.incase_address = self.registration.incaseContactInput
        self.dob = self.registration.dateOfBirthInput
        self.op_dr_name = self.registration.opOrDriverInput

        self.sex = self.getSRBtn()
        self.ch1_name, self.ch1_address, self.ch1_age = self.getChildData(0)
        self.ch2_name, self.ch2_address, self.ch2_age = self.getChildData(1)
        self.ch3_name, self.ch3_address, self.ch3_age = self.getChildData(2)

        #self.registration_inputs = {self.date, self.id_picture, self.ofw_address, self.b_name,
         #                                self.b_address, self.pob, self.province_add, self.religion,
          #                               self.contact_no, self.email, self.age, self.status,
          #                               self.hw_name, self.hw_pob, self.hw_dob, self.hw_age, self.hw_occupation,
           #                              self.emp_name, self.emp_position, self.emp_address,self.emp_date, self.emp_cn,
           #                              self.emp_email, self.incase_name, self.incase_address, self.incase_contact,
             #                            self.op_dr_name, self.id_picture}


        # Iterate on actionsDict.items then call updateClick
        for action, actionName in actionsDict.items():
            self.updateClick(action, actionName)

        # Call the openFileNameDialog when fileSelectBtn is clicked
        self.registration.fileSelectBtn.clicked.connect(self.openFileNameDialog)

        # Call the uploadBtnClicked when uploadBtn is clicked
        self.registration.uploadBtn.clicked.connect(self.uploadBtnClicked)

        self.registration.submitBtn.clicked.connect(self.submitPopup)

        self.registration.msgBox.buttonClicked.connect(self.saveFileDialog)

        self.registration.comboBox.activated.connect(self.comboPressed)

        self.registration.chAddBtn.clicked.connect(self.addChildren)

        self.profile.showBtn.clicked.connect(self.LoadData)

        self.homeTab.register_btn.clicked.connect(self.showRegistration)

        self.homeTab.member_profiles_btn.clicked.connect(self.showMemberProfile)

        self.homeTab.listwidget.itemClicked.connect(self.LoadData)

        self.homeTab.search_input.textChanged.connect(self.inputChecker)

        self.homeTab.comboBox.currentTextChanged.connect(self.getMembersData)

    # Set the clickLabel text to passed text argument
    # and adjust the size of the text
    def clicked(self, text):
        self.registration.clickLabel.setText(text)
        self.registration.clickLabel.show()
        self.registration.clickLabel.adjustSize()

    # Call an action and
    def updateClick(self, action, action_name):
            #if action_name == "Home":
            #    action.triggered.connect(self.ui.showHomeWindow)
            action.triggered.connect(lambda: self.clicked(f"{action_name} was clicked!"))

    # Shows an openFileNameDialog when called and set text of filenameText to file
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, "Choose an image file", "/Users/Jun/Documents",
                                                "All (*);;JPEG (*.jpg);;PNG (*.png)", options=options)
        if file:
            self.filePath = file
            filteredName = self.fileNAmeFilter(file)
            self.registration.filenameText.setText(filteredName)


    # Get the filepath inside filenameText and update imgDefault Pixmap to filepath
    def uploadBtnClicked(self):
        fileName = self.registration.filenameText.text()
        if fileName and self.filePath:
            # Copy a file with new name
            shutil.copy(self.filePath, 'img/'+fileName)
            self.registration.imgDefault.setPixmap(QtGui.QPixmap('img/'+fileName))

    def submitPopup(self):
        self.registration.msgBox.exec_()

    def savePopup(self):
        self.registration.savedBox.exec_()

    def comboPressed(self):
        currentText = self.registration.comboBox.currentText()

        if (currentText != "Member"):
            if (currentText == "Operator"):
                self.registration.opOrDriverLabel.setText("Driver name:")
                self.registration.opOrDriverLabel.move(403, 537)
            else:
                self.registration.opOrDriverLabel.setText("Operator name:")
                self.registration.opOrDriverLabel.move(386, 537)

            self.registration.opOrDriverLabel.show()
            self.registration.opOrDriverLabel.adjustSize()
            self.registration.opOrDriverInput.show()

        else:
            self.registration.opOrDriverLabel.hide()
            self.registration.opOrDriverInput.hide()

    def saveFileDialog(self):
        self.registration.msgBox.close()

        ###############
        #DB UPDATE
        ######

        new_member = f"""
        INSERT INTO
          `members` 
            (`date`, `ofw_name`, `ofw_address`, `mem_name`, `mem_address`,
             `place_of_birth`, `provincial_address`, `date_of_birth`, `age`,
             `sex`, `religion`, `contact_no`, `email`, `tin`, `sss`, `citizenship`,
             `civil_status`, `hw_name`, `hw_place_of_birth`, `hw_date_of_birth`,
             `hw_age`, `occupation`, `ch1_name`, `ch1_address`, `ch1_age`, `ch2_name`,
             `ch2_address`, `ch2_age`, `ch3_name`, `ch3_address`, `ch3_age`, `emp_name`,
             `emp_position`, `emp_address`, `emp_date`, `emp_contact`, `emp_email`,
             `incase_name`, `incase_address`, `incase_contact_no`, `op_dr_name`, `id_picture`)
        VALUES
          ('{self.convertDateFormat(self.date.text())}', '{self.ofw_name.text()}', '{self.ofw_address.text()}', '{self.b_name.text()}', '{self.b_address.text()}', '{self.pob.text()}', '{self.province_add.text()}', '{self.convertDateFormat(self.dob.text())}', '{self.age.text()}',
           '{self.sex}', '{self.religion.text()}', '{self.contact_no.text()}', '{self.email.text()}', '{self.tin.text()}', '{self.sss.text()}', '{self.citizenship.text()}', '{self.status.text()}', '{self.hw_name.text()}',
           '{self.hw_pob.text()}', '{self.convertDateFormat(self.hw_dob.text())}', '{self.hw_age.text()}', '{self.hw_occupation.text()}', '{self.ch1_name}', '{self.ch1_address}', '{self.ch1_age}', '{self.ch2_name}',
           '{self.ch2_address}', '{self.ch2_age}', '{self.ch3_name}', '{self.ch3_address}', '{self.ch3_age}', '{self.emp_name.text()}', '{self.emp_position.text()}', '{self.emp_address.text()}',
           '{self.convertDateFormat(self.emp_date.text())}', '{self.emp_cn.text()}', '{self.emp_email.text()}', '{self.incase_name.text()}', '{self.incase_address.text()}', '{self.incase_contact.text()}', '{self.op_dr_name.text()}', '{self.id_picture.text()}');
        """

        update_row = f"""
        UPDATE
          members
        SET
          mem_name = '{self.b_name.text()}', mem_address = '{self.b_address.text()}'
        WHERE
          id = '{self.id.text()}'
        """
        execute_query(self.connection, new_member)

        self.getMembersData()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save file as", "/Users/Jun/Documents/members",
                                                  "All Files (*);;Word Documents (*.docx)", options=options)
        if fileName:
            filteredName = self.fileNAmeFilter(fileName)
            self.registration.savedBox.setText(f"{filteredName} saved sucessfully!")
            self.savePopup()

    def fileNAmeFilter(self, text):
        index = text.rfind('/') + 1
        fileName = text[index:]

        return fileName

    def getSRBtn(self):
        sex_input = ''
        if self.registration.maleRBtn.isChecked():
            sex_input = self.registration.maleRBtn.text()
        elif self.registration.femaleRBtn.isChecked():
            sex_input = self.registration.femaleRBtn.text()
        return sex_input

    def convertDateFormat(self, date):
        if date:
            date_ = date.split('/')
            month = date_[0]
            day = date_[1]
            year = date_[2]
            new_date = f"{year}-{month}-{day}"
            return new_date

    ######################################################################
    #########################   DATABASE  ################################

    def DataConverter(self, mydata):
        def cvt(data):
            try:
                return ast.literal_eval(data)
            except Exception:
                return str(data)

        return tuple(map(cvt, mydata))

    def LoadData(self, item):
        select_member = f"""
                        SELECT
                            id_picture, date, ofw_name, ofw_address, mem_name, mem_address, place_of_birth, provincial_address,
                            date_of_birth, age, sex, religion, contact_no, email, tin, sss, citizenship, civil_status,
                            hw_name, hw_place_of_birth, hw_date_of_birth, hw_age, occupation, emp_name, emp_position,
                            emp_address, emp_date, emp_contact, emp_email, incase_name, incase_address, incase_contact_no,
                            op_dr_name, ch1_name, ch1_address, ch1_age, ch2_name, ch2_address, ch2_age, ch3_name,
                            ch3_address, ch3_age
                        FROM
                            members
                        WHERE
                            id = '{item.data(100)}'
                        """
        members = execute_read_query(self.connection, select_member)

        for member in members:
            self.showData(self.DataConverter(member), self.profile.imgDefault, self.profile.date_registered, self.profile.ofw_name, self.profile.ofw_address, self.profile.name_, self.profile.address_,
                       self.profile.pob_, self.profile.p_address, self.profile.dob_, self.profile.age_, self.profile.sex_, self.profile.religion_,
                       self.profile.contact_no, self.profile.email_, self.profile.tin_no, self.profile.sss_no, self.profile.citizenship_, self.profile.status_,
                       self.profile.hw_name, self.profile.hw_pob, self.profile.hw_dob, self.profile.hw_age, self.profile.occupation_,
                       self.profile.emp_name, self.profile.position_, self.profile.emp_address, self.profile.emp_date, self.profile.emp_cn, self.profile.emp_email, self.profile.cp_name,
                       self.profile.cp_address, self.profile.cp_cn, self.profile.opdr_name)

        self.showMemberProfile()

    def showData(self, datas, *labels):
        print("showData")
        for i, data in enumerate(datas):
            if i == datas.index(datas[0]):
               imgFile = os.path.isfile(f'img/{data}')
               if data and imgFile:
                labels[i].setPixmap(QPixmap(f'img/{data}'))
               else:
                labels[i].setPixmap(QPixmap('img/default_avatar.png'))
            elif i in range(33, 42):
                if i in range(33, 36):
                    for column, index in enumerate(range(33, 36)):
                        row = 0
                        self.profile.tableWidget.setItem(row, column, QTableWidgetItem(str(datas[index])))
                elif i in range(36, 39):
                    for column, index in enumerate(range(36, 39)):
                        row = 1
                        self.profile.tableWidget.setItem(row, column, QTableWidgetItem(str(datas[index])))
                else:
                    for column, index in enumerate(range(39, 42)):
                        row = 2
                        self.profile.tableWidget.setItem(row, column, QTableWidgetItem(str(datas[index])))
            else:
                labels[i].setText(str(data))
                labels[i].adjustSize()

    def addChildren(self):
        if len(self.childrenData) < 3:
            child_data = []
            if self.registration.chNameInput.text():
                child_data.append(self.registration.chNameInput.text())
            if self.registration.chAddressInput.text():
                child_data.append(self.registration.chAddressInput.text())
            if self.registration.chAgeInput.text():
                child_data.append(int(self.registration.chAgeInput.text()))
            self.registration.chNameInput.clear()
            self.registration.chAddressInput.clear()
            self.registration.chAgeInput.clear()
            self.childrenData.append(child_data)

    def getChildData(self, index):
        name = ''
        address = ''
        age = ''
        if self.childrenData and self.childrenData[index]:
            if self.childrenData[index][0]:
                name = self.childrenData[index][0]
            if self.childrenData[index][1]:
                address = self.childrenData[index][1]
            if self.childrenData[index][2]:
                age = self.childrenData[index][2]

        return name, address, age

    def showRegistration(self):
        index = 1
        self.registration_cls_btn = TabButtonWidget()
        self.registration_cls_btn.button_remove.clicked.connect(self.removeRegistrationTab)
        if self.save_registration_tab2:
            self.save_registration_tab = self.save_registration_tab2
        elif self.ui.tabWidget.widget(index):
            index = 2
        self.ui.tabWidget.insertTab(index, self.save_registration_tab2, 'Registration')  # restore Member Profile Tab
        self.ui.tabWidget.tabBar().setTabButton(index, self.right, self.registration_cls_btn)
        self.ui.tabWidget.setCurrentIndex(index)

    def removeRegistrationTab(self):
        self.save_registration_tab2 = self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(self.save_registration_tab)) # save it for later
        self.ui.tabWidget.removeTab(self.ui.tabWidget.indexOf(self.save_registration_tab))
        self.registration_cls_btn2 = TabButtonWidget()

    def showMemberProfile(self):
        index = 1
        self.profile_cls_btn = TabButtonWidget()
        if self.save_profile_tab2:
            self.save_profile_tab = self.save_profile_tab2
        elif self.ui.tabWidget.widget(index):
            index = 2
        self.ui.tabWidget.insertTab(index, self.save_profile_tab2, 'Member Profile')  # restore Member Profile Tab
        self.ui.tabWidget.tabBar().setTabButton(index, self.right, self.profile_cls_btn)
        self.ui.tabWidget.setCurrentIndex(index)
        self.profile_cls_btn.button_remove.clicked.connect(self.removeMemberProfileTab)

    def removeMemberProfileTab(self):
        self.save_profile_tab2 = self.ui.tabWidget.widget(self.ui.tabWidget.indexOf(self.save_profile_tab))
        self.ui.tabWidget.removeTab(self.ui.tabWidget.indexOf(self.save_profile_tab))
        self.profile_cls_btn = TabButtonWidget()

    def getMembersData(self):
        select_members = f"SELECT id, mem_name, mem_address, date FROM members ORDER BY {self.comboGetCurrentText()};"
        members_data = execute_read_query(self.connection, select_members)
        self.list_widget = self.homeTab.listwidget

        if self.list_widget.count() > 0:
            self.list_widget.clear()
        for multi_datas in members_data:
            list_item = CustomListItem()
            custom_widget = CustomWidget()
            data = self.DataConverter(multi_datas)
            list_item.setData(100, data[0])
            list_item.setSizeHint(custom_widget.sizeHint())
            #list_item.setData(101, self.getYear(str(data[3])))
            #list_item.setData(102, self.getMonth(str(data[3])))
            #list_item.setData(103, self.getDay(str(data[3])))
            #list_item.setData(104, data[1])

            custom_widget.setNameLabel(data[1])
            custom_widget.setAddressLabel(data[2])
            custom_widget.setDateLabel(data[3])

            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, custom_widget)


        #self.list_widget.setSortingEnabled(True)
        #self.list_widget.sortItems(Qt.DescendingOrder)

        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item_widget = self.list_widget.itemWidget(item)
            item_widget.setOrderNo(i)

        self.homeTab.listwidget.setStyleSheet("QListWidget {font-family: Verdana, Geneva, sans-serif;}" "QListWidget.item:hover {color: white; background: blue;}")

    def search(self, search_results):
        self.list_widget.clear()
        if search_results:
            for i, result in enumerate(search_results):
                list_item = CustomListItem()
                custom_widget = CustomWidget()
                result_data = self.DataConverter(result)

                custom_widget.setOrderNo(i)
                custom_widget.setNameLabel(result_data[1])
                custom_widget.setAddressLabel(result_data[2])
                custom_widget.setDateLabel(result_data[3])

                self.list_widget.addItem(list_item)
                self.list_widget.setItemWidget(list_item, custom_widget)

    def comboGetCurrentText(self):
        currentText = self.homeTab.comboBox.currentText()
        if currentText == 'Date':
            return 'date DESC, mem_name ASC;'
        elif currentText == 'Name':
            return 'mem_name ASC'

    def inputChecker(self):

        if self.homeTab.search_input.text():
            search_query = f"SELECT id, mem_name, mem_address, date FROM members WHERE mem_name REGEXP '{self.homeTab.search_input.text()}+'"
            self.search_results = execute_read_query(self.connection, search_query)

            if self.search_results:
                self.search(self.search_results)

            elif not self.search_results:
                self.list_widget.clear()

        elif not self.homeTab.search_input.text():
            self.getMembersData()

    def getYear(self, date):
        date_ = date.split('-')
        year = date_[0]
        return int(year)

    def getMonth(self, date):
        date_ = date.split('-')
        month = date_[1]
        return int(month)

    def getDay(self, date):
        date_ = date.split('-')
        day = date_[2]
        return int(day)