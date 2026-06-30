from fastapi import APIRouter
from langchain_groq import ChatGroq
import os
from langchain_core.messages import HumanMessage,AIMessage
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from app.database.chroma_db import get_vector_store
router = APIRouter()
load_dotenv()
api = os.getenv("GROQ_API_KEY")
chat_history = []
llm = ChatGroq(api_key=api,model='llama-3.3-70b-versatile',max_tokens=100)


@router.get('/chat')
async def chat(query: str):
    print('chat endpoint')
    global chat_history
    vector_store = get_vector_store()
    results = vector_store.similarity_search(query=query,k=3)
    print("=" * 50)
    print("QUERY:", query)
    print("Retrieved", len(results), "documents")

    for i, doc in enumerate(results):
     print(f"\n--- Document {i+1} ---")
     print(doc.page_content[:700])

    print("=" * 50)
    context = '\n'.join(doc.page_content for doc in results)
    history = "\n".join(
    f"{'User' if isinstance(msg, HumanMessage) else 'Assistant'}: {msg.content}"
    for msg in chat_history[-5:]
)
    prompt = f"""you are a helpful ai assitant. use only the provided context.if the answer in present try to answer from previous chats or tell user that u couldnt get it and ask them to be specific .'do not make up facts and dont say based on context or provided context just be natural,and if they dont anything related to pdf just act normal and act natural,conversation history:{history} context:{context},question:{query}"""
    def generate():
       chat_history.append(HumanMessage(content=query))

       full_answer = ""

       for chunk in llm.stream(prompt):
         full_answer += chunk.content
         yield chunk.content

       chat_history.append(AIMessage(content=full_answer))

    return StreamingResponse(
     generate(),
     media_type="text/plain"
)
    
