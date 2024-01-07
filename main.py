from fastapi import FastAPI
from modules.sentiment_analysis.sentiment_analysis import router as sentiment_analysis_router
from modules.sentiment_analysis.pcr_data import router as pcr_data_router

app = FastAPI()

app.include_router(sentiment_analysis_router)
app.include_router(pcr_data_router)