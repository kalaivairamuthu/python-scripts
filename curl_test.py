import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

url = '<url>'
myobj = {'<username>': '<password>'}

x = requests.post(url, data = myobj)

response = x.status_code
print(response)
if response == 200: 
  print("response is 200" )
else:
  smtpObj = smtplib.SMTP('smtp.office365.com', 587)
  smtpObj.ehlo()
  smtpObj.starttls()
  smtpObj.login("<sender_mail_id>", "<mail_password>")
  sender_email = "<sender_mail_id>"
  receiver_email = "<receiver_mail_id>"
  msg = MIMEMultipart()
  msg['Subject'] = 'Dev server2 UI Response is not 200'
  msg['From'] = sender_email
  msg['To'] = receiver_email
  body = """<p>Hi Team,</p>
          <p>Kindly check whether Dev server UI is up and running.</p>
          <p>Thanks,</p>
          <p>DevopsTeam</p>"""

  print(body)
  msgText = MIMEText('<b>%s</b>' % (body), 'html')
  print(msgText)
  msg.attach(msgText)
  try:
      smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
  except Exception as e:
      print(e)


