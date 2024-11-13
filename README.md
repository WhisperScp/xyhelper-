# ChatGPT 拼车次数监控工具

## 项目介绍
这是一个基于吴总拼车点开发的 ChatGPT 使用次数监控工具。当账户剩余次数低于设定阈值时，会自动发送邮件提醒，帮助用户及时充值，避免使用中断。

## 主要功能
- 🔄 定期检查剩余使用次数
- 📧 低次数邮件提醒（支持HTML美化邮件）
- ⚙️ 可配置的监控参数（次数阈值、检查间隔）
- 🔒 支持环境变量配置敏感信息

## 技术特点
- 基于吴总拼车点API开发
- 支持 QQ邮箱 SMTP 发送提醒邮件
- 采用 dotenv 管理配置
- HTML 模板渲染邮件内容

## 使用方法

### 1. 环境要求
- Python 3.7 或更高版本
- 有效的拼车点账号和Cookie

### 2. 安装依赖
首先确保你在项目目录下，然后运行以下命令：

```bash
# 方法1：直接使用pip安装
pip install -r requirements.txt

# 方法2：如果下载速度慢，可以使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 3. 配置环境变量
创建 `.env` 文件，填入以下配置：

```env
# 邮件配置
SENDER_EMAIL=你的QQ邮箱
RECEIVER_EMAIL=接收提醒的邮箱
EMAIL_PASSWORD=QQ邮箱授权码（不是登录密码）

# API配置
USER_COOKIE=你的拼车点Cookie值

# 监控配置
THRESHOLD=1600        # 剩余次数警告阈值（建议设置在1000-2000之间）
CHECK_INTERVAL=600    # 检查间隔时间（秒，建议10分钟）
```

### 4. 获取Cookie
1. 登录 [拼车点网站](https://www.xyhelper-agent.com)
2. 打开浏览器开发者工具（F12）
3. 在网络（Network）标签页中找到请求头中的 `Cookie` 值
4. 复制 `user_id=xxxxxx` 部分到配置文件

### 5. 运行程序
```bash
python remainingCapacity.py
```

## 配置说明

### 邮件配置
- `SENDER_EMAIL`: 用于发送提醒的QQ邮箱
- `RECEIVER_EMAIL`: 接收提醒的邮箱地址
- `EMAIL_PASSWORD`: QQ邮箱的SMTP授权码

### 监控配置
- `THRESHOLD`: 次数警告阈值，当剩余次数低于此值时发送提醒
- `CHECK_INTERVAL`: 检查间隔时间，单位为秒
- `USER_COOKIE`: 拼车点账号的Cookie值

## 注意事项
1. 需要开启QQ邮箱的SMTP服务并获取授权码
2. Cookie值请勿泄露给他人
3. 建议将检查间隔设置在5-15分钟之间
4. 警告阈值建议根据个人使用频率来设置

## 常见问题
1. 邮件发送失败
   - 检查QQ邮箱是否开启SMTP服务
   - 确认授权码是否正确
   - 检查网络连接

2. 获取次数失败
   - 确认Cookie是否正确
   - 检查Cookie是否过期
   - 确认网络连接是否正常

## 联系方式
如有问题可以通过以下方式联系：
- 拼车点官方群
- 提交GitHub Issue

## 许可证
MIT License