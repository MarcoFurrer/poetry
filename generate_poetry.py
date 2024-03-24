import openai

from api_key import API_KEY
import os
import json
from prompts import prompts
REPS_PER_PROMPT = 8 # Number of times to repeat each prompt must be power of 2

filename = "Noah.txt"
txt = open(filename)
text  = txt.read()

openai.api_key = API_KEY

for poem_num, prompt in enumerate(prompts):
  for rep in range(REPS_PER_PROMPT):
    response = openai.ChatCompletion.create(
        
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": prompt},
      ]
    )
    savefile = open(f"generated_poems/prompt{poem_num}rep{rep}.txt","w")
    savefile.write(response.choices[0].message.content)
    savefile.close()
    break