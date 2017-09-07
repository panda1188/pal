#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("harshadiv11@gmail.com","")
message = "wamt to meet up "
s.sendmail("harshadiv11@gmail.com","harshadiv11@gmail.com",message)
s.quit()
