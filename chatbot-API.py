import gradio as gr
from openai import OpenAI

model_name="openai/gpt-oss-20b:free"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)


def chat_with_ai(user_input, history, model_name):

    messages=[]
    
    for item in history:
        messages.append({
            "role": item["role"],
            "content": item["content"][0]["text"]
        })

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    return response.choices[0].message.content



iface = gr.ChatInterface(
    fn = lambda message, history: chat_with_ai(message, history, model_name),
    title= "AI Chatbot"
)

iface.launch()
