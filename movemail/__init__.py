import json

from fastapi import (
    FastAPI,
    Body,
    Response,
    Depends,
)
from fastapi.middleware.cors import (
    CORSMiddleware
)

from .settings import app
from .exchange import ExchangeConnector


documents: dict = app.get('documents')
api: FastAPI = FastAPI(
    docs_url=documents.get('swagger'),
    redoc_url=documents.get('redoc')
)

origins: list = app.get('securities').get('origins')
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['POST'],
)


@api.post('/')
def move_mail(
    response: Response,
    identity: dict = Body(
        media_type='application/json',
    ),
):
    """Function to browse the mail in the box,
    and move the mail corresponding to the id passed by the user.
    
    :param response: The object that is used to modify the response content to the client
    :param identify: The input that is used to identify the target mail to be moved.
    
    :return: {"Information message"}
    """
    identity = identity.get('identity')
    response.content = {'No mail found.'}
    response.status_code = 404

    if identity:
        exchange = ExchangeConnector()
        exchange.identify = identify
        
        # Check, if the mails are fetched and the mail has been moved.
        if exchange.get_all() and exchange.move_to_right_folder():
            response.content = {'Mail correctly moved.'}
            response.status_code = 200
        else:
            # Otherwise set the 'mails' variable to None.
            # Because a lot of mail can be loaded
            exchange.mails = None

    return "{}".format(response.content)
