import openai
from api_key import API_KEY
import os
import json

filename = "Noah.txt"
txt = open(filename)
text  = txt.read()

openai.api_key = API_KEY
"""client = OpenAI(
    api_key=API_KEY
)"""

prompt = f"Schreibe ein Gedicht über {filename[:-3]} mit folgenden Informationen: \
    {text} am Anfang bitte mit bösen Satzen und nachher am Schluss herzlich"
response = openai.ChatCompletion.create(
    
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt},
  ]
)
savefile = open("chatgptpoem.txt","w")
savefile.write(response.choices[0].message.content)
savefile.close()