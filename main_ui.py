from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, MainWindow):
        super().__init__()

        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(350, 45, 771, 681)

        # Creating size policy for MainWindow
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        # Set size policy for Mainwindow
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(771, 681))
        MainWindow.setMaximumSize(QtCore.QSize(771, 681))

        # Creat centralwidget and its size policy
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        # Set size policy for centralwidget
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(771, 640))
        self.centralwidget.setMaximumSize(QtCore.QSize(771, 640))
        self.centralwidget.setObjectName("centralwidget")

        # Create verticalLayout for centralwidget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create tabWidget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        # Create size policy for tabWidget
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())

        # Set tabWidget size policy
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(771, 640))
        self.tabWidget.setMaximumSize(QtCore.QSize(771, 640))

        # Create tab1 and add it to tabWidget
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tabWidget.addTab(self.tab1, "")

        # Create tab and add it to tabWidget
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab2, "")

        # Create tab_2 and add it to tabWidget
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tabWidget.addTab(self.tab3, "")

        # Add scrollArea inside centralwidget with layout verticalLayout
        self.verticalLayout.addWidget(self.tabWidget)

        # Set centralwidget as Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Create Menus inside MainWindow
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 15))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Create menuHome inside menubar
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")

        # Create menuNew inside menubar
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

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
        # Set statusbar as MainWindow Status Bar
        MainWindow.setStatusBar(self.statusbar)

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
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuView.addAction(self.actionPreview)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OFWTMC MANAGEMENT SYSTEM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Registration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Member Profile"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
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