import smtplib
import ssl

from src.notification_message import get_message

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "utm.geoawareness@gmail.com"
gmail_generated_app_password = "fosgnogvrbeszhnf"

receiver_email = "p.a.mistani@gmail.com"  # Enter receiver address
# message = """\
# Subject: Intrusion Alert

# A drone entered your region of interest. 

# Drone Awareness notification service.
# """




def send_email_alert(receiver_email):
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    with smtplib.SMTP(smtp_server, port) as server:
        try:
            message = get_message()
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, gmail_generated_app_password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
