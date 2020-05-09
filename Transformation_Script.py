import array as arr
import numpy as np

x1 = y1 = z1 = 0
x2 = y2 = z2 = 0
x3 = y3 = z3 = 0
x4 = y4 = z4 = 0

v1 = v2 = v3 = v4 = v5 = v6 = 0
roll = pitch = yaw = surge = sway = heave = 0

point1_c0 = np.array([[x1, y1, z1]]).transpose()
point2_c0 = np.array([[x2, y2, z2]]).transpose()
point3_c0 = np.array([[x3, y3, z3]]).transpose()
point4_c0 = np.array([[x4, y4, z4]]).transpose()

#print(point1_c0)

def build_t(vars):
    roll = vars[1]
    pitch = vars[2]
    yaw = vars[3]
    surge = vars[4]
    sway = vars[5]
    heave = vars[6]

    Rz =

vars = np.array([[v1, v2, v3, v4, v5, v6]])

build_t(vars)






#currently in MATLAB format
'''
>> point1_c0 = [10 10 50]';
>> point2_c0 = [-10 10 50]';
>> point3_c0 = [10 -10 50]';
>> point3_c0 = [10 -10 40]';
>> point3_c0 = [-10 -10 40]';
>> point4_c0 = [-10 -10 40]';
>> point3_c0 = [-10 -10 40]';
>> point3_c0 = [10 -10 40]';
>> vars = [20 30 10 49 58 20];
[ T_c0_c1, invT ] = buildT( vars )
T_c0_c1 =
    0.8138   -0.2552    0.5221   49.0000
    0.2962    0.9551    0.0052   58.0000
   -0.5000    0.1504    0.8529   20.0000
         0         0         0    1.0000
invT =
    0.8138    0.2962   -0.5000  -47.0556
   -0.2552    0.9551    0.1504  -45.8976
    0.5221    0.0052    0.8529  -42.9439
         0         0         0    1.0000
>> [ T_c1_c0, invT ] = buildT( vars )
T_c1_c0 =
    0.8138   -0.2552    0.5221   49.0000
    0.2962    0.9551    0.0052   58.0000
   -0.5000    0.1504    0.8529   20.0000
         0         0         0    1.0000
invT =
    0.8138    0.2962   -0.5000  -47.0556
   -0.2552    0.9551    0.1504  -45.8976
    0.5221    0.0052    0.8529  -42.9439
         0         0         0    1.0000
>> point1_c1 = T_c1_c0*[point1_c0;1];
>> point1_c0 = [point1_c0;1];
>> point2_c0 = [point2_c0;1];
>> point3_c0 = [point3_c0;1];
>> point4_c0 = [point4_c0;1];
>> point2_c1 = T_c1_c0*point2_c0;
>> point3_c1 = T_c1_c0*point3_c0;
>> point4_c1 = T_c1_c0*point4_c0;
>> point5_c0 = [10 0 45];
>> T_c1_c0*point5_c0
Error using  * 
Incorrect dimensions for matrix multiplication. Check that the number of columns in the first matrix matches the number of rows in the second matrix. To
perform elementwise multiplication, use '.*'.
>> point5_c0 = [10 0 45 1]';
>> T_c1_c0*point5_c0
ans =
   80.6325
   61.1976
   53.3791
    1.0000
>> ptCloud1 = [point1_c0 point2_c0 point3_c0 point4_c0]
ptCloud1 =
    10   -10    10   -10
    10    10   -10   -10
    50    50    40    40
     1     1     1     1
>> ptCloud2 = [point1_c1 point2_c1 point3_c1 point4_c1]
ptCloud2 =
   80.6906   64.4146   80.5743   64.2984
   70.7749   64.8509   51.6203   45.6963
   59.1473   69.1473   47.6109   57.6109
    1.0000    1.0000    1.0000    1.0000
>> [ R, T ] = ptCloudRegistration( ptCloud1, ptCloud2 )
Unrecognized function or variable 'ptCloudRegistration'.
>> [ R, T ] = ptCloudRegistration( ptCloud1, ptCloud2 )
Error using  * 
Incorrect dimensions for matrix multiplication. Check that the number of columns in the first matrix matches the number of rows in the second matrix. To
perform elementwise multiplication, use '.*'.
Error in ptCloudRegistration (line 43)
 T = avg2' - R*avg1';
>> [ R, T ] = ptCloudRegistration( ptCloud1', ptCloud2' )
Error using  * 
Incorrect dimensions for matrix multiplication. Check that the number of columns in the first matrix matches the number of rows in the second matrix. To
perform elementwise multiplication, use '.*'.
Error in ptCloudRegistration (line 43)
 T = avg2' - R*avg1';
>> [ R, T ] = ptCloudRegistration( ptCloud1(1:3,:)', ptCloud2(1:3,:)' )
R =
    0.8138   -0.2552    0.5221
    0.2962    0.9551    0.0052
   -0.5000    0.1504    0.8529
T =
   49.0000
   58.0000
   20.0000
>>

function

function [ T, invT ] = buildT( vars )
%BUILDT Summary of this function goes here
%   vars: angles (degrees) and position defining plane location
%       roll, pitch, yaw, x, y, z
​
roll = vars(1);
pitch = vars(2);
yaw = vars(3);
x = vars(4);
y = vars(5);
z = vars(6);
​
Rz = [cosd(roll) -sind(roll) 0;sind(roll) cosd(roll) 0;0 0 1];
Ry = [cosd(pitch) 0 sind(pitch);0 1 0;-sind(pitch) 0 cosd(pitch)];
Rx = [1 0 0;0 cosd(yaw) -sind(yaw);0 sind(yaw) cosd(yaw)];
R = Rz*Ry*Rx;
t = [x;y;z];
T = [R t;0 0 0 1];
invT = [R' -R'*t;0 0 0 1];
​
end

'''