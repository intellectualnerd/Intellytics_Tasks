from fastapi import APIRouter, Body
from fastapi_versioning import version

router = APIRouter()

# GET users - Version 1
@router.get("/users")
@version(1, 0)
def get_users():
    return {
        "version": "v1",
        "users": ["Parth", "Raj"]
    }


# POST users - Version 1
@router.post("/users")
@version(1, 0)
def create_user(user: dict = Body(...)):
    return {
        "version": "v1",
        "message": "User created",
        "user": user
    }
