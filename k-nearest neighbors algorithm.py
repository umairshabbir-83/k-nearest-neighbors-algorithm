from math import sqrt
from sklearn import neighbors
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('/content/Fish.csv')
df.head()

df.isnull().sum()

df.drop(['Species'], axis=1, inplace=True)
df = pd.get_dummies(df)
df

# Model Training
train, test = train_test_split(df, test_size=0.3)
x_train = train.drop('Weight', axis=1)
y_train = train['Weight']
x_test = test.drop('Weight', axis=1)
y_test = test['Weight']

# %matplotlib inline

# Model Testing
rmse_val = []
for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors=K)

    # Model Fitting
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    error = sqrt(mean_squared_error(y_test, pred))
    rmse_val.append(error)
    print('RMSE value for K = ', K, 'is:', error)

# Plotting RMSE values against value of K
curve = pd.DataFrame(rmse_val)
curve.plot()

# Model Fitting Minimum RMSE
model = neighbors.KNeighborsRegressor(n_neighbors=3)
model.fit(x_train, y_train)
pred = model.predict(x_test)
error = sqrt(mean_squared_error(y_test, pred))
rmse_val.append(error)  # store rmse values
print('RMSE value for K = ', 3, 'is:', error)

# Prediction Results
test['predicted weights'] = pred
test
