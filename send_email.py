#1.
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


#2.
#!/usr/bin/env pyhton

# import os 
# import time 
# import smtplib
# from email.mime.text import MIMEText
# from datetime import datetime
# from dotenv import load_dotenv

# load_dotenv()

# #configs
# LOG_FILE="/var/log/auth.log"
# SENDER_EMAIL=os.getenv("SENDER_EMAIL")
# SENDER_PASSWORD=os.getenv("SENDER_PASSWORD")
# RECEIVER_EMAIL=["abhinaysikarwar7@gmail.com"]

# msg=MIMEText("This is a and Testing Email for SSH MONITORING")
# msg["Subject"]="Test Email - SSH MONITOR SETUP"
# msg["From"]=SENDER_EMAIL
# msg["To"]=",".join (RECEIVER_EMAIL)

# try:
#     with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
#         server.login(SENDER_EMAIL,SENDER_PASSWORD)
#         server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_string())
#         print("[OK]Test Email Working....")
# except Exception as e :
#     print(f"[ERROR] Email Failed : {e}")




#3.
#!/usr/bin/env pyhton3

# import os 
# import time 
# import smtplib
# from email.mime.text import MIMEText
# from datetime import datetime
# from dotenv import load_dotenv

# load_dotenv()

# #configs
# LOG_FILE="/var/log/auth.log"
# SENDER_EMAIL=os.getenv("SENDER_EMAIL")
# SENDER_PASSWORD=os.getenv("SENDER_PASSWORD")
# RECEIVER_EMAIL=["abhinaysikarwar7@gmail.com"]


# def build_email_body(username,ip_address,method,timestamp):
#     return f"""
#     User : {username}
#     From IP : {ip_address}
#     Method : {method}
#     Time : {timestamp}
#     """

# def send_email(username,ip_address,method,timestamp):
#     subject=f"SSH Login Alert {username} Logged in..."
#     body=build_email_body(username,ip_address,method,timestamp)
#     msg=MIMEText(body)
#     msg["Subject"]=subject
#     msg["From"]=SENDER_EMAIL
#     msg["To"]=", ".join(RECEIVER_EMAIL)
    
#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
#             server.login(SENDER_EMAIL,SENDER_PASSWORD)
#             server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_string())
#             print(f"[OK] Mail sent for {username} - {ip_address} to {RECEIVER_EMAIL}")
#     except Exception as e :
#             print(f"[ERROR] Email Failed : {e}")


# def check_log_for_login(line):
#     if "Accepted" not in line:
#         return

#     words=line.split()

#     try:
#         accepted_index = words.index("Accepted")
#         method = words[accepted_index+1]
#         username = words[accepted_index+2]
#         ip_address = words[accepted_index+3]
#     except Exception as e :
#         return
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     send_email(username,ip_address,method,timestamp)

# def watch_log():
#     print(f"[INFO] watching {LOG_FILE} for SSH logins...")
#     with open(LOG_FILE,"r") as f:
#         f.seek(0,2)

#         while True:
#             line=f.readline()

#             if not line:
#                 time.sleep(1)
#                 continue

#             check_log_for_login(line)
            
# if __name__=="__main__":
   
#     watch_log()





#4.
#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime,timedelta

HISTORY_FILE="/home/ubuntu/.bash_history"
SENDER_EMAIL="sikarwarlakhan00@gmail.com"
SENDER_PASSWORD="mhhk rqtw vamr yvir"
RECEIVER_EMAIL=["abhinaysikarwar7@gmail.com"]
HOURS_BACK=24

def get_commands():
    cutoff=datetime.now() - timedelta(hours=HOURS_BACK)
    commands=[]
    current_timestamp=None
    with open(HISTORY_FILE,"r",errors="ignore") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            if line.startswith("#"):
                try:
                    epoch_value=int(line[1:])
                    current_timestamp=datetime.fromtimestamp(epoch_value)
                except ValueError:
                    current_timestamp=None
            else:
                if current_timestamp and current_timestamp >= cutoff:
                    commands.append((current_timestamp,line))
                current_timestamp=None
                
    return commands

def make_email_body(commands):
    if not commands:
        return "No Commands found in 24 HOURS "
    lines =[f"-----Total Commands: {len(commands)}\n------"]
    for i , (time,cmd) in enumerate(commands,start=1):
        lines.append(f" * {i}. [{time.strftime("%H:%M:%S")}] {cmd} ")
    return "\n".join(lines)

def send_email(commands):
    subject=f"========Daily Commands Summary========="
    body=make_email_body(commands)
    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=SENDER_EMAIL
    msg["To"]=", ".join(RECEIVER_EMAIL)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_string())
            print(f"[OK] Mail sent to {RECEIVER_EMAIL}")
    except Exception as e:
        print(f"[ERROR] Email Failed : {e}")

if __name__=="__main__":
    commands=get_commands()
    send_email(commands)