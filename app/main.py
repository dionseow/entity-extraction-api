from fastapi import FastAPI
from lookup import LookUpService

app = FastAPI(title="Entity Pipeline")
lookup_service = LookUpService()


print(lookup_service.lookup("Hi I am a designer from xiaomi"))

@app.get("/")
def home():
    return "Hello World"
