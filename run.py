import uvicorn

if __name__ == "__main__":
    uvicorn.run("test:app", host="0.0.0.0", port=int(8000), reload=True, workers=int(4))
