import numpy as np
import matplotlib.pyplot as plt
import math as mt

hi = float(input('Initial Height from the ground: '))
vo = float(input('Magnitude of the Velocity: '))
theta = float(input('given angle above ground in degrees: '))
xa = float(input('Input HORIZONTAL acceleration: '))
ya = float(input('Input VERTICAL ACCELERATION [given that:free fall = -9.8]:' ))

if ya>= 0:
    raise ValueError('The acceleration of the y-component must not be greater than or equal to zero.')
elif hi < 0:
    raise ValueError('The Height must not be less than 0.')
 
def python4(hi,vo,theta,xa,ya):
    A = mt.radians(theta)
    xval = mt.cos(A)
    yval = mt.sin(A)

    t = (mt.sqrt(((vo*yval)**2) - 2*ya*hi) - vo*xval)/ya
    #-------------------------------------------------------------------------

    if t <= 0:
    
        t = (-mt.sqrt(((vo*yval)**2) - 2*ya*hi) - vo*xval)/ya
    
    T = np.arange(0,t,0.01)

    X = (vo*(xval)*T)+(1/2)*xa*(T**2)
    Y = (hi+ vo*(yval)*T)+(1/2)*ya*(T**2)
#-----------------------------------------------------------------------------
    plt.plot(X,Y)
    plt.grid()
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title('Projectile Trajectory')
    plt.show()
    
python4(hi,vo,theta,xa,ya)