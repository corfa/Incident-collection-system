from fastapi import HTTPException
from fastapi.params import Header
from starlette import status
from starlette.websockets import WebSocketDisconnect



from db.session_db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



