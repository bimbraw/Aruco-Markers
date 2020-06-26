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

    #this is the transformation matrix part
    
    #size_of_marker = 0.053 #5.3 cm
    #res = np.array(ids)
    #p = res.tolist()

    #focal_length = cap.get(3)
    #center = (cap.get(3) / 2, cap.get(4) / 2)
    #camera_matrix = np.array(
    #    [[focal_length, 0, center[0]],
    #     [0, focal_length, center[1]],
    #     [0, 0, 1]], dtype="double"
    #)

    #these_res_corners = np.concatenate(corners, axis=1)
    #dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion

    #these_ref_corners = np.concatenate([refCorners[x] for x in idx], axis=1)

    #success, rotation_vector, translation_vector = cv2.solvePnP(these_res_corners, these_res_corners, camera_matrix,
    # dist_coeffs, flags=cv2.cv2.SOLVEPNP_ITERATIVE)
    #rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
    #rvecs, tvecs, trash = aruco.estimatePoseSingleMarkers(corners, size_of_marker, mtx, dist)
    #print(rotation_matrix)

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
