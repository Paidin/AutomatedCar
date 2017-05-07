# Send computer's current ip-address as email to 'maturaarbeit17@gmail.com'

import os
import EMail

Target = "maturaarbeit17@gmail.com"
Subject = "RobotBot: Notification"

os.system("hostname -I > IP-Address.txt")

file = open("IP-Address", "rt")
IP = file.read()
file.close()

EMail.SendEMail(Target, Subject, "This is RobotBot's current IP: " + IP)
