import sys
from PyQt4 import QtCore, QtGui, uic

from record import Record
from Voice2Text import Voice2Text
import time

qtCreatorFile = "VoiceInput.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
	
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	"""docstring for MyApp"""
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)

		self.lan = 'zh'
		
		self.setupUi(self)
		self.start_btn.clicked.connect(self.start)
		self.end_btn.clicked.connect(self.end)
		
		self.recorder = recordWorker()
		self.translator = transWorker()

		self.connect(self.recorder, QtCore.SIGNAL("newfile(QString)"), self.newfile)
		self.connect(self, QtCore.SIGNAL("end()"), self.recorder.terminate)
		self.connect(self.translator, QtCore.SIGNAL('addcontent(QString)'), self.addcontent)
		self.connect(self, QtCore.SIGNAL("translate(QString)"), self.translator.translate)
		self.connect(self, QtCore.SIGNAL("end()"), self.translator.terminate)

	def start(self):
		if self.zh_radio.isChecked():
			self.lan = 'zh'
		else:
			self.lan = 'en'

		self.recorder.start()
		self.translator.start()
		# print "started!"
		# self.result.append('start\n')
	def end(self):
		# self.result.append('end\n')
		self.emit(QtCore.SIGNAL('end()'))
		# self.recorder.wait()
		return

	def newfile(self, filename):
		print 'new file' + filename
		self.emit(QtCore.SIGNAL('translate(QString)'), filename + '|' + self.lan)

	def addcontent(self, cont):
		self.result.append(cont)

class recordWorker(QtCore.QThread):
	def __init__(self):
		# self.flag = True
		QtCore.QThread.__init__(self)
		# self.stream = self.record.getStream()
		self.record = Record()
	def __del__(self):
		self.wait()

	def run(self):
		count = 0
		while(True):
			count = count + 1
			filename = self.record.record()
			self.emit(QtCore.SIGNAL('newfile(QString)'), filename)
			# time.sleep(1)
		self.terminate()


class transWorker(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)
		self.voice2Text = Voice2Text()

	def __del__(self):
		self.wait()

	# def run(self):
	
	def translate(self, mystr):
		print mystr
		ary = str(mystr).split('|')
		ret = self.voice2Text.translate(ary[0], ary[1])
		print ret
		if ret['err_no'] == 0:
			self.emit(QtCore.SIGNAL('addcontent(QString)'), ret['result'][0])
		else:
			self.emit(QtCore.SIGNAL('addcontent(QString)'), ret['err_msg'])

		return

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
