from render import Renderer, scaleAndShow
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy

class Pendulum(Renderer):
    def __init__(self, recordLocation = None):
        super().__init__(recordLocation = recordLocation)
        self.ode = scipy.integrate.ode(self.dynamics).set_integrator('vode', nsteps=500, method='bdf')
        self.its = 0
        self.omega = 0
        self.theta = np.pi/2
        self.points = []
        self.l = 100

    def getInfo(self):
        info = {
            'omega' : round(self.omega, 4),
            'theta' : round(self.theta, 4),
            'time' : round(self.ode.t, 4)
        }
        return info
    
    def dynamics(self, t, y):
        g = 9.8
        l = 5
        theta, omega  = y
        dydt = [omega , -(g/l)*np.sin(theta)]
        return dydt

    def plot(self):
        data = np.array(list(self.points))
        plt.plot(data[:, 1])
        plt.figure()
        plt.plot(data[:, 0])
        plt.show()

    def step(self, dt):
        state = [self.theta, self.omega]

        self.ode.set_initial_value(state, 0)
        self.theta, self.omega = self.ode.integrate(self.ode.t + dt) 

        self.its += 1
        if self.its % 1 == 0:
            self.points.append((self.omega, self.theta))

        


    def draw(self, image):

        cv2.line(image, (300, 300), (300 + int(self.l * np.cos(self.theta  + np.pi/2)), 300 + int(self.l * np.sin(self.theta  +np.pi/2))), (0, 255, 0), 1)
        
        for x, y  in self.points:
            cv2.circle(image, (int(x), int(y)), 1, (0, 0, 120), -1)

        cv2.circle(image, (300 + int(self.l * np.cos(self.theta  + np.pi/2)), 300 + int(self.l * np.sin(self.theta  +np.pi/2))), 5, (0, 0, 255), -1)

        return image



obj = Pendulum(recordLocation= 'pendu.mp4')    

for i in range(3000):
    obj.step(0.01)
    if i % 10 == 0:
        obj.render(height= 600, pause = 1)


obj.plot()