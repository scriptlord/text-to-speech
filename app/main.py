from fastapi import FastAPI, HTTPException
from app.config import AWS_REGION, validate_aws_credentials

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        validate_aws_credentials()
    except EnvironmentError as e:
        print(f"Configuration Error: {str(e)}")
        raise

@app.get("/")
def read_root():
    return {"message": "FastAPI TTS service is running", "aws_region": AWS_REGION}
