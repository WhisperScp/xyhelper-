# 使用 Python 3.8 版本
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 设置pip源为阿里云
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip config set install.trusted-host mirrors.aliyun.com

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

# 复制源代码
COPY remainingCapacity.py main.py

# 运行程序
CMD ["python", "main.py"]