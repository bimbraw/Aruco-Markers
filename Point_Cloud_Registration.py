import numpy as np

b = []

a = np.array([[[[437. 387.],
                [367. 382.],
                [372. 310.],
                [439. 316.]]]])

x = a[:,:,0,0]
y = a[:,:,0,1]

print(int(x))
print(int(y))

'''
#point cloud registration matlab function
import numpy as np
import statistics

def pt_cloud_registration(pt_cloud_1, pt_cloud_2):
    n1 = pt_cloud_1.shape[0]
    n2 = pt_cloud_2.shape[0]
    avg1 = statistics.mean(pt_cloud_1)
    avg2 = statistics.mean(pt_cloud_2)
    diff1 = pt_cloud_1
    diff2 = pt_cloud_2

    for i in range(1, n1):
        diff1[i, :] = diff1[i, :] - avg1

    for i in range(1, n2):
        diff2[i, :] = diff2[i, :] - avg2

    h = np.zeros(3, 3)
    h_i = np.zeros(3, 3)

    for i in range(1, n1):
        h_i = [[diff1(i, 1) * diff2(i, 1), diff1(i, 1) * diff2(i, 2), diff1(i, 1) * diff2(i, 3)] \
               [diff1(i, 2) * diff2(i, 1), diff1(i, 2) * diff2(i, 2), diff1(i, 2) * diff2(i, 3)] \
               [diff1(i, 3) * diff2(i, 1), diff1(i, 3) * diff2(i, 2), diff1(i, 3) * diff2(i, 3)]]
        h = h + h_i



'''
'''
function[R, T] = ptCloudRegistration(ptCloud1, ptCloud2)
​
% ptCloud1 = c2;
% ptCloud2 = c1;
​
n1 = size(ptCloud1);
n2 = size(ptCloud2);
avg1 = mean(ptCloud1);
avg2 = mean(ptCloud2);
diff1 = ptCloud1;
diff2 = ptCloud2;
​
for i = 1:n1(1)
diff1(i,:) = diff1(i,:) - avg1;
end
​
for i = 1:n2(1)
diff2(i,:) = diff2(i,:) - avg2;
end
​
H = zeros(3, 3);
H_i = zeros(3, 3);
​
for i = 1:n1(1)

H_i = [diff1(i, 1) * diff2(i, 1) diff1(i, 1) * diff2(i, 2) diff1(i, 1) * diff2(i, 3);
...
diff1(i, 2) * diff2(i, 1)
diff1(i, 2) * diff2(i, 2)
diff1(i, 2) * diff2(i, 3);
...
diff1(i, 3) * diff2(i, 1)
diff1(i, 3) * diff2(i, 2)
diff1(i, 3) * diff2(i, 3)];
H = H + H_i;

end
​
delta = [H(2, 3) - H(3, 2) H(3, 1) - H(1, 3) H(1, 2) - H(2, 1)];
G = [trace(H) delta;
delta
' H+H' - trace(H) * eye(3)];
​
[v, d] = eig(G);
[value, location] = max(d(:));
[row, col] = ind2sub(size(d), location);
​
eVector = v(:, col);
​
R = [eVector(1, 1) * eVector(1, 1) + eVector(2, 1) * eVector(2, 1) - eVector(3, 1) * eVector(3, 1) - eVector(4,
                                                                                                             1) * eVector(
    4, 1) 2 * (eVector(2, 1) * eVector(3, 1) - eVector(1, 1) * eVector(4, 1))
     2 * (eVector(2, 1) * eVector(4, 1) + eVector(1, 1) * eVector(3, 1));
...
2 * (eVector(2, 1) * eVector(3, 1) + eVector(1, 1) * eVector(4, 1))
eVector(1, 1) * eVector(1, 1) - eVector(2, 1) * eVector(2, 1) + eVector(3, 1) * eVector(3, 1) - eVector(4, 1) * eVector(
    4, 1)
2 * (eVector(3, 1) * eVector(4, 1) - eVector(1, 1) * eVector(2, 1));
...
2 * (eVector(2, 1) * eVector(4, 1) - eVector(1, 1) * eVector(3, 1))
2 * (eVector(3, 1) * eVector(4, 1) + eVector(1, 1) * eVector(2, 1))
eVector(1, 1) * eVector(1, 1) - eVector(2, 1) * eVector(2, 1) - eVector(3, 1) * eVector(3, 1) + eVector(4, 1) * eVector(
    4, 1)];
​
T = avg2' - R*avg1';
'''
