from render import Renderer, scaleAndShow
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Object(Renderer):
    def __init__(self, recordLocation = None):
        super().__init__(recordLocation = recordLocation)
        self.its = 0
        self.x = 300
        self.y = 30
        self.vel = 0
        self.points = set()

    def getInfo(self):
        info = {
            'x' : round(self.x, 4),
            'y' : round(self.y, 4),
            'vel' : round(self.vel, 4)
        }
        return info
    

    def plot(self):
        data = np.array(list(self.points))
        plt.scatter(data[:, 0], data[:, 1], )
        plt.show()

    def step(self, dt):
        m = 1
        g = 9.8

        # y = 0.5*g*dt**2
        accel = g
        self.vel += accel*dt
        y = self.y + self.vel*dt

        self.y =  y
        
        self.its += 1
        if self.its % 20 == 0:
            self.points.add((self.x, self.y))

        


    def draw(self, image):
        # x = 100*np.cos(self.i/100) + 200
        # y = 100*np.sin(self.i/100) + 200
        # self.x = x 
        # self.y = y
        
        
        

        for x, y  in self.points:
            cv2.circle(image, (int(x), int(y)), 1, (0, 0, 255), -1)

        cv2.circle(image, (int(self.x), int(self.y)), 5, (0, 255, 0), -1)

        return image



obj = Object(recordLocation = 'obj.mp4')    

for i in range(3000):
    obj.step(0.01)
    if i % 10== 0:
        obj.render(height= 600, pause = 1)


obj.plot()