import smtplib

class EmailSender:
    def __init__(self, sender_email, sender_password, receiver_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def send_email(self, subject, body):
        message = f'Subject: {subject}\n\n{body}'
        with smtplib.SMTP('smtp.163.com', 587) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, message)
