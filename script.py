from robot import Robot
import time

if __name__=='__main__':
 r = Robot()

 r.move(0,0)
 time.sleep(1)

 r.move(0,10)
 time.sleep(1)

 r.exit()