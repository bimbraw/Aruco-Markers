# Support Vector Regression (SVR)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Importing the dataset
dataset_1_u = pd.read_csv('SVM_1_u.csv')
dataset_2_u = pd.read_csv('SVM_2_u.csv')
dataset_3_u = pd.read_csv('SVM_3_u.csv')
dataset_4_u = pd.read_csv('SVM_4_u.csv')
dataset_5_u = pd.read_csv('SVM_5_u.csv')
dataset_6_u = pd.read_csv('SVM_6_u.csv')
dataset_7_u = pd.read_csv('SVM_7_u.csv')
dataset_8_u = pd.read_csv('SVM_8_u.csv')

dataset_1_v = pd.read_csv('SVM_1_v.csv')
dataset_2_v = pd.read_csv('SVM_2_v.csv')
dataset_3_v = pd.read_csv('SVM_3_v.csv')
dataset_4_v = pd.read_csv('SVM_4_v.csv')
dataset_5_v = pd.read_csv('SVM_5_v.csv')
dataset_6_v = pd.read_csv('SVM_6_v.csv')
dataset_7_v = pd.read_csv('SVM_7_v.csv')
dataset_8_v = pd.read_csv('SVM_8_v.csv')

x_1_u = dataset_1_u.iloc[:, 0:-1].values
x_2_u = dataset_2_u.iloc[:, 0:-1].values
x_3_u = dataset_3_u.iloc[:, 0:-1].values
x_4_u = dataset_4_u.iloc[:, 0:-1].values
x_5_u = dataset_5_u.iloc[:, 0:-1].values
x_6_u = dataset_6_u.iloc[:, 0:-1].values
x_7_u = dataset_7_u.iloc[:, 0:-1].values
x_8_u = dataset_8_u.iloc[:, 0:-1].values
x_1_v = dataset_1_v.iloc[:, 0:-1].values
x_2_v = dataset_2_v.iloc[:, 0:-1].values
x_3_v = dataset_3_v.iloc[:, 0:-1].values
x_4_v = dataset_4_v.iloc[:, 0:-1].values
x_5_v = dataset_5_v.iloc[:, 0:-1].values
x_6_v = dataset_6_v.iloc[:, 0:-1].values
x_7_v = dataset_7_v.iloc[:, 0:-1].values
x_8_v = dataset_8_v.iloc[:, 0:-1].values

y_1_u = dataset_1_u.iloc[:, -1].values
y_2_u = dataset_2_u.iloc[:, -1].values
y_3_u = dataset_3_u.iloc[:, -1].values
y_4_u = dataset_4_u.iloc[:, -1].values
y_5_u = dataset_5_u.iloc[:, -1].values
y_6_u = dataset_6_u.iloc[:, -1].values
y_7_u = dataset_7_u.iloc[:, -1].values
y_8_u = dataset_8_u.iloc[:, -1].values
y_1_v = dataset_1_v.iloc[:, -1].values
y_2_v = dataset_2_v.iloc[:, -1].values
y_3_v = dataset_3_v.iloc[:, -1].values
y_4_v = dataset_4_v.iloc[:, -1].values
y_5_v = dataset_5_v.iloc[:, -1].values
y_6_v = dataset_6_v.iloc[:, -1].values
y_7_v = dataset_7_v.iloc[:, -1].values
y_8_v = dataset_8_v.iloc[:, -1].values

y_1_u = y_1_u.reshape(len(y_1_u),1)
y_2_u = y_2_u.reshape(len(y_2_u),1)
y_3_u = y_3_u.reshape(len(y_3_u),1)
y_4_u = y_4_u.reshape(len(y_4_u),1)
y_5_u = y_5_u.reshape(len(y_5_u),1)
y_6_u = y_6_u.reshape(len(y_6_u),1)
y_7_u = y_7_u.reshape(len(y_7_u),1)
y_8_u = y_8_u.reshape(len(y_8_u),1)
y_1_v = y_1_v.reshape(len(y_1_v),1)
y_2_v = y_2_v.reshape(len(y_2_v),1)
y_3_v = y_3_v.reshape(len(y_3_v),1)
y_4_v = y_4_v.reshape(len(y_4_v),1)
y_5_v = y_5_v.reshape(len(y_5_v),1)
y_6_v = y_6_v.reshape(len(y_6_v),1)
y_7_v = y_7_v.reshape(len(y_7_v),1)
y_8_v = y_8_v.reshape(len(y_8_v),1)


# Feature Scaling

