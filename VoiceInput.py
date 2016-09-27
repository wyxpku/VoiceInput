import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "VoiceInput.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class GetAudio(QtCore.QThread):
	"""docstring for GetAudio"""
	def __init__(self):
		QtCore.QThread.__init__(self)

	def run(self):
		for i in range(1000):
			pass
		return
		
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	"""docstring for MyApp"""
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.start_btn.clicked.connect(self.start)
		self.end_btn.clicked.connect(self.end)
		
	def start(self):
		self.result.append('start\n')
	def end(self):
		self.result.append('end\n')

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
