# ChatGPT 拼车次数监控工具
![2](https://github.com/user-attachments/assets/c08f14d9-fbed-43f8-b973-8deff875287a)


## 项目介绍
基于吴总拼车点开发的 ChatGPT 使用次数监控工具。当账户剩余次数低于设定阈值时，自动发送邮件提醒，帮助用户及时充值。

## 功能特点
- 🔄 自动监控剩余使用次数
- 📧 低于阈值自动邮件提醒
- 🎨 美化的HTML邮件模板
- 🔧 支持多种邮箱配置

## 快速开始

1. 安装 Python 3.7+

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置 `.env` 文件：
```env
# 邮件配置
SENDER_EMAIL=发件人邮箱
RECEIVER_EMAIL=收件人邮箱
EMAIL_PASSWORD=邮箱授权码
SMTP_SERVER=smtp.qq.com  # 可选，自动识别常用邮箱
SMTP_PORT=465           # 可选
SMTP_SSL=true          # 可选

# API配置
USER_COOKIE=你的Cookie值

# 监控配置
THRESHOLD=1600        # 警告阈值
CHECK_INTERVAL=600    # 检查间隔（秒）
```

4. 运行程序：
```bash
python main.py
```
![3](https://github.com/user-attachments/assets/e1a91398-0dbc-4df2-b9b9-2a7240ba0408)

### 获取配置信息

1. **获取Cookie**
   - 登录 [拼车点网站](https://www.xyhelper-agent.com)
   - 打开浏览器开发者工具（F12）
   - 在Network标签页找到请求头中的Cookie
   - 复制 `user_id=xxxxxx` 部分
![1](https://github.com/user-attachments/assets/cc85b2fd-71ce-4f1a-80d9-0c82a00f5919)

2. **获取邮箱授权码**
   - QQ邮箱：设置 -> 账户 -> POP3/SMTP服务
   - 163邮箱：设置 -> POP3/SMTP/IMAP -> 开启服务
   - 其他邮箱请参考对应邮箱服务商说明

## 支持的邮箱服务商
- QQ邮箱 (@qq.com)
- 163邮箱 (@163.com)
- Gmail (@gmail.com)
- Outlook (@outlook.com)
- 其他邮箱需手动配置SMTP信息

## 常见问题

### 1. 邮件发送失败
- 检查邮箱授权码是否正确
- 确认SMTP服务是否开启
- 检查网络连接状态

### 2. 监控请求失败
- 验证Cookie是否有效
- 确认Cookie格式是否正确
- 检查网络连接状态

## 注意事项
- Cookie值请勿泄露给他人
- 建议将检查间隔设置在5-15分钟之间
- 警告阈值建议根据个人使用频率设置

## 联系方式
- 拼车点官方群
- GitHub Issues

## 开源协议
MIT License

## Docker 部署

### 方式一：使用环境变量（推荐，一行命令运行）

```bash
docker run -d \
           -e SENDER_EMAIL=xxx@qq.com \
           -e RECEIVER_EMAIL=xxx@qq.com \
           -e EMAIL_PASSWORD=你的授权码 \
           -e USER_COOKIE=你的Cookie值 \
           -e THRESHOLD=低于多少发邮件 \
           -e CHECK_INTERVAL=多少秒检测一次 \
           -e SMTP_SERVER=smtp.qq.com \
           -e SMTP_PORT=465 \
           -e SMTP_SSL=true \
           --restart always whisperscp/xyhelper-agent-warning:latest
```

只需要替换以下内容：
- `xxx@qq.com` 替换为您的实际邮箱
- `你的授权码` 替换为邮箱的授权码（QQ邮箱设置->账户->POP3/SMTP服务）
- `你的Cookie值` 替换为从拼车点网站获取的 Cookie
- 可选配置：
  - THRESHOLD：警告阈值（默认1600）
  - CHECK_INTERVAL：检查间隔，单位秒（默认600）
  - SMTP_SERVER：邮箱服务器地址
  - SMTP_PORT：邮箱服务器端口
  - SMTP_SSL：是否使用SSL（true/false）

常用命令：
```bash
# 查看容器日志
docker logs 容器ID

# 停止容器
docker stop 容器ID

# 重启容器
docker restart 容器ID

# 查看运行中的容器
docker ps
```

常用邮箱 SMTP 配置：
- QQ邮箱：smtp.qq.com:465 (SSL=true)
- 163邮箱：smtp.163.com:465 (SSL=true)
- Gmail：smtp.gmail.com:587 (SSL=false)
- Outlook：smtp.office365.com:587 (SSL=false)
