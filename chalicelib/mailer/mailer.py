import smtplib
import chalicelib.constants as constants


class Mailer:

    def sendEmail(self, email_content):
        gmail_user = constants.GMAIL_USERNAME
        gmail_app_password = constants.GMAIL_USERNAME
        target_mail_list = constants.TARGET_MAIL

        email_text = self.create_email_message(email_content, gmail_user, target_mail_list)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(gmail_user, target_mail_list, email_text)
            server.close()
        except:
            print('Unable to connect to Gmail')

    def create_email_message(self, email_content, gmail_user, target_mail_list):
        sent_from = gmail_user
        to = target_mail_list
        subject = 'Cheap NCAV Stocks'
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, email_content)
        return email_text
