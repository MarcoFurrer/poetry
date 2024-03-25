import openai
from api_key import API_KEY
openai.api_key = API_KEY


for counter in range(0,10):
    file = open(f"optimized_poem/optimized{counter}.txt", "r")
    poem = file.read()
    
    response = openai.chat.completions.create(
            
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": poem},
            {"role": "user", "content": "Optimiere das Gedicht."}
        ]
        )
    savefile = open(f"optimized_poem/optimized{counter+1}.txt","w")
    savefile.write(response.choices[0].message.content)
    savefile.close()