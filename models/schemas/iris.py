from typing import Any, List

from pydantic import BaseModel, conlist


class Iris(BaseModel):
    data: List[conlist(float, min_length=4, max_length=4)]


class IrisPredictionResponse(BaseModel):
    prediction: List[int]
