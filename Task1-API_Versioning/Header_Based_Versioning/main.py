from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="Header Versioning API")


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


# Single endpoint reads version from header
@app.get("/api/users")
def get_users(x_api_version: str = Header(...)):

    if x_api_version == "v1":
        return get_users_v1()

    elif x_api_version == "v2":
        return get_users_v2()

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid API version"
        )
