# # Example: reuse your existing OpenAI setup
# from openai import OpenAI

# # Point to the local server
# client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# completion = client.chat.completions.create(
#     model="Llama-2-7B-Chat-GGUF",
#   messages=[
#     {"role": "system", "content": "Always answer in rhymes."},
#     {"role": "user", "content": "Introduce yourself."}
#   ],
#   temperature=0.7,
# )

# print(completion.choices[0].message)

#######################################################################################################################################

# # Chat with an intelligent assistant in your terminal
# from openai import OpenAI

# # Point to the local server
# client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# history = [
#     {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
#     {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
# ]

# while True:
#     completion = client.chat.completions.create(
#         model="Llama-2-7B-Chat-GGUF",
#         messages=history,
#         temperature=0.7,
#         stream=True,
#     )

#     new_message = {"role": "assistant", "content": ""}
    
#     for chunk in completion:
#         if chunk.choices[0].delta.content:
#             print(chunk.choices[0].delta.content, end="", flush=True)
#             new_message["content"] += chunk.choices[0].delta.content

#     history.append(new_message)
    
#     # Uncomment to see chat history
#     import json
#     gray_color = "\033[90m"
#     reset_color = "\033[0m"
#     print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
#     print(json.dumps(history, indent=2))
#     print(f"\n{'-'*55}\n{reset_color}")

#     print()
#     history.append({"role": "user", "content": input("> ")})

    #######################################################################################################################################
# C:\law-doc\OpenAI\rag\sourceFiles\tci-1.png
# Adapted from OpenAI's Vision example 
from openai import OpenAI
import base64
import requests

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Ask the user for a path on the filesystem:
path = input("Enter a local filepath to an image: ")

print(path)

# Read the image and encode it to base64:
base64_image = ""
try:
  image = open(path.replace("'", ""), "rb").read()
  base64_image = base64.b64encode(image).decode("utf-8")
except:
  print("Couldn't read the image. Make sure the path is correct and the file exists.")
  exit()

completion = client.chat.completions.create(
        model="Llama-2-7B-Chat-GGUF",
  messages=[
    {
      "role": "system",
      "content": "This is a chat between a user and an assistant. The assistant is helping the user to describe an image.",
    },
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Whats in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
  max_tokens=1000,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)

#######################################################################################################################################