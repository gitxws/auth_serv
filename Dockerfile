# 使用 Python 官方的 Alpine 镜像
FROM python:3.9-alpine

# 设置工作目录
WORKDIR /app

# 复制必要的文件到容器中
COPY requirements.txt requirements.txt
COPY app.py app.py

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 创建挂载点
VOLUME /usr/app

# 暴露 Flask 默认端口
EXPOSE 5050

# 启动应用
CMD ["python", "app.py"]
