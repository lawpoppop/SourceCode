# not working for azure open ai
from openai import OpenAI
import gradio as gr
from openai import AzureOpenAI

api_key="af49c7c3e293444db2513ec7cfd0e97c" # Replace with your key
# client = OpenAI(api_key=api_key)

client = AzureOpenAI(
  azure_endpoint = "https://i8h6a1s2a1.openai.azure.com/", 
  api_key="af49c7c3e293444db2513ec7cfd0e97c",  
  api_version="2024-02-15-preview"
)

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    response = client.chat.completions.create(model='I8H6A1S2A1',
    messages= history_openai_format,
    temperature=1.0,
    stream=True)

    print(response)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message

gr.ChatInterface(predict).launch()