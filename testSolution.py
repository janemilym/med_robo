import sys
import math
import numpy as np

def robotAngles(x,y,z,l):
    x = float(x)
    y = float(y)
    z = float(z)
    l = float(l)

    T07 = np.array(\
    [[0, -1, 0, x],\
    [1, 0, 0, y],\
    [0, 0, 1, z],\
    [0, 0, 0, 1]])

    theta_1 = math.atan2(y,x)

    d = (x**2 + y**2 + (z-l)**2)**(1/2)
    alpha = math.acos(d / (2 * l))
    beta = math.acos( (l**2 + l**2 - d**2) / (2*l*l) )
    gamma = math.atan2( (z-l), (x**2 + y**2)**(1/2) )

    theta_2 = gamma - alpha
    theta_3 = math.pi - beta

    T01 = np.array(\
    [[math.cos(theta_1), -(math.sin(theta_1)), 0, 0],\
    [math.sin(theta_1), math.cos(theta_1), 0, 0],\
    [0, 0, 1, 0],\
    [0, 0, 0, 1]])

    T_rotate = np.array(\
    [[1, 0, 0, 0],\
    [0, 0, 1, 0],\
    [0, -1, 0, l],\
    [0, 0, 0, 1]])

    T12 = np.array([\
    [math.cos(theta_2), math.sin(theta_2), 0, 0],\
    [-(math.sin(theta_2)), math.cos(theta_2), 0, 0],\
    [0, 0, 1, 0],\
    [0, 0, 0, 1]])
    T02 = np.matmul( np.matmul(T01, T_rotate), T12 )

    T23 = np.array(\
    [[math.cos(theta_3), math.sin(theta_3), 0, l],\
    [-(math.sin(theta_3)), math.cos(theta_3), 0, 0],\
    [0, 0, 1, 0],\
    [0, 0, 0, 1]])
    T03 = np.matmul( T02, T23 )

    T34 = np.array(\
    [[1, 0, 0, l],\
    [0, 1, 0, 0],\
    [0, 0, 1, 0],\
    [0, 0, 0, 1]])
    T04 = np.matmul( T03, T34 )
    
    T47 = np.matmul( np.linalg.inv(T04), T07 )

    theta_5 = math.asin( -T47[2,0] )
    theta_4 = math.acos( (T47[0][0]) / math.cos(theta_5) )
    theta_6 = math.asin( (T47[2][1]) / math.cos(theta_5) )

    angles = [math.degrees(x) for x in [theta_1, theta_2, theta_3, theta_4, theta_5, theta_6]]
    return angles

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 inverse.py [x] [y] [z] [length]")
        sys.exit()
    
    try:
        x_in = float(sys.argv[1])
        y_in = float(sys.argv[2])
        z_in = float(sys.argv[3])
        length = float(sys.argv[4])

        result = inverseSol(x_in, y_in, z_in, length)
        print(result)
    except ValueError:
        print("Error: input args must be numbers")