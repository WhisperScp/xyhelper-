# ChatGPT 拼车次数监控工具

## 项目介绍
基于吴总拼车点开发的 ChatGPT 使用次数监控工具。当账户剩余次数低于设定阈值时，自动发送邮件提醒，帮助用户及时充值。

## 功能特点
- 🔄 自动监控剩余使用次数
- 📧 低于阈值自动邮件提醒
- 🎨 美化的HTML邮件模板
- 🔧 支持多种邮箱配置
- 🐳 支持Docker一键部署

## 快速开始

### Docker 快速部署

1. 直接运行（推荐）：
```bash
docker run -d \
  --name chatgpt-monitor \
  --restart always \
  -e SENDER_EMAIL=你的邮箱 \
  -e RECEIVER_EMAIL=接收邮箱 \
  -e EMAIL_PASSWORD=邮箱授权码 \
  -e USER_COOKIE=你的Cookie \
  whisperscp/xyhelper-agent-warning:latest
```

2. 使用 docker-compose：

创建 `docker-compose.yml`：
```yaml
version: '3'
services:
  chatgpt-monitor:
    image: whisperscp/xyhelper-agent-warning:latest
    container_name: chatgpt-monitor
    environment:
      - SENDER_EMAIL=你的邮箱
      - RECEIVER_EMAIL=接收邮箱
      - EMAIL_PASSWORD=邮箱授权码
      - USER_COOKIE=你的Cookie
    restart: always
```

运行：
```bash
docker-compose up -d
```

### 环境变量说明

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

### 获取配置信息

1. **获取Cookie**
   - 登录 [拼车点网站](https://www.xyhelper-agent.com)
   - 打开浏览器开发者工具（F12）
   - 在Network标签页找到请求头中的Cookie
   - 复制 `user_id=xxxxxx` 部分

2. **获取邮箱授权码**
   - QQ邮箱：设置 -> 账户 -> POP3/SMTP服务
   - 163邮箱：设置 -> POP3/SMTP/IMAP -> 开启服务
   - 其他邮箱请参考对应邮箱服务商说明

## Docker 常用命令

```bash
# 查看运行状态
docker ps

# 查看日志
docker logs -f chatgpt-monitor

# 停止服务
docker-compose down

# 重启服务
docker-compose restart
```

## 支持的邮箱服务商
- QQ邮箱 (@qq.com)
- 163邮箱 (@163.com)
- Gmail (@gmail.com)
- Outlook (@outlook.com)
- 其他邮箱需手动配置SMTP信息

## 常见问题

### 1. 邮件发送失败
- 检查邮箱授权码是否正��
- 确认SMTP服务是否开启
- 检查网络连接状态

### 2. 监控请求失败
- 验证Cookie是否有效
- 确认Cookie格式是否正确
- 检查网络连接状态

### 3. Docker相关问题
- 确保Docker和Docker Compose已安装
- 检查环境变量是否正确配置
- 查看容器日志排查具体错误

## 本地部署（不推荐）

如果不使用Docker，也可以直接在本地运行：

1. 安装Python 3.7+
2. 安装依赖：`pip install -r requirements.txt`
3. 配置环境变量
4. 运行：`python main.py`

## 注意事项
- Cookie值请勿泄露给他人
- 建议将检查间隔设置在5-15分钟之间
- 警告阈值建议根据个人使用频率设置
- 使用Docker部署时注意保护好.env文件

## 联系方式
- 拼车点官方群
- GitHub Issues

## 开源协议
MIT License
