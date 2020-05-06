import numpy as np
import cv2, PIL, os
from cv2 import aruco
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)

fig = plt.figure()
nx = 2
ny = 3
for i in range(1, nx*ny+1):
    ax = fig.add_subplot(ny,nx, i)
    img = aruco.drawMarker(aruco_dict,i-1, 700)
    plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
    ax.axis("off")

plt.savefig("markers_new.pdf")
plt.show()

'''
#create a 4x4 checkerboard
board = aruco.CharucoBoard_create(4, 4, 1, 0.8, aruco_dict)
imboard = board.draw((4000, 4000))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.imshow(imboard, cmap = mpl.cm.gray, interpolation = "nearest")
ax.axis("off")
cv2.imwrite("chessboard.tiff",imboard)

plt.grid()
plt.savefig("markers_checkerboard.pdf")
plt.show()

print("Chessboard printed")
'''