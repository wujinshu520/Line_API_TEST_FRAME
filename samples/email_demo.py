# encoding: utf-8
# @author: wujinshu
# @file: email_demo.py
# @time:2021/11/20 14:03
# @desc: 邮件发送
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_body = '''
<h1 align="center"> 接口自动化测试报告</h1>
<P align="center">详情见附件  备注：封装后的</p>
'''
html_file_path = os.path.join(
    os.path.dirname(__file__), '..', 'html_reports', 'WX_API_TEST_V1.2','WX_API_TEST_V1.2.html'
)

test_obj = MIMEText(email_body, 'html', 'utf-8')
attach_file = MIMEText(
    open(html_file_path, 'rb').read(),
    'base64', 'utf-8')
attach_file['Content-type'] = 'application/octet-stream'
attach_file.add_header(
    'Content-Disposition',
    'attachment',
    filename=('gbk', '', 'WWX_API_TEST_V1.2.html')
)

email_obj = MIMEMultipart()
email_obj.attach(test_obj)
email_obj.attach(attach_file)
email_obj['from'] = '3123838856@qq.com'  # 发件人
email_obj['to'] = 'wujinshu1314@foxmail.com'  # 收件人
email_obj['Cc'] = 'wujinshu1314@foxmail.com'  # 抄送人
email_obj['subject'] = '接口自动化测试报告'

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
smtp.login(user='1964855301@qq.com', password='yyszkmkhzqurdfjg')
smtp.sendmail("1964855301@qq.com", email_obj.as_string())
smtp.close()
