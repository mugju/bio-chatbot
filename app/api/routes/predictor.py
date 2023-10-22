import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from fastapi import APIRouter, HTTPException

from app.services.chatbot import BioChatBotHandler as chatbot
from app.models.prediction import (
    HealthResponse,
    MachineLearningResponse,
    MachineLearningDataInput,
)
router = APIRouter()


## Change this portion for other types of models
## Add the correct type hinting when completed

@router.get(
    "/check",
)
async def check():

    try:
        print("good")

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return HealthResponse()


@router.post(
    "/question",
    name="chat-bot:response-data",
)
async def predict(data_input):

    if not data_input:
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")
    try:
        data_point = data_input.get_np_array()

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return chatbot.create_answer(data_input)
