# This is the main entry point of the application. From here, we import the FastAPI app defined in app.py and run it using uvicorn.

from app.app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)