# Form implementation generated from reading ui file 'tubes2_Algeo.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Tubes2Algeo(object):
    def setupUi(self, Tubes2Algeo):
        Tubes2Algeo.setObjectName("Tubes2Algeo")
        Tubes2Algeo.resize(752, 410)
        self.verticalLayoutWidget = QtWidgets.QWidget(Tubes2Algeo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 158, 287))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.InsertDataset = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InsertDataset.setFont(font)
        self.InsertDataset.setObjectName("InsertDataset")
        self.verticalLayout_2.addWidget(self.InsertDataset)
        self.ChooseFolder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ChooseFolder.setObjectName("ChooseFolder")
        self.verticalLayout_2.addWidget(self.ChooseFolder)
        self.FolderChosen = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.FolderChosen.setFont(font)
        self.FolderChosen.setObjectName("FolderChosen")
        self.verticalLayout_2.addWidget(self.FolderChosen)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InsertImageFile = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InsertImageFile.setFont(font)
        self.InsertImageFile.setObjectName("InsertImageFile")
        self.verticalLayout_3.addWidget(self.InsertImageFile)
        self.ChooseFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ChooseFile.setObjectName("ChooseFile")
        self.verticalLayout_3.addWidget(self.ChooseFile)
        self.FileChosen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.FileChosen.setObjectName("FileChosen")
        self.verticalLayout_3.addWidget(self.FileChosen)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.TakePicture = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.TakePicture.setObjectName("TakePicture")
        self.verticalLayout_3.addWidget(self.TakePicture)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.ClosestImageLabel = QtWidgets.QLabel(Tubes2Algeo)
        self.ClosestImageLabel.setGeometry(QtCore.QRect(500, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClosestImageLabel.setFont(font)
        self.ClosestImageLabel.setObjectName("ClosestImageLabel")
        self.TestImageLabel = QtWidgets.QLabel(Tubes2Algeo)
        self.TestImageLabel.setGeometry(QtCore.QRect(260, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TestImageLabel.setFont(font)
        self.TestImageLabel.setObjectName("TestImageLabel")
        self.TestImage = QtWidgets.QLabel(Tubes2Algeo)
        self.TestImage.setGeometry(QtCore.QRect(260, 150, 151, 141))
        self.TestImage.setObjectName("TestImage")
        self.ClosestImage = QtWidgets.QLabel(Tubes2Algeo)
        self.ClosestImage.setGeometry(QtCore.QRect(500, 150, 151, 141))
        self.ClosestImage.setObjectName("ClosestImage")

        self.retranslateUi(Tubes2Algeo)
        QtCore.QMetaObject.connectSlotsByName(Tubes2Algeo)

    def retranslateUi(self, Tubes2Algeo):
        _translate = QtCore.QCoreApplication.translate
        Tubes2Algeo.setWindowTitle(_translate("Tubes2Algeo", "Form"))
        self.InsertDataset.setText(_translate("Tubes2Algeo", "Insert Dataset"))
        self.ChooseFolder.setText(_translate("Tubes2Algeo", "Choose Folder"))
        self.FolderChosen.setText(_translate("Tubes2Algeo", "No Folder Chosen"))
        self.InsertImageFile.setText(_translate("Tubes2Algeo", "Insert Image File"))
        self.ChooseFile.setText(_translate("Tubes2Algeo", "Choose File"))
        self.FileChosen.setText(_translate("Tubes2Algeo", "No File Chosen"))
        self.label.setText(_translate("Tubes2Algeo", "OR"))
        self.label_2.setText(_translate("Tubes2Algeo", "Take Picture From Camera"))
        self.TakePicture.setText(_translate("Tubes2Algeo", "Take Picture"))
        self.ClosestImageLabel.setText(_translate("Tubes2Algeo", "Closest Image"))
        self.TestImageLabel.setText(_translate("Tubes2Algeo", "Test Image"))
        self.TestImage.setText(_translate("Tubes2Algeo", "<html><head/><body><p><img src=\":/Image/dataset/Aaron Paul22_265.jpg\"/></p></body></html>"))
        self.ClosestImage.setText(_translate("Tubes2Algeo", "<html><head/><body><p><img src=\":/Image/dataset/Aaron Paul22_265.jpg\"/></p></body></html>"))
