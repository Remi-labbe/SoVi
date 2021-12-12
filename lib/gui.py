from PyQt5 import QtCore, QtGui, QtWidgets

class Gui(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('../assets/icon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 597)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 701, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.userTab = QtWidgets.QWidget()
        self.userTab.setObjectName("userTab")
        self.frame_2 = QtWidgets.QFrame(self.userTab)
        self.frame_2.setGeometry(QtCore.QRect(10, 120, 301, 161))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.userNomLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        self.userNomLabel.setFont(font)
        self.userNomLabel.setObjectName("userNomLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.userNomLabel)
        self.userNomField = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        self.userNomField.setFont(font)
        self.userNomField.setObjectName("userNomField")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userNomField)
        self.userPrenomLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        self.userPrenomLabel.setFont(font)
        self.userPrenomLabel.setObjectName("userPrenomLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.userPrenomLabel)
        self.userPrenomField = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        self.userPrenomField.setFont(font)
        self.userPrenomField.setObjectName("userPrenomField")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userPrenomField)
        self.userAgeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.userAgeLabel.setObjectName("userAgeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.userAgeLabel)
        self.userAgeField = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.userAgeField.setMinimum(1)
        self.userAgeField.setMaximum(999)
        self.userAgeField.setObjectName("userAgeField")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.userAgeField)
        self.addUserButton = QtWidgets.QPushButton(self.frame_2)
        self.addUserButton.setGeometry(QtCore.QRect(190, 120, 91, 31))
        self.addUserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addUserButton.setObjectName("addUserButton")
        self.frame_3 = QtWidgets.QFrame(self.userTab)
        self.frame_3.setGeometry(QtCore.QRect(320, 10, 371, 361))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 351, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.userInfosMainLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userInfosMainLabel.sizePolicy().hasHeightForWidth())
        self.userInfosMainLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(True)
        self.userInfosMainLabel.setFont(font)
        self.userInfosMainLabel.setObjectName("userInfosMainLabel")
        self.verticalLayout_2.addWidget(self.userInfosMainLabel)
        self.userInfoSelectBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.userInfoSelectBox.setObjectName("userInfoSelectBox")
        self.verticalLayout_2.addWidget(self.userInfoSelectBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.userNameInfosField = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.userNameInfosField.setObjectName("userNameInfosField")
        self.gridLayout.addWidget(self.userNameInfosField, 0, 1, 1, 1)
        self.userAgeInfosLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.userAgeInfosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userAgeInfosLabel.setObjectName("userAgeInfosLabel")
        self.gridLayout.addWidget(self.userAgeInfosLabel, 2, 0, 1, 1)
        self.userFirstNameInfosLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.userFirstNameInfosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userFirstNameInfosLabel.setObjectName("userFirstNameInfosLabel")
        self.gridLayout.addWidget(self.userFirstNameInfosLabel, 1, 0, 1, 1)
        self.userAgeInfosField = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.userAgeInfosField.setObjectName("userAgeInfosField")
        self.gridLayout.addWidget(self.userAgeInfosField, 2, 1, 1, 1)
        self.userFirstNameInfosField = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.userFirstNameInfosField.setObjectName("userFirstNameInfosField")
        self.gridLayout.addWidget(self.userFirstNameInfosField, 1, 1, 1, 1)
        self.userNameInfosLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.userNameInfosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userNameInfosLabel.setObjectName("userNameInfosLabel")
        self.gridLayout.addWidget(self.userNameInfosLabel, 0, 0, 1, 1)
        self.userFollowLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.userFollowLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userFollowLabel.setObjectName("userFollowLabel")
        self.gridLayout.addWidget(self.userFollowLabel, 3, 0, 1, 1)
        self.userFollowListView = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.userFollowListView.setObjectName("userFollowListView")
        self.gridLayout.addWidget(self.userFollowListView, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.deleteUserButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.deleteUserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.verticalLayout_2.addWidget(self.deleteUserButton)
        self.tabWidget.addTab(self.userTab, "")
        self.pageTab = QtWidgets.QWidget()
        self.pageTab.setObjectName("pageTab")
        self.frame = QtWidgets.QFrame(self.pageTab)
        self.frame.setGeometry(QtCore.QRect(320, 10, 371, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 351, 341))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pageInfosLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageInfosLabel.sizePolicy().hasHeightForWidth())
        self.pageInfosLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(True)
        self.pageInfosLabel.setFont(font)
        self.pageInfosLabel.setObjectName("pageInfosLabel")
        self.verticalLayout_6.addWidget(self.pageInfosLabel)
        self.pageInfosSelected = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.pageInfosSelected.setObjectName("pageInfosSelected")
        self.verticalLayout_6.addWidget(self.pageInfosSelected)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pageNameInfosLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.pageNameInfosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pageNameInfosLabel.setObjectName("pageNameInfosLabel")
        self.gridLayout_2.addWidget(self.pageNameInfosLabel, 0, 0, 1, 1)
        self.pageNameInfosField = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageNameInfosField.sizePolicy().hasHeightForWidth())
        self.pageNameInfosField.setSizePolicy(sizePolicy)
        self.pageNameInfosField.setObjectName("pageNameInfosField")
        self.gridLayout_2.addWidget(self.pageNameInfosField, 0, 1, 1, 1)
        self.pageAdminsInfosLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.pageAdminsInfosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pageAdminsInfosLabel.setObjectName("pageAdminsInfosLabel")
        self.gridLayout_2.addWidget(self.pageAdminsInfosLabel, 1, 0, 1, 1)
        self.pageAdminsListView = QtWidgets.QListView(self.verticalLayoutWidget_4)
        self.pageAdminsListView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pageAdminsListView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pageAdminsListView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.pageAdminsListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pageAdminsListView.setItemAlignment(QtCore.Qt.AlignLeading)
        self.pageAdminsListView.setObjectName("pageAdminsListView")
        self.gridLayout_2.addWidget(self.pageAdminsListView, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.addAdminBox = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.addAdminBox.setObjectName("addAdminBox")
        self.verticalLayout_6.addWidget(self.addAdminBox)
        self.addAdminButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.addAdminButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addAdminButton.setObjectName("addAdminButton")
        self.verticalLayout_6.addWidget(self.addAdminButton)
        self.deletePageButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.deletePageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deletePageButton.setObjectName("deletePageButton")
        self.verticalLayout_6.addWidget(self.deletePageButton)
        self.frame_4 = QtWidgets.QFrame(self.pageTab)
        self.frame_4.setGeometry(QtCore.QRect(10, 160, 301, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.pageNameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.pageNameLabel.setObjectName("pageNameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pageNameLabel)
        self.pageNameField = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.pageNameField.setObjectName("pageNameField")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pageNameField)
        self.addPageButton = QtWidgets.QPushButton(self.frame_4)
        self.addPageButton.setGeometry(QtCore.QRect(200, 50, 81, 31))
        self.addPageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addPageButton.setObjectName("addPageButton")
        self.tabWidget.addTab(self.pageTab, "")
        self.viewTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        self.viewTab.setFont(font)
        self.viewTab.setObjectName("viewTab")
        self.arcsListLabel = QtWidgets.QLabel(self.viewTab)
        self.arcsListLabel.setGeometry(QtCore.QRect(380, 10, 251, 17))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(True)
        self.arcsListLabel.setFont(font)
        self.arcsListLabel.setObjectName("arcsListLabel")
        self.arcsView = QtWidgets.QTableView(self.viewTab)
        self.arcsView.setGeometry(QtCore.QRect(380, 78, 301, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arcsView.sizePolicy().hasHeightForWidth())
        self.arcsView.setSizePolicy(sizePolicy)
        self.arcsView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.arcsView.setTabKeyNavigation(False)
        self.arcsView.setProperty("showDropIndicator", False)
        self.arcsView.setDragDropOverwriteMode(False)
        self.arcsView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.arcsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.arcsView.setObjectName("arcsView")
        self.sommetsView = QtWidgets.QTableView(self.viewTab)
        self.sommetsView.setGeometry(QtCore.QRect(10, 80, 311, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sommetsView.sizePolicy().hasHeightForWidth())
        self.sommetsView.setSizePolicy(sizePolicy)
        self.sommetsView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sommetsView.setTabKeyNavigation(False)
        self.sommetsView.setProperty("showDropIndicator", False)
        self.sommetsView.setDragDropOverwriteMode(False)
        self.sommetsView.setShowGrid(True)
        self.sommetsView.setObjectName("sommetsView")
        self.sommetsListFilter = QtWidgets.QComboBox(self.viewTab)
        self.sommetsListFilter.setGeometry(QtCore.QRect(10, 40, 311, 25))
        self.sommetsListFilter.setObjectName("sommetsListFilter")
        self.sommetsListFilter.addItem("")
        self.sommetsListFilter.addItem("")
        self.sommetsListLabel = QtWidgets.QLabel(self.viewTab)
        self.sommetsListLabel.setGeometry(QtCore.QRect(10, 10, 297, 17))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(True)
        self.sommetsListLabel.setFont(font)
        self.sommetsListLabel.setObjectName("sommetsListLabel")
        self.tabWidget.addTab(self.viewTab, "")
        self.infosGraph = QtWidgets.QGroupBox(self.centralwidget)
        self.infosGraph.setGeometry(QtCore.QRect(50, 440, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(11)
        font.setUnderline(False)
        self.infosGraph.setFont(font)
        self.infosGraph.setAutoFillBackground(False)
        self.infosGraph.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.infosGraph.setObjectName("infosGraph")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.infosGraph)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 221, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nbSommetsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(False)
        self.nbSommetsLabel.setFont(font)
        self.nbSommetsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbSommetsLabel.setObjectName("nbSommetsLabel")
        self.horizontalLayout.addWidget(self.nbSommetsLabel)
        self.nbSommetsField = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(False)
        self.nbSommetsField.setFont(font)
        self.nbSommetsField.setObjectName("nbSommetsField")
        self.horizontalLayout.addWidget(self.nbSommetsField)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nbArcLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(False)
        self.nbArcLabel.setFont(font)
        self.nbArcLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nbArcLabel.setObjectName("nbArcLabel")
        self.horizontalLayout_2.addWidget(self.nbArcLabel)
        self.nbArcField = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Medium")
        font.setPointSize(10)
        font.setUnderline(False)
        self.nbArcField.setFont(font)
        self.nbArcField.setObjectName("nbArcField")
        self.horizontalLayout_2.addWidget(self.nbArcField)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.showGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.showGraphButton.setGeometry(QtCore.QRect(430, 460, 171, 61))
        self.showGraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showGraphButton.setObjectName("showGraphButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 729, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuOpen = QtWidgets.QAction(MainWindow)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QAction(MainWindow)
        self.menuSave.setObjectName("menuSave")
        self.menuQuit = QtWidgets.QAction(MainWindow)
        self.menuQuit.setObjectName("menuQuit")
        self.menufile.addAction(self.menuOpen)
        self.menufile.addSeparator()
        self.menufile.addAction(self.menuSave)
        self.menufile.addSeparator()
        self.menufile.addAction(self.menuQuit)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.menuQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.userNomField)
        MainWindow.setTabOrder(self.userNomField, self.userPrenomField)
        MainWindow.setTabOrder(self.userPrenomField, self.userAgeField)
        MainWindow.setTabOrder(self.userAgeField, self.addUserButton)
        MainWindow.setTabOrder(self.addUserButton, self.userInfoSelectBox)
        MainWindow.setTabOrder(self.userInfoSelectBox, self.deleteUserButton)
        MainWindow.setTabOrder(self.deleteUserButton, self.pageNameField)
        MainWindow.setTabOrder(self.pageNameField, self.addPageButton)
        MainWindow.setTabOrder(self.addPageButton, self.pageInfosSelected)
        MainWindow.setTabOrder(self.pageInfosSelected, self.pageAdminsListView)
        MainWindow.setTabOrder(self.pageAdminsListView, self.addAdminBox)
        MainWindow.setTabOrder(self.addAdminBox, self.addAdminButton)
        MainWindow.setTabOrder(self.addAdminButton, self.deletePageButton)
        MainWindow.setTabOrder(self.deletePageButton, self.showGraphButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Social Visualisator"))
        self.userNomLabel.setText(_translate("MainWindow", "Nom :"))
        self.userPrenomLabel.setText(_translate("MainWindow", "Prenom :"))
        self.userAgeLabel.setText(_translate("MainWindow", "Age :"))
        self.addUserButton.setToolTip(_translate("MainWindow", "Add a user with the information in the form."))
        self.addUserButton.setText(_translate("MainWindow", "Ajouter"))
        self.userInfosMainLabel.setText(_translate("MainWindow", "Informations sur l\'utilisateur :"))
        self.userNameInfosField.setText(_translate("MainWindow", "---"))
        self.userAgeInfosLabel.setText(_translate("MainWindow", "Age :"))
        self.userFirstNameInfosLabel.setText(_translate("MainWindow", "Prenom :"))
        self.userAgeInfosField.setText(_translate("MainWindow", "---"))
        self.userFirstNameInfosField.setText(_translate("MainWindow", "---"))
        self.userNameInfosLabel.setText(_translate("MainWindow", "Nom :"))
        self.userFollowLabel.setText(_translate("MainWindow", "Comptes suivis :"))
        self.deleteUserButton.setText(_translate("MainWindow", "Supprimer l\'utilisateur"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userTab), _translate("MainWindow", "Utilisateur"))
        self.pageInfosLabel.setText(_translate("MainWindow", "Informations sur la page :"))
        self.pageNameInfosLabel.setText(_translate("MainWindow", "Nom :"))
        self.pageNameInfosField.setText(_translate("MainWindow", "---"))
        self.pageAdminsInfosLabel.setText(_translate("MainWindow", "Admins :"))
        self.addAdminButton.setText(_translate("MainWindow", "Ajouter un administrateur"))
        self.deletePageButton.setText(_translate("MainWindow", "Supprimer la page"))
        self.pageNameLabel.setText(_translate("MainWindow", "Nom :"))
        self.addPageButton.setText(_translate("MainWindow", "Ajouter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pageTab), _translate("MainWindow", "Page"))
        self.arcsListLabel.setText(_translate("MainWindow", "Liste des arcs :"))
        self.sommetsListFilter.setItemText(0, _translate("MainWindow", "Nom"))
        self.sommetsListFilter.setItemText(1, _translate("MainWindow", "Degre Sortant"))
        self.sommetsListLabel.setText(_translate("MainWindow", "Liste des sommets :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewTab), _translate("MainWindow", "Vue"))
        self.infosGraph.setTitle(_translate("MainWindow", "Informations courantes: "))
        self.nbSommetsLabel.setText(_translate("MainWindow", "Nb. sommets :"))
        self.nbSommetsField.setText(_translate("MainWindow", "0"))
        self.nbArcLabel.setText(_translate("MainWindow", "Nb. Arcs :"))
        self.nbArcField.setText(_translate("MainWindow", "0"))
        self.showGraphButton.setText(_translate("MainWindow", "Afficher le Graphe"))
        self.menufile.setTitle(_translate("MainWindow", "fichier"))
        self.menuOpen.setText(_translate("MainWindow", "Ouvrir"))
        self.menuOpen.setToolTip(_translate("MainWindow", "Open a new file"))
        self.menuOpen.setStatusTip(_translate("MainWindow", "Open a data file"))
        self.menuOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.menuSave.setText(_translate("MainWindow", "Enregistrer"))
        self.menuSave.setToolTip(_translate("MainWindow", "Save to a file"))
        self.menuSave.setStatusTip(_translate("MainWindow", "Save status to file"))
        self.menuSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuQuit.setText(_translate("MainWindow", "Quitter"))
        self.menuQuit.setToolTip(_translate("MainWindow", "Quit the app"))
        self.menuQuit.setStatusTip(_translate("MainWindow", "Quit the app"))
        self.menuQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
