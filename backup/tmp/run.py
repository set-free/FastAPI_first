import uvicorn
from config import PORT, HOST, WORKERS

if __name__ == "__main__":
    uvicorn.run("test:app", host=HOST, port=int(PORT), reload=True, workers=int(WORKERS))
