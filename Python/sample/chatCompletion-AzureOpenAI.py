#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 1.0.0 or higher.

#pip install openai==0.14.3
#Incase ERROR openai not found, FIX by 
#   Enter Shift + Ctrl + P on Windows and Linux (Shift + Cmd + P on macOS) to open the Command Palette and click Python: Select Interpreter

import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = "https://i8h6a1s2a1.openai.azure.com/", 
  api_key="af49c7c3e293444db2513ec7cfd0e97c",  
  api_version="2024-02-15-preview"
)

message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},
                {"role":"user","content":"I have 5 oranges today, I ate 3 oranges last week. How many oranges do I have left?"}
                ]

completion = client.chat.completions.create(
  model="I8H6A1S2A1", # model = "deployment_name"
  messages = message_text,
  temperature=0.5,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion)
# Print the generated response
# print(completion.choices[0].text.strip())