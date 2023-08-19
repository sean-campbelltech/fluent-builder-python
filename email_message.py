class EmailMessage(object):
    def __init__(self):
        self._from = ""
        self._to = []
        self._cc = []
        self._bcc = []
        self._subject = ""
        self._body = ""
        self._attachments = []

    def set_from(self, from_address: str):
        self._from = from_address

    def set_to(self, to: []):
        self._to = to

    def get_to(self):
        return self._to

    def get_cc(self):
        return self._cc

    def get_bcc(self):
        return self._bcc

    def set_subject(self, subject: str):
        self._subject = subject

    def set_body(self, body: str):
        self._body = body

    def get_attachments(self):
        return self._attachments

    def send(self):
        print(
            f"Email successfully sent from {self._from} to {self._to} with subject {self._subject}"
        )
