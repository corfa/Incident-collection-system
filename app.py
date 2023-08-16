import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.session_db import check_db_connect
from routers import problems, finds


class App:

    """Class for running a FastAPI application on a specified host and port.

    Args:
        host (str): The host on which the application will be run.
        port (int): The port on which the application will be run.

    Attributes:
        host (str): The host for running the application.
        port (int): The port for running the application.
        server (FastAPI): An instance of the FastAPI application.

    """
    
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server = FastAPI()
        self.server.add_middleware(CORSMiddleware,
                                   allow_origins=["*"],
                                   allow_credentials=True,
                                   allow_methods=["*"],
                                   allow_headers=["*"],
                                   )

    def run(self):
        try:
            check_db_connect()
            self.server.include_router(problems.router)
            self.server.include_router(finds.router)
            uvicorn.run(self.server, host=self.host, port=self.port)
        except Exception as e:
            raise e