from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from email import policy

E_MAIL = 'xxx@gmail.com'
SENHA = 'xxx'

with open('xxx', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='xxx', data=data_atual)

print(corpo_msg)

msg = MIMEMultipart(policy=policy.default)
msg['from'] = 'Diógenes Dornelles Costa'
msg['to'] = 'xxx@gmail.com'  # Cliente
msg['subject'] = 'Atenção: este é um e-mail urgente!'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('xxx@gmail.com', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(E_MAIL, SENHA)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as err:
        print('E-mail não enviado.')
        print(err)
