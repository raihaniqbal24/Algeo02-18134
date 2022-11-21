import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from gui import Ui_Tubes2Algeo

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tubes2Algeo()
        self.ui.setupUi(self)
        self.show()
    
    def getDatasetPath(self):
        database_path = QFileDialog.getExistingDirectory(None, "Select Folder")
        return database_path
    
    def getFilePath(self):
        file_path = QFileDialog.getOpenFileName(None, "Select File", "", "JPEG Files(*.jpg)")
        return file_path
    
    def calculate(self):
        database_path = self.ui.ChooseFolder.clicked.connect(self.getDatasetPath)
        file_path = self.ui.file_path[0]
        testPhoto = QPixmap(file_path)
        testPhoto = testPhoto.scaled(150, 150)
        self.ui.TestImage.setPixmap(testPhoto)

    

# def databaseExtractor(database_path, gui):
    # 


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())