import flask
#import robot
import robot_sock
import threading



Robot_Sock = robot_sock.Socket()
Robot_Sock.run()
print ('loading page...')
Robot_Sock.Send('test data')

app = flask.Flask(__name__)

@app.route('/')
def landing():
	return flask.render_template('index.html')

@app.route('/action', methods=["POST"])
def action():
		if flask.request.form['button'] == 'forward':
			print ('forward!')
#			robot.forward()
			Robot_Sock.Send('forward')
		elif flask.request.form['button'] == 'stop':
			print ('stop!')
#			robot.stop()
			Robot_Sock.Send('stop')
		elif flask.request.form['button'] == 'left':
			print ('left')
#			robot.left()
			Robot_Sock.Send('left')
		elif flask.request.form['button'] == 'right':
			print ('right')
#			robot.right()
			Robot_Sock.Send('right')
		elif flask.request.form['button'] == 'backward':
			print ('backward')
#			robot.backward()
			Robot_Sock.Send('backward')
		elif flask.request.form['button'] == 'servo left':
			print ('servo left')
#			robot.servo_left()
			Robot_Sock.Send('servo left')
		elif flask.request.form['button'] == 'servo center':
			print ('servo center')
#			robot.servo_center()
			Robot_Sock.Send('servo center')
		elif flask.request.form['button'] == 'servo right':
			print ('servo right')
#			robot.servo_right()
			Robot_Sock.Send('servo right')
		elif flask.request.form['button'] == 'lights':
			print ('lights')
#			robot.lights())
			Robot_Sock.Send('lights')
		elif flask.request.form['button'] == 'blinkers':
			print ('blinkers')
#			robot.blinkers()
			Robot_Sock.Send('blinkers')
		else:
			pass	
		return '', 204

@app.route('/response', methods=["POST"])
def response():
	if flask.request.form['button'] == 'voltage':
		print ('voltage')
		#Robot_Sock.Send('voltage')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='80')
