"""
Poetry Optimization
-------------------
Iteratively refines poems using AI optimization.
Takes existing poems and asks AI to improve them,
creating progressively better versions.
"""

import openai
from api_key import API_KEY

openai.api_key = API_KEY

# Optimize poems through 10 iterations
for counter in range(0, 10):
    # Read current version
    file = open(f"optimized_poem/optimized{counter}.txt", "r")
    poem = file.read()
    
    # Ask AI to optimize the poem
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": poem},
            {"role": "user", "content": "Optimiere das Gedicht."}
        ]
    )
    
    # Save optimized version
    savefile = open(f"optimized_poem/optimized{counter+1}.txt", "w")
    savefile.write(response.choices[0].message.content)
    savefile.close()
    
    print(f"Optimized version {counter+1} created")