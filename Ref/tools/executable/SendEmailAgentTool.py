#SendEmailAgentTool

import smtplib
from email.mime.text import MIMEText

class SendEmailAgentTool:
    def __init__(self, smtp_server, smtp_port, smtp_username, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def get_description(self):
        return 'Send an email notification to a list of email addresses'

    def get_parameters(self):
        return {
            'subject': 'email subject',
            'body': 'html email body',
            'to': 'comma separated list of VALID email addresses',
            'cc': '(optional) comma separated list of VALID email addresses',
            'replyTo': '(optional) email address'
        }

    def execute(self, args):
        if 'subject' not in args or 'body' not in args or 'to' not in args:
            raise Exception('Missing required parameters.')

        to_addresses = args['to'].split(',')
        cc_addresses = args.get('cc', '').split(',') if args.get('cc') else []

        msg = MIMEText(args['body'], 'html')
        msg['Subject'] = args['subject']
        msg['From'] = self.smtp_username
        msg['To'] = ', '.join(to_addresses)
        if cc_addresses:
            msg['Cc'] = ', '.join(cc_addresses)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.smtp_username, to_addresses + cc_addresses, msg.as_string())
            return 'Email sent successfully to ' + ', '.join(to_addresses) + '.'
        except Exception as e:
            raise Exception(str(e))