
import flask
#import robot

app = flask.Flask(__name__)

@app.route('/')
def landing():
	return flask.render_template('index.html')

@app.route('/move_div', methods=["POST"])
def move_div():
	#if flask.request.method == 'POST':
		if flask.request.form['button'] == 'forward':
			print ('forward!')
#			robot.forward()
		elif flask.request.form['button'] == 'stop':
			print ('stop!')
#			robot.stop()
		elif flask.request.form['button'] == 'left':
			print ('left')
#			robot.left()
		elif flask.request.form['button'] == 'right':
			print ('right')
#			robot.right()
		elif flask.request.form['button'] == 'backward':
			print ('backward')
#			robot.backward()
		else:
			pass	
		return flask.render_template('index.html')

@app.route('/servo_div', methods=['POST'])
def servo_div():
		if flask.request.form['button'] == 'servo left':
			print ('servo left')
#			robot.servo_left()
		elif flask.request.form['button'] == 'servo center':
			print ('servo center')
#			robot.servo_center()
		elif flask.request.form['button'] == 'servo right':
			print ('servo right')
#			robot.servo_right()
		elif flask.request.form['button'] == 'lights':
			print ('lights')
#			robot.lights()
		elif flask.request.form['button'] == 'blinkers':
			print ('blinkers')
#			robot.blinkers()
		else:
			pass
		return flask.render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='80')
