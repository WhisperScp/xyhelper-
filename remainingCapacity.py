import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# 邮件发送函数
def send_email(remaining_capacity):
    sender_email = "909045610@qq.com"  # 发送方邮箱
    receiver_email = "1697044379@qq.com"     # 接收方邮箱
    password = "mabsdctimghpbfei"         # 发送方邮箱的密码或授权码

    # 邮件内容
    subject = "Remaining Capacity Warning"
    body = f"Warning: The remaining capacity is {remaining_capacity}, which is below 100."

    # 设置邮件内容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # 连接到SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 使用SSL的SMTP服务器
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")

# 请求的URL
url = 'https://www.xyhelper-agent.com/User/GetCapacity'

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.xyhelper-agent.com/LogList.html',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=1, i',
    'Cookie': 'user_id=ff568afe8ac64313a981cb5ccf8d455d'
}

# 设定的阈值
threshold = 1000

# 持续检查remainingCapacity
while True:
    try:
        # 发出请求
        response = requests.get(url, headers=headers)

        # 确认请求成功
        if response.status_code == 200:
            data = response.json().get('data', {})
            remaining_capacity = data.get('remainingCapacity')

            print(f"当前剩余容量: {remaining_capacity}")

            # 检查剩余容量是否小于阈值
            if remaining_capacity < threshold:
                print("剩余容量低于100，准备发送邮件...")
                send_email(remaining_capacity)
                # 邮件发送后继续循环，保持监控状态

        else:
            print(f"请求失败，状态码: {response.status_code}")

    except Exception as e:
        print(f"发生错误: {e}")

    # 等待一段时间再进行下一次检查 (这里设为10分钟)
    time.sleep(10)  # 单位为秒，600秒 = 10分钟
