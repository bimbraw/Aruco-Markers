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

    #l = data.shape[0] // 2
    #corners = data[["c1", "c2", "c3", "c4"]].values.reshape(l, 2, 4)
    #c1 = corners[:, :, 0]
    #c2 = corners[:, :, 1]
    #c3 = corners[:, :, 2]
    #c4 = corners[:, :, 3]

    print(type(array))

    #print(corners)
    #print(type(corners))

    #print(len(corners)) # this is 1
    #print(np.shape(corners)) # 1, 1, 4, 2 for 1
    #1st element number of markers
    #2nd - don't know
    #3rd - rows
    #4th - column
    #print(corners[0][0][0])

    q = np.array(corners)

    #print(q[0][0][0][0]) #this doesn't work
    print(q)

    #x = q[:, :, 0, 0]
    #y = q[:, :, 0, 1]

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
