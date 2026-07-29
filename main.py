from fastapi import FastAPI
from routers.complaints import router as complaints_router 
app = FastAPI()
app.include_router(complaints_router)
@app.get("/")
def home():
    return {"message": "Backend is Working!"}