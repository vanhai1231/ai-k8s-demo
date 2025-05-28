# 1. Dùng Python base image
FROM python:3.10-slim

# 2. Đặt thư mục làm việc bên trong container
WORKDIR /app

# 3. Copy file requirements.txt và cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy toàn bộ code và mô hình vào container
COPY . .

# 5. Mở cổng Flask app
EXPOSE 5000

# 6. Command chạy app.py
CMD ["python", "app.py"]
