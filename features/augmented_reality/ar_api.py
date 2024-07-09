from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ARModel(BaseModel):
    id: int
    type: str
    data: list

@app.post("/generate")
async def generate_ar_model(ar_model: ARModel):
    # Call AR ML model to generate AR model
    ar_model = await ar_ml_model.generate_ar_model(ar_model)
    return {"ar_model": ar_model}
