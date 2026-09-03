from fastapi import FastAPI

app = FastAPI(title="FlowPipe Sample App")


@app.get("/")
def read_root():
    return {"message": "Hello from the FlowPipe sample app", "version": "1.1.0"}


@app.get("/health")
def health():
    return {"status": "ok"}