from sklearn.preprocessing import StandardScaler
from sklearn import metrics

sc_1_u_x = StandardScaler()
sc_2_u_x = StandardScaler()
sc_3_u_x = StandardScaler()
sc_4_u_x = StandardScaler()
sc_5_u_x = StandardScaler()
sc_6_u_x = StandardScaler()
sc_7_u_x = StandardScaler()
sc_8_u_x = StandardScaler()
sc_1_v_x = StandardScaler()
sc_2_v_x = StandardScaler()
sc_3_v_x = StandardScaler()
sc_4_v_x = StandardScaler()
sc_5_v_x = StandardScaler()
sc_6_v_x = StandardScaler()
sc_7_v_x = StandardScaler()
sc_8_v_x = StandardScaler()
sc_1_u_y = StandardScaler()
sc_2_u_y = StandardScaler()
sc_3_u_y = StandardScaler()
sc_4_u_y = StandardScaler()
sc_5_u_y = StandardScaler()
sc_6_u_y = StandardScaler()
sc_7_u_y = StandardScaler()
sc_8_u_y = StandardScaler()
sc_1_v_y = StandardScaler()
sc_2_v_y = StandardScaler()
sc_3_v_y = StandardScaler()
sc_4_v_y = StandardScaler()
sc_5_v_y = StandardScaler()
sc_6_v_y = StandardScaler()
sc_7_v_y = StandardScaler()
sc_8_v_y = StandardScaler()

#print(x_1_u)

x_1_u = sc_1_u_x.fit_transform(x_1_u)
x_2_u = sc_2_u_x.fit_transform(x_2_u)
x_3_u = sc_3_u_x.fit_transform(x_3_u)
x_4_u = sc_4_u_x.fit_transform(x_4_u)
x_5_u = sc_5_u_x.fit_transform(x_5_u)
x_6_u = sc_6_u_x.fit_transform(x_6_u)
x_7_u = sc_7_u_x.fit_transform(x_7_u)
x_8_u = sc_8_u_x.fit_transform(x_8_u)
x_1_v = sc_1_v_x.fit_transform(x_1_v)
x_2_v = sc_2_v_x.fit_transform(x_2_v)
x_3_v = sc_3_v_x.fit_transform(x_3_v)
x_4_v = sc_4_v_x.fit_transform(x_4_v)
x_5_v = sc_5_v_x.fit_transform(x_5_v)
x_6_v = sc_6_v_x.fit_transform(x_6_v)
x_7_v = sc_7_v_x.fit_transform(x_7_v)
x_8_v = sc_8_v_x.fit_transform(x_8_v)

#print(x_1_u)

y_1_u = sc_1_u_y.fit_transform(y_1_u)
y_2_u = sc_2_u_y.fit_transform(y_2_u)
y_3_u = sc_3_u_y.fit_transform(y_3_u)
y_4_u = sc_4_u_y.fit_transform(y_4_u)
y_5_u = sc_5_u_y.fit_transform(y_5_u)
y_6_u = sc_6_u_y.fit_transform(y_6_u)
y_7_u = sc_7_u_y.fit_transform(y_7_u)
y_8_u = sc_8_u_y.fit_transform(y_8_u)
y_1_v = sc_1_v_y.fit_transform(y_1_v)
y_2_v = sc_2_v_y.fit_transform(y_2_v)
y_3_v = sc_3_v_y.fit_transform(y_3_v)
y_4_v = sc_4_v_y.fit_transform(y_4_v)
y_5_v = sc_5_v_y.fit_transform(y_5_v)
y_6_v = sc_6_v_y.fit_transform(y_6_v)
y_7_v = sc_7_v_y.fit_transform(y_7_v)
y_8_v = sc_8_v_y.fit_transform(y_8_v)


# Training the SVR model on the whole dataset
import sklearn
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

regressor.fit(x_1_u, y_1_u)
regressor.fit(x_2_u, y_2_u)
regressor.fit(x_3_u, y_3_u)
regressor.fit(x_4_u, y_4_u)
regressor.fit(x_5_u, y_5_u)
regressor.fit(x_6_u, y_6_u)
regressor.fit(x_7_u, y_7_u)
regressor.fit(x_8_u, y_8_u)
regressor.fit(x_1_v, y_1_v)
regressor.fit(x_2_v, y_2_v)
regressor.fit(x_3_v, y_3_v)
regressor.fit(x_4_v, y_4_v)
regressor.fit(x_5_v, y_5_v)
regressor.fit(x_6_v, y_6_v)
regressor.fit(x_7_v, y_7_v)
regressor.fit(x_8_v, y_8_v)

