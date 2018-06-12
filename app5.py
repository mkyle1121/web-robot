import flask
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

def send_to_robot(data):
	msg = json.dumps({'action':data})
	return msg

def from_robot(clientid, userdata, message): # callback for from_robot subscribe needs global response
	global response_from_robot
	data = message.payload.decode()
	data = json.loads(data)
	data = data['action']
	print(data)
	response_from_robot = data




myMQTT = AWSIoTMQTTClient('Web')
myMQTT.configureEndpoint('a111amujev1y9r.iot.us-west-2.amazonaws.com', 8883)
myMQTT.configureCredentials('/home/mike/keys/root-CA.crt', '/home/mike/keys/Web.private.pem.key', '/home/mike/keys/Web.certificate.pem.crt')
myMQTT.configureOfflinePublishQueueing(-1)
myMQTT.configureDrainingFrequency(2)
myMQTT.configureConnectDisconnectTimeout(10)
myMQTT.connect()
myMQTT.subscribe('from_robot', 1, from_robot)




response_from_robot = ''

application = flask.Flask(__name__)

@application.route('/')
def landing():
	return flask.render_template('index.html')

@application.route('/action', methods=["POST"])
def action():
		if flask.request.form['button'] == 'forward':
			print ('forward!')
			myMQTT.publish('to_robot', send_to_robot('forward'), 1)
		elif flask.request.form['button'] == 'stop':
			print ('stop!')
			myMQTT.publish('to_robot', send_to_robot('stop'), 1)
		elif flask.request.form['button'] == 'left':
			print ('left')
			myMQTT.publish('to_robot', send_to_robot('left'), 1)
		elif flask.request.form['button'] == 'right':
			print ('right')
			myMQTT.publish('to_robot', send_to_robot('right'), 1)
		elif flask.request.form['button'] == 'backward':
			print ('backward')
			myMQTT.publish('to_robot', send_to_robot('backward'), 1)
		elif flask.request.form['button'] == 'servo left':
			print ('servo left')
			myMQTT.publish('to_robot', send_to_robot('servo left'), 1)
		elif flask.request.form['button'] == 'servo center':
			print ('servo center')
			myMQTT.publish('to_robot', send_to_robot('servo center'), 1)
		elif flask.request.form['button'] == 'servo right':
			print ('servo right')
			myMQTT.publish('to_robot', send_to_robot('servo right'), 1)
		elif flask.request.form['button'] == 'lights':
			print ('lights')
			myMQTT.publish('to_robot', send_to_robot('lights'), 1)
		elif flask.request.form['button'] == 'blinkers':
			print ('blinkers')
			myMQTT.publish('to_robot', send_to_robot('blinkers'), 1)
		else:
			pass	
		return '', 204

@application.route('/response', methods=["POST"])
def response():
	global response_from_robot
	response_from_robot = ''
	if flask.request.form['button'] == 'voltage':
		print ('voltage')
		myMQTT.publish('to_robot', send_to_robot('voltage'), 1) # sends request to robot
		while response_from_robot == '': # looping until robot responds to callback above
			pass
		print('robot responded')
		response_from_robot = response_from_robot+' volts' # comes from the callback now and adds volts
		return flask.render_template('index.html', voltage=response_from_robot)
	elif flask.request.form['button'] == 'distance':
		print ('distance')
		myMQTT.publish('to_robot', send_to_robot('distance'), 1) # sends request to robot
		while response_from_robot == '': # looping until robot responds to callback above
			pass
		print('robot responded')
		response_from_robot = response_from_robot+' inches' # comes from the callback now and adds volts
		return flask.render_template('index.html', distance=response_from_robot)

