import openai

from api_key import API_KEY
import os
import json
import random
import statistics
openai.api_key = API_KEY
directory = "generated_poems"
counter_json = 0

files = os.listdir(directory)
random.shuffle(files)


def enter_json(filepath,content):
    with open(filepath, 'w') as json_file:
        json.dump(content, json_file)
                    

def rate_poems(ratings_files_arr):
    
    poems = []
    ratings = []
    
    for file in ratings_files_arr:
        file = file.replace("poem", "prompt")
        if not file.endswith(".txt"):
            file += ".txt"
        txt = open(directory+"/"+file)
        text  = txt.read()
        poems.append(text)
        txt.close()


    for i in range(0,len(poems),2):
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

    enter_json(f"ratings/rating{counter_json}.json", ratings)
        
        
        
def win_poems(json_file_dir):
    json_file = open(json_file_dir,"r")
    ratings = json.load(json_file)

    winners = []


    for rating in ratings:
        keys = list(rating.keys())
        values = list(rating.values())

        avrg0 = statistics.mean(values[0])
        avrg1 = statistics.mean(values[1])

        if avrg0 > avrg1:
            winners.append(keys[0])
        else:
            winners.append(keys[1])
    return winners







while len(files) > 1:
    rate_poems(files)
    print("yes")
    files = win_poems(f"ratings/rating{counter_json}.json")
    counter_json += 1