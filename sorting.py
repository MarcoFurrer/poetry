import json
import statistics

def win_poems():
    json_file = open("ratings.json","r")
    ratings = json.load(json_file)

    winners = []


    for rating in ratings:
        keys = list(rating.keys())
        values = list(rating.values())

        avrg0 = statistics.mean(values[0])
        avrg1 = statistics.mean(values[1])

        if avrg0 > avrg1:
            winners.append(keys[0])
            print("Yes")
        else:
            winners.append(keys[1])
    