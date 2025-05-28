from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Tải dữ liệu
data = fetch_california_housing()
X = data.data
y = data.target

# Tách tập train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# Lưu mô hình
joblib.dump(model, "model.pkl")

print("Đã lưu mô hình dự đoán giá nhà vào model.pkl")
