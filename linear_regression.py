import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import train_test_split

# Read data
df = pd.read_csv('house_price.csv')
df.columns = ["index", "price", "acreage", "room", "area"]
print(df.head())

#MA HOA ONE-HOT CHO AREA
df = pd.get_dummies(df, columns=['area'], drop_first=True)

# Tach features (X) tru cot price và taget (y)
X = df.drop(columns="price").values
y = df["price"].values

# chuan hoa du lieu
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# chia data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# MSE - ham mat mat
def computer_cost(X, y, w, b):
     m = X.shape[0] # sl mau
     f_wb = np.dot(X, w) + b  #tinh vector du doan y_hat = X.w + b
     cost = np.sum((f_wb - y) ** 2)
     total_cost = 1 / (2 * m) * cost # cong thuc MSE
     return total_cost


# Ham gradient
def compute_gradient(X, y, w, b):
    m, n = X.shape # m la so mau, n : so dac trung
    err = (np.dot(X, w) + b) - y   #sai so
    dj_dw = (1/m) * np.dot(X.T, err) #gradient dao ham voi w
    dj_db = (1/m) * np.sum(err) #gradiun vs dao ham b

    return dj_dw, dj_db


# Ve bieu do
sns.scatterplot(
    data=df,
    x="price",
    y="acreage",
)
plt.show()