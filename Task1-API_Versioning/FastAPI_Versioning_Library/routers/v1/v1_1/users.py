from fastapi import APIRouter, Body
from fastapi_versioning import version

router = APIRouter()

# GET users - Version 1
@router.get("/users")
@version(1, 1)
def get_users():
    return {
        "version": "v1.1",
        "users": [
            {
                "id": 1,
                "name": "Parth"
            }
        ]
    }


# POST users - Version 1
@router.post("/users")
@version(1, 1)
def create_user(user: dict = Body(...)):
    return {
        "version": "v1.1",
        "message": "User created",
        "user": user
    }
