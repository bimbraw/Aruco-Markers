import numpy as np
import cv2, PIL, os
from cv2 import aruco
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

    res = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    x1 = (res[0][0][0][0][0], res[0][0][0][0][1])
    x2 = (res[0][0][0][1][0], res[0][0][0][1][1])
    x3 = (res[0][0][0][2][0], res[0][0][0][2][1])
    x4 = (res[0][0][0][3][0], res[0][0][0][3][1])

    print(x1)

    #q = np.array(corners)

    #print(q[0][0][0][0]) #this doesn't work
    #print(q)

    #x = q[0, 0]
    #y = q[0, 1]

    #print(int(x))

    #print(int(y))

    #print(type(corners))
    #print(corners[0][0][0])

    #print(corners)
    #print(corners[0][0])
    #print(*corners[[1]])

    #cv2.putText(gray, '.',)

    cv2.imshow('frame', frame_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    '''
    for i in range(len(ids)):
        c = corners[i][0]
        plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))

    plt.legend()
    plt.show()
    '''
