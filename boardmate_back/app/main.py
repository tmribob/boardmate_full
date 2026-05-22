import asyncio

import typer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.db.init_db import init_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(api_router)


@app.get("/health")
async def health():
    return {"status": "ok"}


cli = typer.Typer()


@cli.command()
def db():
    asyncio.run(init_models())
    print("Done")


@cli.command()
def hello():
    print("Hello")


if __name__ == "__main__":
    cli()
