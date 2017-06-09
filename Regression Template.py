

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.set_printoptions(threshold=np.inf)


# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values           

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""                                               
                                                   
#Fitting Regression model to the dataset

#Predicting a new result with Regression
y_pred = regressor.predict((6.5))

# Visualizing the Regression results
plt.scatter(X,y, color = 'Red' )
plt.plot(X,regressor.predict(X), color = 'Blue')
plt.title('Truth or Bluff (Linear Regression) ')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

# Visualizing the Regression results with higher resolution
X_grid = np.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape(len(X_grid),1 )
plt.scatter(X,y, color = 'Red' )
plt.plot(X_grid,regressor.predict((X_grid)), color = 'Blue')
plt.title('Truth or Bluff (Polynomial Regression) ')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()


