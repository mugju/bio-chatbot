from fastapi import APIRouter

import predictor

router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
