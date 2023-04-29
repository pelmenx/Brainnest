''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib
from datetime import datetime
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
import schedule


def logging(msg, log, error=None):
    with open(log, "a") as f:
        curr_time = datetime.now().strftime("%H:%M:%S|%d/%m/%Y")
        status = f"FAILED - {error}" if error else "SUCCESS"
        f.write(f"{curr_time}; {msg['From']}; {msg['To']}; {status}\n")


def form_message(sender, receiver, file_path, log):
    msg = MIMEMultipart()
    msg.attach(MIMEText(f"Deer, {receiver}.\nHere is you daily report", 'plain'))

    msg['Subject'] = 'Test mail'
    msg['From'] = sender
    msg['To'] = receiver
    try:
        with open(file_path, 'r') as f:
            part = MIMEApplication(f.read(), Name=basename(file_path))
    except FileNotFoundError:
        logging(msg, log, "File Not Founded")
        return
    part['Content-Disposition'] = f'attachment; filename="{basename(file_path)}"'
    msg.attach(part)

    return msg


def send_mail(receivers, log):
    sender = 'very@important.corporation'
    for receiver, file_path in receivers.items():
        msg = form_message(sender, receiver, file_path, log)
        if not msg:
            continue
        try:
            smtp_object = smtplib.SMTP("smtp.mailtrap.io", 2525)
            smtp_object.login("1d3d73c9e53eed", "bf4f6a46ca22f5")
            smtp_object.sendmail(sender, receivers, msg.as_string())
        except smtplib.SMTPException:
            logging(msg, log, "Message not sent")
        else:
            logging(msg, log)


def main():
    receivers = {"Liam": "attachments/Emma.css",
                 "Noah": "attachments/Noah.css",
                 "Emma": "attachments/Emma.css",
                 "Levi": "attachments/Levi.css",
                 "Jack": "attachments/Jack.css",
                 "Owen": "attachments/Owen.css"}

    log_file = "log.txt"
    schedule.every().day.at("16:46").do(send_mail, receivers, log_file)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
