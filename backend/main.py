import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
logging.basicConfig(level=logging.DEBUG)


app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__":
    import uvicorn
    logging.debug("Starting Uvicorn...")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")

