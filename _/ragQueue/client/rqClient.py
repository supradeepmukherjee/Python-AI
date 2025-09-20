from dotenv import load_dotenv
import os
from redis import Redis
from rq import Queue

load_dotenv()

queue= Queue(connection=Redis(
    host=os.getenv('REDIS_URL') or '',
    port=19090,
    decode_responses=False,
    username="default",
    password="4XVSAqQVNddmp27LsANyc1uK4c4vXZMM",
))