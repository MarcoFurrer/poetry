"""
Poetry Tournament Rating System
--------------------------------
Implements a tournament-style elimination system to find the best poem.
Compares poems pairwise using AI ratings across three categories:
- Content (Inhalt)
- Rhymes (Reime)  
- Style (Stil)
Winners advance to the next round until a champion emerges.
"""

import openai
from api_key import API_KEY
import os
import json
import random
import statistics

openai.api_key = API_KEY
# Configuration
directory = "generated_poems"
counter_json = 0

# Load and shuffle all poem files for random tournament brackets
files = os.listdir(directory)
random.shuffle(files)


def enter_json(filepath, content):
    """Save rating results to JSON file"""
    with open(filepath, 'w') as json_file:
        json.dump(content, json_file)
                    

def rate_poems(ratings_files_arr):
    """
    Rate poems pairwise using AI.
    Compares two poems at a time across three categories.
    """
    poems = []
    ratings = []
    
    # Load poem contents
    for file in ratings_files_arr:
        file = file.replace("poem", "prompt")
        if not file.endswith(".txt"):
            file += ".txt"
        txt = open(directory + "/" + file)
        text = txt.read()
        poems.append(text)
        txt.close()

    # Compare poems pairwise
    for i in range(0, len(poems), 2):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{files[i]}: {poems[i]}, {files[i+1]}: {poems[i+1]}\
                Gebe mir ein Rating von 1-10 mit einer Dezimalzahl von den beiden Gedichten gegeneinander im in diesem JSONFormat zurück: 'poemxrepx': [x,x,x], 'poemxrepx': [x,x,x]\
                Kategorie 1: Inhalt,\
                Kategorie 2: Reime,\
                Kategorie 3: Stil"
                },
            ]
        )
        print(response.choices[0].message.content)
        parsed_dict = json.loads(response.choices[0].message.content)
        ratings.append(parsed_dict)
        print(len(ratings))

    # Save this round's ratings
    enter_json(f"ratings/rating{counter_json}.json", ratings)
        
        
def win_poems(json_file_dir):
    """
    Determine winners from a round of ratings.
    Returns the poem with higher average score from each pair.
    """
    json_file = open(json_file_dir, "r")
    ratings = json.load(json_file)
    winners = []

    for rating in ratings:
        keys = list(rating.keys())
        values = list(rating.values())

        # Calculate average scores across three categories
        avrg0 = statistics.mean(values[0])
        avrg1 = statistics.mean(values[1])

        # Select winner with higher average
        if avrg0 > avrg1:
            winners.append(keys[0])
        else:
            winners.append(keys[1])
    
    return winners


# Tournament loop: continue until only one poem remains
while len(files) > 1:
    rate_poems(files)
    print("Round completed")
    files = win_poems(f"ratings/rating{counter_json}.json")
    counter_json += 1