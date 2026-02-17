from fastapi import APIRouter

router = APIRouter()

# Version 2 endpoint
@router.get("/users")
def get_users():
    return {
        "version": "v2",
        "users": [
            {
                "id": 1,
                "name": "Parth",
                "email": "parth@gmail.com"
            }
        ]
    }

# Version 2 endpoint with ID
@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "version": "v2",
        "user_id": user_id,
        "name": "Parth",
        "email": "parth@gmail.com"
    }
