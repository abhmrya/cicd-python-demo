import os

from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def index():
    return {
        "message": "Hello from the CI/CD demo",
        "version": os.getenv("APP_VERSION", "dev"),
        "environment": os.getenv("APP_ENV", "local"),
    }


@app.get("/add")
def add(a: int, b: int):
    # FastAPI validates types automatically and returns 422 for bad input
    return {"result": a + b}