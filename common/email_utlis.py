# encoding: utf-8
# @author: wujinshu
# @file: email_utlis.py
# @time:2021/11/21 13:20
# @desc:
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_utils import config


class EmailUtlis(object):
    def __init__(self, email_body, email_attch_path=None):
        self.smtp_server = config.SMTP_SERVER
        self.sender = config.SENDER
        self.password = config.PASSWORD
        self.receiver = config.RECEIVER
        self.cc = config.CC
        self.subject = config.SUBJECT
        self.body = email_body
        self.attch_path = email_attch_path

    def email_body(self):
        email_obj = MIMEMultipart()
        email_obj['from'] = self.sender
        email_obj['to'] = self.receiver  # 收件人
        email_obj['Cc'] = self.cc  # 抄送人
        email_obj['subject'] = self.subject
        email_obj.attach(MIMEText(self.body, 'html', 'utf-8'))
        if self.attch_path:
            attach_file = MIMEText(open(self.attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file['Content-type'] = 'application/octet-stream'
            attach_file.add_header(
                'Content-Disposition', 'attachment',
                filename=('gbk', '',
                          os.path.basename(self.attch_path)
                          ))
            email_obj.attach(attach_file)
        return email_obj

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.sender, password=self.password)
        smtp.sendmail(self.sender, self.receiver.split(",") + self.cc.split(","), self.email_body().as_string())
        smtp.close()


if __name__ == "__main__":
    email_body = '''
    <h1 align="center"> 接口自动化测试报告</h1>
    <P align="center">详情见附件  备注：封装后的</p>
    '''
    html_file_path = os.path.join(
        os.path.dirname(__file__), '..',
        'html_reports', 'WX_API_TEST_V1.2',
        'WX_API_TEST_V1.2.html'
    )
    EmailUtlis(email_body, html_file_path).send_mail()