y_rbf_1_u = svr_rbf.fit(x_1_u, y_1_u).predict(x_1_u)
y_rbf_2_u = svr_rbf.fit(x_2_u, y_2_u).predict(x_2_u)
y_rbf_3_u = svr_rbf.fit(x_3_u, y_3_u).predict(x_3_u)
y_rbf_4_u = svr_rbf.fit(x_4_u, y_4_u).predict(x_4_u)
y_rbf_5_u = svr_rbf.fit(x_5_u, y_5_u).predict(x_5_u)
y_rbf_6_u = svr_rbf.fit(x_6_u, y_6_u).predict(x_6_u)
y_rbf_7_u = svr_rbf.fit(x_7_u, y_7_u).predict(x_7_u)
y_rbf_8_u = svr_rbf.fit(x_8_u, y_8_u).predict(x_8_u)

y_rbf_1_v = svr_rbf.fit(x_1_v, y_1_v).predict(x_1_v)
y_rbf_2_v = svr_rbf.fit(x_2_v, y_2_v).predict(x_2_v)
y_rbf_3_v = svr_rbf.fit(x_3_v, y_3_v).predict(x_3_v)
y_rbf_4_v = svr_rbf.fit(x_4_v, y_4_v).predict(x_4_v)
y_rbf_5_v = svr_rbf.fit(x_5_v, y_5_v).predict(x_5_v)
y_rbf_6_v = svr_rbf.fit(x_6_v, y_6_v).predict(x_6_v)
y_rbf_7_v = svr_rbf.fit(x_7_v, y_7_v).predict(x_7_v)
y_rbf_8_v = svr_rbf.fit(x_8_v, y_8_v).predict(x_8_v)

# Predicting a new result
df = pd.read_csv("SVM_1_u.csv")
vals = df.values[:,1]
angle_vals = df.values[:,0]
#print(vals[0])

for i in range(0,len(vals)):
    #print(vals[i])
    print(sc_1_u_y.inverse_transform(regressor.predict(sc_1_u_x.transform([[40]]))))

print(sklearn.metrics.r2_score(y_1_u, y_rbf_1_u, multioutput='uniform_average'))

'''
plt.scatter(x_3_u, y_3_u, color='darkorange', label='data')
plt.plot(x_3_u, y_rbf_3_u, color='navy', label='RBF model')
plt.xlabel('Normalized Angle Values')
plt.ylabel('Normalized U coordinate Values')
plt.title('Fittings and data plotting')
plt.legend()
plt.show()
'''
'''
for i in range(0,len(vals)):
    print(str(i) + ". For " + str(angle_vals[i]) +
          " degrees, the value is " + str(vals[i]) +
          " and the prediction is " + str(sc_2_v_y.inverse_transform(regressor.predict
                                                                     (sc_2_v_x.transform([[angle_vals[i]]])))))

#print(y_rbf_1_u)

#sample weight for 6 u
#sample_weight=[1, 0, 1, 0, .1, .1, .1, 0, 1, 0, .1, 1, 0, 1, 0, 1, .1, 1, 1, 1]

#sample weight for new 1u
#sample_weight=[1, 1, 1, .1, .1, .1, .1, 1, .1, .1, .1, 1, 0, .1, .1, 1, .1, 1, 1, 1],

print(len(y_1_u))

#sample weight for 1u
print(sklearn.metrics.r2_score(y_1_u, y_rbf_1_u,
                               sample_weight=[0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                                              1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                               multioutput='uniform_average'))


plt.scatter(x_2_u, y_2_u, color='darkorange', label='data')
plt.plot(x_2_u, y_rbf_2_u, color='navy', label='RBF model')
plt.xlabel('Normalized Angle Values')
plt.ylabel('Normalized U coordinate Values')
plt.title('Fittings and data plotting')
plt.legend()
plt.show()
'''

