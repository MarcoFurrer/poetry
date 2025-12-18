"""
AI Poetry Generator
-------------------
Generates multiple variations of German poems about a person using OpenAI GPT-3.5.
Reads facts from a text file and creates 64 poems (8 prompts × 8 repetitions each).
"""

import openai
from api_key import API_KEY
import os
import json

# Configuration
REPS_PER_PROMPT = 8  # Number of times to repeat each prompt (must be power of 2 for tournament)

# Load person's facts from file
filename = "Noah.txt"
txt = open(filename)
text = txt.read()

# Initialize OpenAI API
openai.api_key = API_KEY
# Define 8 different creative prompts for poem generation
prompts = [
    # Prompt 0: Standard poem with mean-to-kind emotional arc
    f"Schreibe ein Gedicht über {filename[:-3]} mit folgenden Informationen: \
    {text}, am Anfang bitte mit bösen Satzen und nachher am Schluss herzlich",

    
    # Prompt 1: Well-rhymed poem with mean-to-kind emotional arc
    f"Schreibe einen Gedicht mit guten Reimen über {filename[:-3]} mit folgenden Information: \
    {text} am Anfang bitte mit bösen Satzen und nachher am Schluss herzlich",

    # Prompt 2: Well-rhymed birthday poem
    f"Schreibe einen Gedicht mit guten Reimen über {filename[:-3]} mit folgenden Information: \
    {text} , so dass ich es an einem Geburtstag vortragen kann",

    
    # Prompt 3: End-rhymed poem with mean-to-kind emotional arc
    f"Schreibe einen Gedicht mit guten Reimen am Ende der Zeile über {filename[:-3]} mit folgenden Information: \
    {text} , am Anfang bitte mit bösen Satzen und nachher am Schluss herzlich",

    # Prompt 4: End-rhymed birthday poem
    f"Schreibe einen Gedicht mit guten Reimen am Ende der Zeile über {filename[:-3]} mit folgenden Information: \
    {text} , so dass ich es an einem Geburtstag vortragen kann",

    
    # Prompt 5: Goethe-style poem with mean-to-kind emotional arc
    f"Stell dir vor du bist Johann Wolfgang von Goethe und musst dein bestes Gedicht schreiben {filename[:-3]} mit folgenden Informationen: \
    {text}, am Anfang bitte mit bösen Satzen und nachher am Schluss herzlich",
    
    # Prompt 6: Goethe-style birthday poem
    f"Stell dir vor du bist Johann Wolfgang von Goethe und musst dein bestes Gedicht schreiben {filename[:-3]} mit folgenden Informationen: \
    {text}, , so dass er es an einem Geburtstag vortragen kann",
    
    # Prompt 7: Poem by fictional poet Sophie Meier
    f"Stell dir vor du bist diese Dichterin und musst dein bestes Gedicht über {filename[:-3]} schreiben\
    Name: Sophie Meier \ \
    Geburtsdatum: 3. November 1992 \
    Geburtsort: Wien, Österreich \
    Sophie Meier ist eine aufstrebende Dichterin aus Wien, deren Leidenschaft für Poesie sie seit ihrer Jugend begleitet. Nach einem Studium der Literaturwissenschaften an der Universität Wien widmete sie sich ganz ihrer eigenen poetischen Arbeit. Ihre Gedichte, die oft introspektiv und voller Empfindungen sind, wurden in verschiedenen Literaturzeitschriften und Online-Plattformen veröffentlicht. \
    Sophie strebt danach, mit ihren Gedichten nicht nur zum Nachdenken anzuregen, sondern auch zum Lachen zu bringen. Ihre Werke sind oft humorvoll und provokant, und sie scheut nicht davor zurück, gesellschaftliche Normen zu hinterfragen. Trotz ihres humorvollen Ansatzes gelingt es Sophie, ihren Gedichten eine tiefere Bedeutung zu verleihen, indem sie ihren Lesern subtile Botschaften und Lebensweisheiten vermittelt. \
    Sie glaubt an die transformative Kraft der Poesie und setzt ihre Worte ein, um Licht in die Dunkelheit zu bringen und Trost zu spenden. Sophie lebt und arbeitet weiterhin in Wien, wo sie sich von den Alltagsmomenten und der Welt um sie herum inspirieren lässt, um neue Gedichte zu schaffen, die ihre Leser zum Schmunzeln bringen und gleichzeitig zum Nachdenken anregen. \
    mit folgenden Informationen: {text}\
    "
]

# Generate poems
# For each of the 8 prompts, generate 8 variations (total: 64 poems)
for poem_num, prompt in enumerate(prompts):
    for rep in range(REPS_PER_PROMPT):
        # Call OpenAI API to generate poem
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ]
        )
        
        # Save generated poem to file
        savefile = open(f"generated_poems/prompt{poem_num}rep{rep}.txt", "w")
        savefile.write(response.choices[0].message.content)
        savefile.close()
        
        # Print progress with preview
        print(f"Version {rep} of poem {poem_num} generated. {response.choices[0].message.content[:100]}...{response.choices[0].message.content[-100:]}")
    
    print(f"Completed all {REPS_PER_PROMPT} variations for prompt {poem_num}")