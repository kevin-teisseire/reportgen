import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os


class Mailer():
    """Send report email"""
    def __init__(self, config):
        load_dotenv()
        self.password = os.getenv("EMAIL_PASSWORD")
        self.smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.msg = MIMEMultipart()
        self.config = config
        self.smtp.login(self.config['email'], self.password)
        self.msg['From'] = self.config['email']
        self.msg['Subject'] = 'Your new expenses report'
   
    def send_message(self, html):
        if not self.config['recipient']:
            print("Please configure a recipient for the report : command = set --recipient 'email'")
            return
        elif not self.password:
            print('Please configure an application password on gmail and add it to your .env')
        else:
            self.msg['To'] = self.config['recipient']
        self.msg.attach(MIMEText(html, 'html'))
        self.smtp.send_message(self.msg)
        self.smtp.quit()
        print(f'\nReport successfully sent to {self.config['recipient']}\n')

