import serial

class Robot:
    def __init__(self, _port="COM11", _baudrate=115200, _timeout=0.1):
        self._port = _port
        self._baudrate = _baudrate
        self._timeout = _timeout
        self.robot = serial.Serial(self._port,self._baudrate,timeout=self._timeout)

    def move(self, joint: int, degree: float):
        deg = int(round(degree,1)*10)
        cmd = '#' + str(joint) + "D" + str(deg) + '\r'
        print(cmd)
        self.robot.write(cmd.encode())

    def resetJoint(self, joint: int):
        cmd = '#' + str(joint) + "RESET" + '\r'
        print(cmd)
        self.robot.write(cmd.encode())
