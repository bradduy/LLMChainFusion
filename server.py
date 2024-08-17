import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
from utils.check_gpu import can_run_model
# pip install fastapi uvicorn ollama
# curl -X POST "http://localhost:8000/chat" \
    #  -H "Content-Type: application/json" \
    #  -d '{"mode": "1", "message": "What is error for this array in python? conversation = [1,2,3,"}'
app = FastAPI()

class ChatRequest(BaseModel):
    mode: str
    message: str

class ChatResponse(BaseModel):
    response: str

default_model = 'llama3.1'

modes = {
    '1': 'Coding Assistant',
    '2': 'Sentiment Analysis',
    '3': 'Question Answering'
}

init_messages = {
    '1': 'You are an AI coding assistant expert in various programming languages and software development practices.',
    '2': 'You are an AI sentiment analyzer. Analyze the sentiment of the given text and categorize it as positive, negative, or neutral.',
    '3': 'You are an AI assistant specialized in answering questions on a wide range of topics.'
}

conversations = {}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if request.mode not in modes:
        raise HTTPException(status_code=400, detail="Invalid mode")

    if request.mode not in conversations:
        init_mess = init_messages[request.mode]
        response = ollama.chat(model=default_model, messages=[
            {
                'role': 'system',
                'content': init_mess,
            },
        ])
        conversations[request.mode] = [
            {'role': 'system', 'content': init_mess},
            {'role': 'assistant', 'content': response['message']['content']}
        ]

    user_input = request.message
    if request.mode == '2':
        user_input = f"Analyze the sentiment of the following text: '{user_input}'"
    elif request.mode == '3':
        user_input = f"Please answer the following question: {user_input}"

    response = ollama.chat(model=default_model, messages=conversations[request.mode] + [
        {
            'role': 'user',
            'content': user_input,
        },
    ])

    conversations[request.mode].append({'role': 'user', 'content': user_input})
    conversations[request.mode].append({'role': 'assistant', 'content': response['message']['content']})

    return ChatResponse(response=response['message']['content'])

@app.on_event("startup")
async def startup_event():
    if not can_run_model(model_name=default_model):
        print(f'Error: Not enough GPU memory to run the {default_model} model')
        sys.exit(1)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)