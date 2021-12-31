from fastapi import FastAPI

from app.factory import create_app


app: FastAPI = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("manage:app", reload=True)
