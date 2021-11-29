from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
import socket
import serial

from solution import robotAngles
from robot import Robot

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 80))
server_ip = s.getsockname()[0]
s.close()

r = Robot()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    print('file uploaded successfully')

    response = make_response(redirect(url_for('index')))
    return(response)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        x = float(request.form['input_x'])
        y = float(request.form['input_y'])
        z = float(request.form['input_z'])
        l = float(request.form['input_l'])

        angles = robotAngles(x,y,z,l)
        print(angles)
        print("success!")

        response = make_response(redirect(url_for('index')))
        return(response)
    except ValueError:
        print('input must be number')

@app.route('/move', methods=['POST'])
def move():
    try:
        joint = int(request.form['joint'])
        angle = float(request.form['angle'])

        print(joint)
        print(angle)

        r.move(joint - 1,angle)

        response = make_response(redirect(url_for('index')))
        return(response)
    except ValueError:
        print('bad input')

if __name__ == '__main__':
    app.run(debug=True)