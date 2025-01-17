from des.models import DynamicEmailConfiguration
from django.core.mail import EmailMultiAlternatives


class ReportMailSender:

    def __init__(self, admins, subject, body):
        self.admins = admins
        self.subject = subject
        self.body = body
        self.attachments = []

    def send(self):
        emails = self.admins.get_emails()

        config = DynamicEmailConfiguration.get_solo()
        sender_email = config.from_email
        mail = EmailMultiAlternatives(self.subject, self.body, from_email=sender_email, to=emails,
                                      bcc=[sender_email])
        mail.attach_alternative(self.body, 'text/html')

        for attachment_args in self.attachments:
            mail.attach(*attachment_args)

        mail.send()

    def add_csv_attachment(self, file_name, body):
        self.attachments.append((file_name, body, 'text/csv'))

    def add_plaintext_attachment(self, file_name, body):
        self.attachments.append((file_name, body, 'text/plain'))
