from fastapi import FastAPI

# Import version routers
from routers.v1.v1_0 import router as v1_0_router
from routers.v1.v1_1 import router as v1_1_router
from routers.v2 import router as v2_router

# Create FastAPI app
app = FastAPI(
    title="My Versioned API",
    description="Example of URL Versioning",
    version="1.0"
)

# Register Version 1 routes
app.include_router(v1_0_router, prefix="/api/v1.0")


"""
Version inheritance pattern:

FastAPI checks routes in registration order.
First matching route is used.

So we register v1.1 first (new endpoints),
then v1.0 as fallback for endpoints not present in v1.1.

Result:
- If endpoint exists in v1.1 → use v1.1
- Else → fallback to v1.0
"""

#new paths
app.include_router(v1_1_router, prefix="/api/v1.1")
#privious paths will be the same
app.include_router(v1_0_router, prefix="/api/v1.1")


# Register Version 2 routes
app.include_router(v2_router, prefix="/api/v2")