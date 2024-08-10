from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from simple import generate, models

app = FastAPI()

@app.get('/healthz')
async def health():
    return {
        "application": "Simple LLM API",
        "message": "running successfully"
    }
    
@app.post('/chat')
async def generate_chat(request: Request):
    query = await request.json()
    model = query["model"]
    
    if model not in models:
        return {
            "error": "You did not pass a correct Model"
        }
        
    response = generate(model, query["question"], query["temperature"])
    
    return {
        "status": "success",
        "response": response
    }
    
    
if __name__ == "__main__":
    import uvicorn
    print("Starting LLM API")
    uvicorn.run(app, host="0.0.0.0", reload=True)