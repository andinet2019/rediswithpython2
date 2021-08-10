from flask import Flask
import redis
from rq import Queue
app=Flask(__name__)
#creates redis connection
r=redis.Redis()
#create task queue
q=Queue(connection=r)
from app import views
from app import tasks