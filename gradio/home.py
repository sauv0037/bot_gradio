import gradio as gr
import apibot
import symfonybot
import dockerbot
import keycloakbot

demo = gr.TabbedInterface(
    [
        apibot.chat_interface,
        symfonybot.chat_interface,
        dockerbot.chat_interface,
        keycloakbot.chat_interface
    ], 
    [
        "ApiPlatform",
        "Symfony",
        "Docker",
        "Keycloak"
    ]
)

demo.launch(share=True, server_name="0.0.0.0", server_port=8000)