from fastapi import FastAPI
from uvicorn import run
from app.routers.test_router import test_router


app = FastAPI(
    title="base",
    description="",
)

app.include_router(test_router)

def main() -> None:
    run(
        app,
        host='0.0.0.0',
        port=8080
    )