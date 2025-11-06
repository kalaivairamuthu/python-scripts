import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

url1 = ''
Headers1 = {'Content-Type': 'application/json'}
data1 = {"username": "admin", "password": "Cl0u4@dmin"}
#post = requests.post(url1, data=data1, headers=Headers1)
response = requests.post(url1, headers=Headers1, data=json.dumps(data1)).text
print(response)
parsed_json = (json.loads(response))
Token=parsed_json['data']['token']['key']
print(Token)
#url = 'https://ggggg/'
url = 'http://vvvvvvv'
Headers = {'X-Auth-Token': Token, 'Content-Type': 'application/json', 'X-Auth-User': 'admin'}

print("Token applied")
x = requests.get(url, headers=Headers)
print(x)
status = x.text
print(json.dumps(status))
#data  x.content
#print(data)
response = x.status_code
print(response)
if response == requests.codes.ok: 
  print("response is 200" )
else:
  smtpObj = smtplib.SMTP('smtp.office365.com', 587)
  smtpObj.ehlo()
  smtpObj.starttls()
  smtpObj.login("kal", "")
  sender_email = "kal"
  receiver_email = "kala"
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
