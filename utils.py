import cv2
import numpy as np

def stackAndShow(dic : dict, height = 600, save = '', winname = 'window'):
    '''
    dict : {'ImageTextOverlay':image_as_numpy_array ...}
    '''
    length = len(dic)
    nStack = round(np.sqrt(length))
    row = []
    finalImg = None    
    for i, (k, v) in enumerate(dic.items()):

        if i % nStack == 0 and i != 0:
            if finalImg  is not None:
                rowstack = np.vstack(row)
                finalImg = np.hstack((finalImg, rowstack))
                
            else:
                finalImg =np.vstack(row)
            row = []
        v = v.astype(float)
        v = (v*255/v.max()).astype(np.uint8)
        if len(v.shape) == 2:
            v = np.stack((v, v, v), axis = 2)
        cv2.rectangle(v, (0, 0), (5 + len(k) * 8, 30), (50, 50, 50), -1)
        cv2.putText(v, k, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        row.append(v)


    rowstack = np.vstack(row)    

    while rowstack.shape[0] != finalImg.shape[0]:
        row.append(np.zeros_like(row[0]))        
        rowstack = np.vstack(row)    

    finalImg = np.hstack((finalImg, rowstack))

    if save != '' and save is not None:
        cv2.imwrite(save, finalImg)
    scaleAndShow(finalImg, winname, height = height)


def scaleAndShow(im, name = 'window', height = None, waitKey = 1):
    def callback(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, y, im[y, x])
    
    cv2.namedWindow(name)
    cv2.setMouseCallback(name,callback)
    if height is not None:
        width = int(im.shape[1]*height/im.shape[0])
        im = cv2.resize(im, (width, height), interpolation= cv2.INTER_NEAREST)
    cv2.imshow(name, im)
    if cv2.waitKey(waitKey) == ord('q'):
        exit()