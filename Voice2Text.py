import urllib2, base64, json, os
from uuid import getnode as get_mac

class Voice2Text(object):
	"""docstring for Voice2Text"""
	def __init__(self):
		super(Voice2Text, self).__init__()
		# self.arg = arg
		self.format = 'wav'
		self.rate = 8000
		self.channel = 1
		self.cuid = "wyx"
		# self.token = '24.ec8afa69e6ba61bc547478258bacaba3.2592000.1478106702.282335-8671800'
		tokenfile = open('token.txt', 'r')
		self.token = tokenfile.readline()
		tokenfile.close

		self.url = 'http://vop.baidu.com/server_api/?cuid=wyx&token=' + self.token
		

	def translate(self, filename, lan):
		print "Dealling with new file:", filename, ", Language is", lan
		f = open(filename,'rb')
		# speech = base64.b64encode(f.read())
		speech = f.read()
		size = os.path.getsize(filename)
		# print size
		# data = json.dumps({'format': 'wav','rate': 8000,'channel':1,'cuid':'wyx','token': self.token,'speech':speech,'len':size})
		# print data
		header = {
			"Content-Type": "audio/wav;rate=8000",
			"Content-length": size
		}

		# httpHandler = urllib2.HTTPHandler(debuglevel=1)
		# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
		# opener = urllib2.build_opener(httpHandler, httpsHandler)
		# urllib2.install_opener(opener)

		req = urllib2.Request(self.url + '&lan=' + lan)
		req.add_header("Content-Type", "audio/wav;rate=8000")
		req.add_header("Content-length", size)
		req.add_data(speech)
		# print req
		rsp = urllib2.urlopen(req)
		cont = rsp.read().decode('utf-8')
		# print cont
		# print type(cont)
		return json.loads(cont)
		# print type(mydict)
		# return speech
		# return 

if __name__ == '__main__':
	ob = Voice2Text()
	a = ob.translate("2016-10-04_02_04_38.wav", "zh")
	print a
	print a["result"]