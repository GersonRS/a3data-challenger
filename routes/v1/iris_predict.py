from fastapi import APIRouter

import models.ml.classifier as clf
from models.schemas.iris import Iris, IrisPredictionResponse

app_iris_predict_v1 = APIRouter()


@app_iris_predict_v1.post('/iris/predict',
                          tags=["Predictions"],
                          response_model=IrisPredictionResponse,
                          description="Get a classification from Iris")
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()
    return {"prediction": prediction}

