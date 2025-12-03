import gradio as gr
from mistralai import Mistral
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)

def chatbot_conversation(message, chat_history=None):
    if chat_history is None:
        chat_history = []

    try:
        mistral_messages = [
            {"role": msg["role"], "content": msg["content"]} for msg in chat_history
        ]
    except KeyError as e:
        raise ValueError(f"chat_history mal formaté, manque la clé : {e}")

    mistral_messages.append({"role": "user", "content": message})

    chat_response = client.agents.complete(
        agent_id="ag:fe8dcc97:20250330:maxibot-keycloak:d365748d",
        messages=mistral_messages,
    )
    response = chat_response.choices[0].message.content

    return response

chat_interface = gr.ChatInterface(
    fn=chatbot_conversation,
    type="messages",
    title="Keycloak Bot 🤖",
    description="Posez vos questions sur Keycloak. Ce chatbot est alimenté par Mistral.",
)
