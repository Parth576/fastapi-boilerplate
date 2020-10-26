from fastapi import APIRouter

router = APIRouter()

@router.get("/register")
def registerUser():
    return {"message":"register user"}

@router.get("/login")
def loginUser():
    return {"message":"login user"}
