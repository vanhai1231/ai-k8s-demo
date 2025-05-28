# 🧐 AI Housing Price Prediction API - CI/CD with Docker + Render

## 📌 Mô tả dự án

Dự án này triển khai một mô hình AI đơn giản dự đoán giá nhà tại California bằng **Flask API**, được **đóng gói với Docker**, **tự động build bằng GitHub Actions**, và **deploy public qua Render**.

---

## 🚀 Link demo API đang chạy

👉 [https://ai-k8s-demo.onrender.com](https://ai-k8s-demo.onrender.com)

---

## 🛠 Công nghệ sử dụng

* `Python` + `Flask`
* `scikit-learn`: LinearRegression
* `Docker`
* `GitHub Actions` (CI/CD)
* `Docker Hub`: push image
* `Render.com`: triển khai container
* (Có sẵn folder `k8s/` nếu muốn deploy lên Kubernetes)

---

## 📂 Cấu trúc thư mục

```
ai-k8s-demo/
├── app.py                 # Flask API
├── model.pkl              # Mô hình đã huấn luyện
├── requirements.txt       # Thư viện Python
├── Dockerfile             # Build Docker image
├── train_save_model.py    # Script tạo model.pkl
├── README.md              # File mô tả
├── .github/workflows/
│   └── docker-push.yml    # GitHub Actions CI/CD
└── k8s/
    ├── deployment.yaml    # Kubernetes Deployment file
    └── service.yaml       # Kubernetes Service file
```

---

## 🥪 Hướng dẫn test API

Gửi POST request đến `/predict` với input JSON chứa `features` (8 đặc trưng):

### ✅ Ví dụ (dùng `curl` trên CMD/Terminal):

```bash
curl -X POST https://ai-k8s-demo.onrender.com/predict \
 -H "Content-Type: application/json" \
 -d "{\"features\": [8.3252, 41, 6.9841, 1.0238, 322, 2.5556, 37.88, -122.23]}"
```

### 🔁 Kết quả mẫu:

```json
{"predicted_price": 4.15}
```

---

## 📦 CI/CD Pipeline

1. **Push code lên GitHub**
2. **GitHub Actions** sẽ:

   * Build Docker image từ Dockerfile
   * Push image lên Docker Hub (`vanhaiha/ai-k8s-demo:latest`)
3. **Render** sẽ pull image và deploy

---

## ☁️ Tùy chọn K8s (không bắt buộc)

Thư mục `k8s/` gồm:

* `deployment.yaml`
* `service.yaml`

Bạn có thể deploy image lên Minikube hoặc cluster thật bằng:

```bash
kubectl apply -f k8s/
```

---
