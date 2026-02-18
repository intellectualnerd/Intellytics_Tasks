from fastapi import APIRouter

from .users import router as users_router
from .orders import router as orders_router

router = APIRouter()

router.include_router(users_router)
router.include_router(orders_router)
