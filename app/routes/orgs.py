from fastapi import APIRouter

router = APIRouter()

@router.get("/register")
def registerOrg():
    return {"message":"register org"}

@router.get("/login")
def loginOrg():
    return {"message":"login org"}
