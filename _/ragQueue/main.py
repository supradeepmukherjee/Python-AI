from .server import app
import uvicorn

def main():
    uvicorn.run(app,port=6379,host='localhost')

main()