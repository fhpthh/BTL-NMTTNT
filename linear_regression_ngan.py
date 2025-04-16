import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('house_price.csv')
df.columns = ["index", "price", "acreage", "room", "area"]


# One-Hot Encoding cho cột "Vị trí"
df = pd.get_dummies(df, columns=['area'], drop_first=True)

print(df.head())

# Hàm dự đoán (hypothesis function)
def hypothesis(X, w):
    return np.dot(X, w) 

# Hàm mất mát (Loss Function - Mean Squared Error)
def compute_mse(X, y, w):
    m = len(y)  # Số mẫu
    predictions = hypothesis(X, w)  
    cost = np.sum((predictions - y) ** 2)  # Bình phương sai số
    mse = (1 / (2 * m)) * cost  # Công thức MSE
    return mse

# Hàm Gradient Descent
def gradient_descent(X, y, w, learning_rate, iterations):
    m = len(y)  # Số lượng mẫu
    mse_history = []  # Lưu trữ MSE qua từng vòng lặp
    
    for i in range(iterations):
        predictions = hypothesis(X, w)  
        error = predictions - y  # Tính sai số
        gradient = (1 / m) * np.dot(X.T, error)  # Tính gradient
        w -= learning_rate * gradient  # Cập nhật trọng số (w)
        
        mse = compute_mse(X, y, w)  # Tính MSE sau mỗi vòng lặp
        mse_history.append(mse)  
        
        if i % 100 == 0:  
            print(f"Iteration {i}: MSE = {mse}")
    
    return w, mse_history 

# Tạo ma trận đặc trưng và giá trị mục tiêu từ dữ liệu
X = df.drop(columns="price").values
y = df["price"].values


# Chuẩn hóa dữ liệu (Standardization) thủ công
X_mean = np.mean(X, axis=0)  # Tính trung bình theo cột
X_std = np.std(X, axis=0)  # Tính độ lệch chuẩn theo cột
X = (X - X_mean) / X_std  # Chuẩn hóa dữ liệu

# Khởi tạo trọng số ban đầu
w_initial = np.zeros(X.shape[1])  # Trọng số ban đầu = 0 (bias + w1 + w2)

# Tốc độ học và số vòng lặp
learning_rate = 0.01
iterations = 1000

# Chạy Gradient Descent để tìm trọng số tối ưu
w_optimal, mse_history = gradient_descent(X, y, w_initial, learning_rate, iterations)

# In ra trọng số tối ưu cuối cùng
print(f"Optimal weights: {w_optimal}")

# Ve do thi MSE qua tung vong lap
plt.plot(range(iterations), mse_history)
plt.xlabel("Iterations")
plt.ylabel("MSE") 
plt.title("MSE over iterations")
plt.show()
