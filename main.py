from fastapi import FastAPI
from pydantic import BaseModel
import settings

db = settings.client.proctoring
print(db.list_collection_names())
    
class User(BaseModel):
    email: str
    username: str
    password: str
    college: str

app = FastAPI()

@app.get("/collections")
async def db():
    return {"db":db.list_collection_names()}

@app.post("/register")
async def register(user: User):
    print(user.email)
    return user

@app.post("/login")
async def login():
    return {"response":"login endpoint"}


