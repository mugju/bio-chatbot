from fastapi import APIRouter

import chatbot

router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
