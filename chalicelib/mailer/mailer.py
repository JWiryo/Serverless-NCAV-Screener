import smtplib
import chalicelib.constants as constants

from email.message import EmailMessage


class Mailer:

    def sendEmail(self, email_content):
        gmail_user = constants.GMAIL_USERNAME
        gmail_app_password = constants.GMAIL_APP_PASSWORD
        target_mail_list = constants.TARGET_MAIL

        email_text = self.create_email_message(email_content, gmail_user, target_mail_list)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(gmail_user, gmail_user, email_text.as_string())
            server.close()
        except:
            print('Unable to connect to Gmail')

    @staticmethod
    def create_email_message(email_content, gmail_user, target_mail_list):
        msg = EmailMessage()
        msg['Subject'] = 'Cheap NCAV Stocks'
        msg['From'] = gmail_user
        msg['To'] = target_mail_list

        email_text = """\
        %s
        """ % email_content

        msg.set_content(email_text)
        return msg
