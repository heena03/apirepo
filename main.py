from fastapi import FastAPI
from pydantic import BaseModel  
from dotenv import load_dotenv 
import os 
from openai import OpenAI

load_dotenv()# Load environment variables from .env file

Client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))#object of OpenAI class

app = FastAPI() #FastAPI instance

class ChatRequest(BaseModel):
    message: str
    
@app.post("/chat") #post get to communicate with the model
async def chat(request: ChatRequest):
    
        response = Client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[ 
                {"role": "user", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.message}
            ]          
        )
        reply = response.choices[0].message.content
        return {"reply": reply}
     