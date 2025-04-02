
from typing import Annotated, Any, Dict, List, Optional 
import os
from load_dotenv import load_dotenv
import speech_recognition as sr
from concurrent import futures
from fastapi.openapi.utils import get_openapi
from fastapi import (
    FastAPI, 
    Header,
    HTTPException, 
    Request, 
    status,
    responses
)
# from core.control.cors import EnvironmentController as EC
from fastapi.middleware.cors import CORSMiddleware
result : Dict[List, Any] = None
bet : str = os.getenv("APP_ROUTE")
app = FastAPI(
        root_path=bet
)
context=load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
def custom_openapi()->Dict[str,Any]:
        if app.openapi_schema:
                return app.openapi_schema
        openapi_schema=get_openapi(
                title="Graffiti - Signals AcoustIQ Interface: \
                        Audio Transcription Services Layer", 
                version="1.0.0", 
                summary="""
                System controls and scalable architecture supporting ingest, 
                classification and executive function for sensitive and regulated 
                data sources. The system supports control of audio input to devices
                on network and promotes a basic means to draw and deliver audio input
                to a backend normalization engine.
                """,
                description="Backend data services to handle multi-format data \
                input and workflow management for complex AI Assisted data \
                transformation and control",
                routes=app.routes,
        )
        app.openapi_schema=openapi_schema
        return app.openapi_schema
app.openapi= custom_openapi

@app.get("/api/vi/unit/health",
        tags=["AcoustIQ Graffiti"],
        responses={
                200: {'description': "OK"}, 
                401: {'description': "Unauthorized - Failed Authentication"}, 
                422: {'description': "Malformed Input (Check Types & Values)"}
            }
         
         )
async def health_check():
        return {"status": "OK"}



@app.get("/api/v1/audio/input-test",
        tags=["AcoustIQ Graffiti"],
        responses={
                200: {'description': "OK"}, 
                401: {'description': "Unauthorized - Failed Authentication"}, 
                422: {'description': "Malformed Input (Check Types & Values)"}
            }
        )
async def base_listen_test():
        import logging
        logging.basicConfig(level=logging.DEBUG)
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        r = sr.Recognizer()
        devices = sr.Microphone.list_microphone_names()
        filedata = open("./in/devices_output.txt", "w")
        with sr.Microphone(device_index=0) as source:
            print("Speak now...")
            audio = r.listen(source, timeout=100)
        try:
                text = r.recognize_google(audio)
                filedata.write(text)
        except sr.UnknownValueError:
                print("Could not understand audio")
        except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return {
                "status": "Recording Complete", 
                "devices": devices,
                "text": text
        }