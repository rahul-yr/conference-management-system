from fastapi import FastAPI
from api.conferences.routes import users_router

app = FastAPI()

# adding users routers
app.include_router(users_router, prefix="/api")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
