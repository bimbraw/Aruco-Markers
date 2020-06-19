# Support Vector Regression (SVR)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# Average shoulder width from babies (~13 cm to adults (women ~35, men ~41))
# data from 35 to 55 cm, with my data being 49/5 cm)
dataset = pd.read_csv('SVMdata_edited.csv')
X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values
#print(X)
#print(y)
y = y.reshape(len(y),1)
#print(y)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
#print(X)
#print(y)

# Training the SVR model on the whole dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=180)
regressor.fit(X, y)
y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)

# Predicting a new result
print(sc_y.inverse_transform(regressor.predict(sc_X.transform([[36.5]]))))

'''
# Visualising the SVR results
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X)), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(X_grid, sc_y.inverse_transform(regressor.predict(sc_X.transform(X_grid))), color = 'blue')
plt.title('Fitting line and data plotting')
plt.xlabel('Shoulder to Shoulder Width (in cm)')
plt.ylabel('Overlay distance from center (in cm)')
plt.show()
'''
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
#plt.hold('on')
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
#plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('Angle')
plt.ylabel('Ratio')


#plt.xlabel('Shoulder to Shoulder Width (in cm)')
#plt.ylabel('Overlay distance from center (in cm)')
plt.title('Fittings and data plotting')
plt.legend()
plt.show()