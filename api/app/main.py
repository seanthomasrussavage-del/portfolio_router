from fastapi import FastAPI
from core.src.service import health_check

app = FastAPI()


@app.get("/health")
def health():
    # Thin wrapper: call core, return primitive/serializable
    return {"status": health_check().status}
