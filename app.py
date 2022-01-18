from flask import Flask, render_template, request, redirect, url_for, make_response
import socket
import serial
import os

#from solution import robotAngles
from robot import Robot

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadSolution', methods=['POST'])
def uploadSolution():
    f = request.files['solution']
    f.save("solution.py")
    print('solution uploaded successfully')

    response = make_response(redirect(url_for('index')))
    return(response)

@app.route('/uploadScript', methods=['POST'])
def uploadScript():
    f = request.files['script']
    f.save("script.py")
    print('script uploaded successfully')

    response = make_response(redirect(url_for('index')))
    return(response)

@app.route('/calculate', methods=['POST'])
def calculate():

    from testSolution import robotAngles
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

        r = Robot()
        r.move(joint - 1,angle)
        r.exit()

        response = make_response(redirect(url_for('index')))
        return(response)
    except ValueError:
        print('bad input')

# @app.route('/script', methods=['GET','POST'])
# def script():
#     code = request.form.get("code")

#     f = open("script.py", "w")
#     f.write(code)
#     f.close()

#     return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    os.system('py .\script.py')

    response = make_response(redirect(url_for('index')))
    return(response)

if __name__ == '__main__':
    app.run(debug=True)