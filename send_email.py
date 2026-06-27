#!/usr/bin/env python3

# import os 
# import time 
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_email_python(sender_email,sender_password,receiver_email,subject,body):
#     msg=MIMEMultipart()
#     msg["From"]=sender_email
#     msg["To"]=receiver_email
#     msg["Subject"]=subject

#     msg.attach(MIMEText(body,"plain"))

#     try:
#         server=smtplib.SMTP("smtp.gmail.com",587)
#         server.starttls()
#         server.login(sender_email,sender_password)
#         server.sendmail(sender_email,receiver_email,msg.as_string())
#         server.quit()
#         print("Email sent Succussfully...✅")
#     except Exception as e:
#         print("Error :",e)

# send_email_python(
#     sender_email="sikarwarlakhan00@gmail.com",
#     receiver_email="abhinaysikarwar7@gmail.com",
#     sender_password="mhhk rqtw vamr yvir",
#     subject="Testing Email Sender Using Pure Python",
#     body="Hello ! This email from python programming in IQ",\
# )



#!/usr/bin/env pyhton

import os 
import time 
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

#configs
LOG_FILE="/var/log/auth.log"
SENDER_EMAIL=os.getenv("SENDER_EMAIL")
SENDER_PASSWORD=os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL=["abhinaysikarwar7@gmail.com"]

msg=MIMEText("This is a and Testing Email for SSH MONITORING")
msg["Subject"]="Test Email - SSH MONITOR SETUP"
msg["From"]=SENDER_EMAIL
msg["To"]=",".join (RECEIVER_EMAIL)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_string())
        print("[OK]Test Email Working....")
except Exception as e :
    print(f"[ERROR] Email Failed : {e}")