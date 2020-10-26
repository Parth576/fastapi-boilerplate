from fastapi import FastAPI 
from pydantic import BaseModel
import settings
from app.routes import users, orgs

db = settings.client.proctoring

app = FastAPI()

app.include_router(users.router, prefix="/users",tags=["users"])
app.include_router(orgs.router, prefix="/orgs",tags=["orgs"])


