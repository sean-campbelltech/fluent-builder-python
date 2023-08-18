class EmailMessage(object):

    def __init__(self):
        self.__from = ""
        self.__to = []
        self.__cc = []
        self.__bcc = []
        self.__subject = ""
        self.__body = ""
        self.__attachments = []

    def set_from(self, from_address: str):
        self.__from = from_address

    def set_to(self, to: []):
        self.__to = to

    def get_to(self):
        return self.__to

    def get_cc(self):
        return self.__cc

    def get_bcc(self):
        return self.__bcc

    def set_subject(self, subject: str):
        self.__subject = subject

    def set_body(self, body: str):
        self.__body = body

    def get_attachments(self):
        return self.__attachments

    def send(self):
        print(f"Email successfully sent from {self.__from} to {self.__to} with subject {self.__subject}")
