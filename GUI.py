import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import *

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle('Simple Sentences')
		self.setGeometry(0, 0, 800, 800)

		self.corpusSelectLabel = QLabel('Select Corpus', self)
		self.corpusSelectLabel.move(60, 50)
		self.corpusSelectLabel.resize(200, 50)
		self.corpusSelectLabel.setStyleSheet("border-radius: 25px; border: 1px solid black;")
		self.corpusSelectLabel.setFont(QFont("Times", 14, QFont.Bold))
		
		self.corpusSelectLabel.setAlignment(Qt.AlignCenter)
		
		
		self.corpusCombo = QComboBox(self)
		self.corpusCombo.addItem('Text1')
		self.corpusCombo.addItem('Text2')
		#corpusCombo.setFixedWidth(300)
		#corpusCombo.setAlignment(QtCore.Qt.AlignCenter)
		#self.corpusSelectLabel.buddy(corpusCombo)

		self.show()
		
		
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())