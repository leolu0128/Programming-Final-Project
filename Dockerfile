# 使用輕量級的 Python 3.10 映像檔
FROM python:3.10-slim

# 設定容器內的工作目錄
WORKDIR /app

# 將 requirements.txt 複製到容器內並安裝套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 將專案所有檔案複製到容器內
COPY . .

# 曝露 5000 port 供外部連線
EXPOSE 5000

# 啟動 Flask 伺服器
CMD ["python", "app.py"]