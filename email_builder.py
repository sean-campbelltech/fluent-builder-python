from email_message import EmailMessage


class EmailBuilder:
    def __init__(self):
        self.email = EmailMessage()

    def add_from(self, from_address: str):
        self.email.set_from(from_address)
        return self

    def add_to(self, to: str):
        self.email.get_to().append(to)
        return self

    def add_attachments(self, cc: str):
        self.email.get_cc().append(cc)
        return self

    def add_cc(self, cc: str):
        self.email.get_cc().append(cc)
        return self

    def add_bcc(self, bcc: str):
        self.email.get_bcc().append(bcc)
        return self

    def with_subject(self, subject: str):
        self.email.set_subject(subject)
        return self

    def with_body(self, body: str):
        self.email.set_body(body)
        return self

    def add_attachment(self, attachment: str):
        self.email.get_attachments().append(attachment)
        return self

    def build(self):
        return self.email
