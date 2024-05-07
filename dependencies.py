from database import SessionLocal
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
import secrets
import string
import datetime

def get_current_time():
    return datetime.datetime.now()

def get_estimated_time(ptime,ctime=None):
    return ((datetime.datetime.now() if ctime is None else ctime)+datetime.timedelta(minutes=ptime))

def get_order_id():
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(6))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_time_compare(ctime):
    return datetime.datetime.now()>=ctime