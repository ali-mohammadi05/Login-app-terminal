from random import randint
import smtplib
from email.message import EmailMessage



otp = ""
for count in range(6):
    otp += str(randint(0,9))
    
    
def send_otp(email):
    try:
        server = smtplib.SMTP("smtp.gmail.com" , 587)
        server.starttls()
        from_email = "rodrigez.v1384@gmail.com"
        server.login(from_email , "dupr xhhn xtif oigh")
        email_message = EmailMessage()
        email_message['subject'] = "Login App Email Verificaton"
        email_message['from'] = from_email
        email_message['to'] = email
        email_message.set_content("Your verification code is: " + otp)
        server.send_message(email_message)
    except:
        print("\033[32minternet connection has problem!\033[0m")
        while True:
            check = input("if the problem was gone,press enter to get verification code:")
            if not check:
                send_otp(email)
                break
            else:
                print("please press enter!")
                continue