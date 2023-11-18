from fastapi import APIRouter

import chatbot

router = APIRouter()
router.include_router(chatbot.router, tags=["predictor"], prefix="/v1")
