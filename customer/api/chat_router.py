from  fastapi import APIRouter
from   customer.api.schemas import  ChatMessage,ChatObject,ChatRequest,ChatResponse


chat_router =   APIRouter()

@chat_router.post("/api/chat")
def chat(chat_request:chat_request ) -> ChatResponse:


    return ChatResponse(

        
    )