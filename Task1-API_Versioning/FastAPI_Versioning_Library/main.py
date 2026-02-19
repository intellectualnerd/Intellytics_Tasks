from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
# Import version routers
from routers.v1.v1_0 import router as v1_0_router
from routers.v1.v1_1 import router as v1_1_router

# Create FastAPI app
app = FastAPI(
    title="My Versioned API",
    description="Example of URL Versioning"
)

app.include_router(v1_0_router)
app.include_router(v1_1_router)
# enable versioning
app = VersionedFastAPI(
    app,
    version_format="{major}.{minor}",
    prefix_format="/api/v{major}.{minor}",
)