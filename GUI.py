import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import *
#from nltk.corpus import*
#from nltk.book import*
from Functions import generateSentences

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		
		#CSS Styles
		self.setStyleSheet("""
			QWidget {
				background: rgb(253, 224, 255);
			}
			QPushButton { 
				border-radius: 25px; 
				border: 1px solid black;
				background-color: rgb(238, 237, 255);
				font-family: Brush Script MT, Brush Script Std, cursive;
				font-size: 24px;
			}
			QPushButton:hover {
				background-color: rgb(255, 255, 237);
			}
			QLabel {
				border: 1px solid black;
				background: rgb(255, 237, 246);
				font-family: Arial, sans-serif;
				font-size: 14px;
			}
			QComboBox {
				font-family: Brush Script MT, Brush Script Std, cursive;
				font-size: 24px;
				background-color: rgb(238, 237, 255);
			}
			QLineEdit {
				background-color: rgb(255, 255, 237);
				font-family: Brush Script MT, Brush Script Std, cursive;
				font-size: 22px;
				border: 1px solid black;
			}
		""")
		
		corpus = ""

		self.setWindowIcon(QIcon('icon.png'))
		self.setWindowTitle('Simple Sentences')
		self.setGeometry(0, 0, 800, 800)
		
		#GUI Elements from top to bottom, Left to right 
		self.loadButton = QPushButton('Load Corpus', self)
		self.loadButton.move(150, 50)
		self.loadButton.resize(200, 50)
		self.loadButton.clicked.connect(self.loadCorpus)
		
		self.corpusSelect = QComboBox(self)
		self.corpusSelect.addItem('text1')
		self.corpusSelect.addItem('text2')
		self.corpusSelect.move(400, 50)
		self.corpusSelect.resize(200, 50)

		self.corpusExcerpt = QLabel('', self)
		self.corpusExcerpt.move(100, 150)
		self.corpusExcerpt.resize(600, 200)
		self.corpusExcerpt.setAlignment(Qt.AlignCenter)
		
		self.startWord = QLineEdit('Type a Word', self)
		self.startWord.move(100, 400)
		self.startWord.resize(200, 50)
		
		self.sentenceLength = QLineEdit('Type a Number', self)
		self.sentenceLength.move(500, 400)
		self.sentenceLength.resize(200, 50)
		
		self.generatedSentence = QLabel('', self)
		self.generatedSentence.move(200, 500)
		self.generatedSentence.resize(400, 150)
		self.generatedSentence.setAlignment(Qt.AlignCenter)
		
		self.generateButton = QPushButton('Generate', self)
		self.generateButton.move(300, 700)
		self.generateButton.resize(200, 50)
		self.generateButton.clicked.connect(self.generateSentence)
		
	
		self.show()
		
	def loadCorpus(self, s):
		#self.corpusExcerpt.setText(self.corpusSelect.currentText())
		dlg = FileLoader()
		if dlg.exec():
			print("success")
		else:
			print("failure")
		
		
	def generateSentence(self):
		finishedSentence = generateSentences(int(self.sentenceLength.text()), self.startWord.text(), corpus)
		self.generatedSentence.setText(finishedSentence)
		
		
class FileLoader(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('Select Text File')
		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		self.layout = QVBoxLayout()
		message = QLabel("uh oh")
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())