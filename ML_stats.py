import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def train():
    pass

def predict_stat_ML(player_data):
    x = LinearRegression().fit(player_data)
    print(x)
    pass

X = np.arange(1,101).reshape((100,1))
y = np.dot(X, [7]) + 3
reg = LinearRegression().fit(X, y)
coef = np.round(reg.coef_[0])
print("The coefficient is " + str(coef))
temp =ggplot(DataFrame({'X':X.reshape(100),'y':y.reshape(100)})) + \
geom_line(aes(x='X', y='y'), color = "blue", size=0.8) + \
ggtitle("f(X) = 7X + 3")
print(temp)