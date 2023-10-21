
from fastapi import APIRouter, HTTPException

from core.config import INPUT_EXAMPLE
from services.predict import MachineLearningModelHandlerScore as model
from models.prediction import (
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
async def predict(data_input: MachineLearningDataInput):

    if not data_input:
        raise HTTPException(status_code=404, detail="'data_input' argument invalid!")
    try:
        data_point = data_input.get_np_array()
        prediction = get_prediction(data_point)

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return MachineLearningResponse(prediction=prediction)