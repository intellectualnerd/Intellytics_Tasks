from fastapi import FastAPI

# Import version routers
from routers.v1 import router as v1_router
from routers.v2 import router as v2_router

# Create FastAPI app
app = FastAPI(
    title="My Versioned API",
    description="Example of URL Versioning",
    version="1.0"
)

# Register Version 1 routes
app.include_router(v1_router, prefix="/api/v1")

# Register Version 2 routes
app.include_router(v2_router, prefix="/api/v2")