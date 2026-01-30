from langchain.memory import ConversationBufferMemory
from llm import run_llm

memory = ConversationBufferMemory()

def chat_with_ai(prompt):
    memory.chat_memory.add_user_message(prompt)
    reply = run_llm(prompt)
    memory.chat_memory.add_ai_message(reply)
    return reply
