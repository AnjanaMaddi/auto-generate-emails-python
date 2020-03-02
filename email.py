import pandas as pd
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(path_csv,n,path_temp,subject,mail_id,password,smtp_host,p):
    df=pd.read_csv(path_csv)
    with open(path_temp, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    message_template=Template(template_file_content)
    MY_ADDRESS = mail_id
    PASSWORD = password
    s = smtplib.SMTP(host=smtp_host, port=p)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    for i in range(len(df)):
        msg = MIMEMultipart()
        d={}
        d['NAME']=df.iloc[i,0]
        var="VAR_"
        for v in range(n):
            x=var+str(v)
            d[x]=df.iloc[i,n+2]
        message = message_template.substitute(d)
        msg['From']=MY_ADDRESS
        msg['To']=df.iloc[i,1]
        msg['Subject']=subject
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
