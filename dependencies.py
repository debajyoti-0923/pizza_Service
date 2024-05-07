from database import SessionLocal
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
import secrets
import string
import datetime

def get_IST():
    return (datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=5,minutes=30))

def get_current_time():
    return get_IST()

def get_estimated_time(ptime,ctime=None):
    return ((get_IST() if ctime is None else ctime)+datetime.timedelta(minutes=ptime))

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