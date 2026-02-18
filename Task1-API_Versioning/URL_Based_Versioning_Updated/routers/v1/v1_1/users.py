from fastapi import APIRouter

# Create router object
router = APIRouter()

# Version 1 endpoint
@router.get("/users")
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


