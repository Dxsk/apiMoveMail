from os import getenv

from dotenv import (
    load_dotenv,
    find_dotenv
)
load_dotenv(find_dotenv())

# App Settings
true_list = ('True', 'true', True)
app: dict = {
    'debug': True if getenv('DEBUG') in true_list else False,
    'port': getenv('APP_PORT') or 8000,
    'securities': {
        'origins': [
            'http://127.0.0.1',
            'http://127.0.0.1:8000',
            'https://127.0.0.1',
            'https://127.0.0.1:8000',
        ],
    },
    'documents': {
        'swagger': None,
        'redoc': None,
    }
}
if app.get('debug') in true_list:
    app['documents']['swagger'] = '/docs'
    app['documents']['redoc'] = '/redoc'

# Email Settings
email: dict = {
    'login': getenv('EMAIL_LOGIN') or '',
    'password': getenv('EMAIL_PASSWORD') or '',
}
