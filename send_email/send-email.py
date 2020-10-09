# 发送邮件模块
import smtplib
# 定义邮件内容
from email.mime.text import MIMEText
# 定义邮件标题
from email.header import Header
# 发送邮箱服务器
smtp_server = 'smtp.exmail.qq.com'
# 发送邮箱用户名
user = 'tanghongyu@reworldgame.com'
# 密码，此密码需要授权
password = 'b34i529kPnpim5wF'
# 发信方
sender = 'tanghongyu@reworldgame.com'
# 接收方
receive = '13051082905@163.com'
# 发送邮件的主题
subject = 'Rewold自动化测试报告'
# 内容
context = '<html><h1 style="color:red">Rewold自动化测试报告</h1></html>'
# html邮件正文
msg = MIMEText(context, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
msg['To'] = receive
# SSL协议端口号
smtp = smtplib.SMTP_SSL(smtp_server, 465)
# 向服务器表明用户身份
smtp.helo(smtp_server)
# 服务器返回结果确认
smtp.ehlo(smtp_server)
# 登录邮箱
smtp.login(user, password)
# 开始发送
print("stsrt send email~~~~")
smtp.sendmail(sender, receive, msg.as_string())
# 发送完退出
smtp.quit()
print("send  email  end")
print(6000-5948.64)