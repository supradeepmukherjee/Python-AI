from fastapi import FastAPI,Query
from .client.rqClient import queue
from .queues.worker import processQuery

app=FastAPI()

@app.get('/')
def root():
    return {'status':'running'}

@app.post('/chat')
def chat(query:str=Query(...,description='The query of user')):
    job=queue.enqueue(processQuery,query)
    return {
        'status':'queued',
        'jobId':job.id
    }

@app.get('/job-status')
def getResult(jobId:str=Query(...,description='Job ID')):
    job=queue.fetch_job(jobId)
    result=job.return_value()
    return {'result':result}        