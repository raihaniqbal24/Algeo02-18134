import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from gui import Ui_Tubes2Algeo
from eigen_gui import Ui_MainWindow

class App(QWidget):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_Tubes2Algeo()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
    
    def calculate(self):
        database_path = self.ui.database_path
        file_path = os.path.relpath(self.ui.file_path[0])
        testPhoto = QPixmap(file_path)
        testPhoto = testPhoto.scaled(150, 150)
        self.ui.TestImage.setPixmap(testPhoto)

    

# def databaseExtractor(database_path, gui):
    # 


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())