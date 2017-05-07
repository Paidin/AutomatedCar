# Other python programs are able to send emails if this file is imported

import smtplib

###################################
# Include login settings      
from MailConfig import *
# 'MailConfig' contains following:      
#User = "email.address@gmail.com"   
#Pass = "password"
#SMTP_Server = "smtp.gmail.com"
#SMTP_Port = 587
###################################

def SendEMail(Target, Subject, Text):
    print("Starting E-Mail Service...")
    smtpserver = smtplib.SMTP(SMTP_Server, SMTP_Port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    print("::: Login as", User)
    smtpserver.login(User, Pass)
    header = "To: " + Target + "\n" + "From: " + User + "\n" + "Subject: " + Subject + "\n"
    message = header + "\n" + Text + " \n\n"
    print("::: Sending mail to", Target + "...")
    smtpserver.sendmail(User, Target, message)
    smtpserver.close()
    print("E-Mail Service Closed")
    

#SendEMail("maturaarbeit17@gmail.com", "Hello", "This message was send via python")
