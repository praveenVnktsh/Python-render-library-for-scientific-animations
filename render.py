

from utils import scaleAndShow
import cv2
import numpy


class Renderer():


    def __init__(self, height = 600, width = 600 ):
        shape = (height, width, 3)

        self.origImage = numpy.ones(shape, dtype=numpy.uint8) * 255


    def putText(self, image, info = {}):
        for i, (k, v) in enumerate(info.items()):
            cv2.putText(image, k + ' : ' + str(v), (10, 20 + i*20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
        return image
    
    def draw(self, image):
        raise NotImplementedError

    def getInfo(self):
        raise NotImplementedError

    def render(self, height = 600, pause = 10):
        image = self.origImage.copy()
        image = self.draw(image)

        image = self.putText(image, self.getInfo())
        scaleAndShow(image, height= height, waitKey = pause)
        return image

if __name__ == "__main__":

    
    def render(image):
        cv2.line(image, (0, 0), (100, 100), (0, 128, 0), 1)
        return image

    r = Renderer(600, 600, render)    

    for i in range(100):
        r.render(info = {'hello' : '00'})


        