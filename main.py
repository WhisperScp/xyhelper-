import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def get_html_template(remaining_capacity, threshold):
    return f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background-color: #f9f9f9;
                }}
                .warning {{
                    color: #721c24;
                    background-color: #f8d7da;
                    border: 1px solid #f5c6cb;
                    padding: 10px;
                    border-radius: 4px;
                    margin-bottom: 20px;
                }}
                .capacity-info {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #dc3545;
                    text-align: center;
                    margin: 20px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="warning">
                    <h2>⚠️ 容量警告通知</h2>
                </div>
                <div class="capacity-info">
                    当前剩余次数: {remaining_capacity}<br>
                    警告阈值: {threshold}
                </div>
                <p>您的账户剩余容量已经低于设定的警告阈值，请及时处理。</p>
                <p>此邮件为自动发送，请勿直接回复。</p>
            </div>
        </body>
    </html>
    """

def send_email(remaining_capacity, threshold):
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')

    # 邮件内容
    subject = "容量警告通知"
    html_content = get_html_template(remaining_capacity, threshold)

    # 设置邮件内容
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
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
    'Cookie': f'user_id={os.getenv("USER_COOKIE")}'
}

# 从环境变量获取配置
threshold = int(os.getenv('THRESHOLD', 1000))
check_interval = int(os.getenv('CHECK_INTERVAL', 600))

# 持续检查remainingCapacity
while True:
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data', {})
            remaining_capacity = data.get('remainingCapacity')

            print(f"当前剩余容量: {remaining_capacity}")

            if remaining_capacity < threshold:
                print(f"剩余容量低于{threshold}，准备发送邮件...")
                send_email(remaining_capacity, threshold)

        else:
            print(f"请求失败，状态码: {response.status_code}")

    except Exception as e:
        print(f"发生错误: {e}")

    time.sleep(check_interval)
