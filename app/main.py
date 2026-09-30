from fastapi import FastAPI

app = FastAPI(title="CI/CD Task API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "CI/CD Task API"}
