from flask import Flask, render_template, request, redirect, url_for, make_response
import socket
from solution import robotAngles

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def test():
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

if __name__ == '__main__':
    app.run(debug=True)