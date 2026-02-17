from fastapi import FastAPI, Query, HTTPException

app = FastAPI(title="Query Versioning API")


# Version 1 logic
def get_users_v1():
    return {
        "version": "v1",
        "users": ["Parth", "Rahul"]
    }


# Version 2 logic
def get_users_v2():
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


# Single endpoint handles both versions
@app.get("/api/users")
def get_users(version: str = Query(..., description="API version")):

    if version == "v1":
        return get_users_v1()

    elif version == "v2":
        return get_users_v2()

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid API version"
        )
