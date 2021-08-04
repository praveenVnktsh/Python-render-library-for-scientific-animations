from render import Renderer
import cv2
import numpy as np

class Object(Renderer):
    def __init__(self,):
        super().__init__()
        self.i = 0
        self.x = 0
        self.y = 0
        self.prevpoints = [(0, 0)]

    def getInfo(self):
        info = {
            'radius' : 100,
            'x' : round(self.x, 4),
            'y' : round(self.y, 4),
        }
        return info
    
    def draw(self, image):
        x = 100*np.cos(self.i/100) + 200
        y = 100*np.sin(self.i/100) + 200
        self.x = x 
        self.y = y
        self.i += 1
        self.prevpoints.append((int(x), int(y)))

        cv2.line(image, ((int(x), int(y))), (200, 200), (0, 128, 0), 2)
        
        for x, y  in self.prevpoints[::-1]:
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

        return image



obj = Object()    

for i in range(3000):
    obj.render(height= 600, pause = 1)