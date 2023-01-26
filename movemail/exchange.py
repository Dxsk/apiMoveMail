from exchangelib import (
    DELEGATE,
    Credentials,
    Account,
)

from .settings import email


class ExchangeConnector:
    
    def __init__(self):
        self.identify: str = ''
        self.login: str = email.get('login')
        self.password: str = email.get('password')
        self.credentials: Credentials = Credentials(
            self.login,
            self.password,
        )
        self.mails: object or None = ''
        self.account: Account = Account(
            self.login,
            credentials=self.credentials,
            autodiscover=True,
            access_type=DELEGATE,
        )
        
    def get_all(self) -> bool:
        """Retrieves all mails and stocks in the object..
        
        :return: Bool
        """
        response: bool = False
        self.mails = self.account.inbox.all()
        if self.mails:
            response = True
        return response
    
    def move_to_right_folder(self) -> bool:
        """Function to move the mail to the corresponding folder.
        
        :return: Bool
        """
        response = False
        to_folder = self.account.inbox / 'test'  # Hard written folder for the POC
        if self.mails:
            for mail in self.mails.filter(subject__contains=self.identify):
                mail.move(to_folder=to_folder)
                response = True
        
        self.mails = None
        return response
