from fastapi import APIRouter

# Create router object
router = APIRouter()

# Version 1 endpoint
@router.get("/users")
def get_users():
    return {
        "version": "v1.0",
        "users": ["Parth", "Rahul", "Amit"]
    }

# Version 1 endpoint with ID
@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "version": "v1.0",
        "user_id": user_id,
        "name": "Parth"
    }