'''
#print(sc_1_u_y.inverse_transform(regressor.predict(sc_1_u_x.transform([[dataset_1_u]]))))
print(sc_2_u_y.inverse_transform(regressor.predict(sc_2_u_x.transform([[129.6]]))))
print(sc_3_u_y.inverse_transform(regressor.predict(sc_3_u_x.transform([[129.6]]))))
print(sc_4_u_y.inverse_transform(regressor.predict(sc_4_u_x.transform([[129.6]]))))
print(sc_5_u_y.inverse_transform(regressor.predict(sc_5_u_x.transform([[129.6]]))))
print(sc_6_u_y.inverse_transform(regressor.predict(sc_6_u_x.transform([[129.6]]))))
print(sc_7_u_y.inverse_transform(regressor.predict(sc_7_u_x.transform([[129.6]]))))
print(sc_8_u_y.inverse_transform(regressor.predict(sc_8_u_x.transform([[129.6]]))))

print(sc_1_v_y.inverse_transform(regressor.predict(sc_1_v_x.transform([[129.6]]))))
print(sc_2_v_y.inverse_transform(regressor.predict(sc_2_v_x.transform([[129.6]]))))
print(sc_3_v_y.inverse_transform(regressor.predict(sc_3_v_x.transform([[129.6]]))))
print(sc_4_v_y.inverse_transform(regressor.predict(sc_4_v_x.transform([[129.6]]))))
print(sc_5_v_y.inverse_transform(regressor.predict(sc_5_v_x.transform([[129.6]]))))
print(sc_6_v_y.inverse_transform(regressor.predict(sc_6_v_x.transform([[129.6]]))))
print(sc_7_v_y.inverse_transform(regressor.predict(sc_7_v_x.transform([[129.6]]))))
print(sc_8_v_y.inverse_transform(regressor.predict(sc_8_v_x.transform([[129.6]]))))

lw = 2
plt.scatter(x_3_u, y_3_u, color='darkorange')#, label='data')

plt.scatter(x_2_u, y_2_u, color='darkorange', label='data')
plt.scatter(x_3_u, y_3_u, color='darkorange', label='data')
plt.scatter(x_4_u, y_4_u, color='darkorange', label='data')
plt.scatter(x_5_u, y_5_u, color='darkorange', label='data')
plt.scatter(x_6_u, y_6_u, color='darkorange', label='data')
plt.scatter(x_7_u, y_7_u, color='darkorange', label='data')
plt.scatter(x_8_u, y_8_u, color='darkorange', label='data')
plt.scatter(x_1_v, y_1_v, color='darkorange', label='data')
plt.scatter(x_2_v, y_2_v, color='darkorange', label='data')
plt.scatter(x_3_v, y_3_v, color='darkorange', label='data')
plt.scatter(x_4_v, y_4_v, color='darkorange', label='data')
plt.scatter(x_5_v, y_5_v, color='darkorange', label='data')
plt.scatter(x_6_v, y_6_v, color='darkorange', label='data')
plt.scatter(x_7_v, y_7_v, color='darkorange', label='data')
plt.scatter(x_8_v, y_8_v, color='darkorange', label='data')

plt.plot(x_3_u, y_rbf_3_u, color='navy')#, lw=lw, label='RBF model')
plt.plot(x_2_u, y_rbf_2_u, color='navy', lw=lw, label='RBF model')
plt.plot(x_3_u, y_rbf_3_u, color='navy', lw=lw, label='RBF model')
plt.plot(x_4_u, y_rbf_4_u, color='navy', lw=lw, label='RBF model')
plt.plot(x_5_u, y_rbf_5_u, color='navy', lw=lw, label='RBF model')
plt.plot(x_6_u, y_rbf_6_u, color='navy', lw=lw, label='RBF model')
plt.plot(x_7_u, y_rbf_7_u, color='navy', lw=lw, label='RBF model')
plt.plot(x_8_u, y_rbf_8_u, color='navy', lw=lw, label='RBF model')
plt.plot(x_1_v, y_rbf_1_v, color='navy', lw=lw, label='RBF model')
plt.plot(x_2_v, y_rbf_2_v, color='navy', lw=lw, label='RBF model')
plt.plot(x_3_v, y_rbf_3_v, color='navy', lw=lw, label='RBF model')
plt.plot(x_4_v, y_rbf_4_v, color='navy', lw=lw, label='RBF model')
plt.plot(x_5_v, y_rbf_5_v, color='navy', lw=lw, label='RBF model')
plt.plot(x_6_v, y_rbf_6_v, color='navy', lw=lw, label='RBF model')
plt.plot(x_7_v, y_rbf_7_v, color='navy', lw=lw, label='RBF model')
plt.plot(x_8_v, y_rbf_8_v, color='navy', lw=lw, label='RBF model')

plt.xlabel('Angle in Degrees')
plt.ylabel('U coordinate')
plt.title('Fittings and data plotting')
plt.legend()
plt.show()
'''