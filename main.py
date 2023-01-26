import uvicorn

import movemail  # noqa
from movemail.settings import (
    app
)

if __name__ == '__main__':

    if app.get('debug'):
        reload: bool = True
        log_level: str = 'info'
    else:
        reload: bool = False
        log_level: str = 'error'
    
    uvicorn.run(
        "movemail:api",
        port=app.get('port'),
        reload=reload,
        log_level=log_level,
    )
