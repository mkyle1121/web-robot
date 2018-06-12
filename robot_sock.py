import socket
import threading

class Socket(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.address = '0.0.0.0'
		self.port = 8888
		self.conn = socket.socket()
		self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.conn.bind((self.address,self.port))
	def run(self):
		self.conn.listen(5)
		print ('Listening for robot...')
		self.robotsock, self.addr = self.conn.accept()
		print ('Accepted connection')
	def Send(self,data):
		print ('sending {}'.format(data))
		self.robotsock.send(data.encode())

	
