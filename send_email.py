# https://support.google.com/accounts/answer/185833

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import traceback

import config

def send_email_with_attach(destination=None, subject=None, body=None, attach_path_list=[]):
    # Inicia o email
    mimemsg = MIMEMultipart()
    mimemsg['From']=config.email
    mimemsg['To']=destination
    mimemsg['Subject']=subject
    if body:
        mimemsg.attach(MIMEText(body, 'plain'))

    # Para cada attachment na lista
    for mail_attachment in attach_path_list:
        mail_attachment_name = mail_attachment.split('/')[-1]

        with open(mail_attachment, "rb") as attachment:
            mimefile = MIMEBase('application', 'octet-stream')
            mimefile.set_payload((attachment).read())
            encoders.encode_base64(mimefile)
            mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
            mimemsg.attach(mimefile)

    # Envia o email por o server smpt configurado em config
    with smtplib.SMTP(config.host, config.port) as server:
        server.starttls()
        server.login(config.email, config.password)
        server.send_message(mimemsg)

if __name__ == '__main__':
    try:
        send_email_with_attach('artur.temporal@hotmail.com', 'Test', 'Test', ['/home/bcc/atc19/Captura de tela de 2022-10-26 14-18-28.png'])
    except:
        traceback.print_exc()