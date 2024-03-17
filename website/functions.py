from bs4 import BeautifulSoup
import requests 
import os
import numpy as np
import pandas as pd
import openpyxl
import re
import functions

from openai import OpenAI
import os 
import json
import time


def prettyprint(input_string):
    output_string = ''.join([' ' + char if (char.isupper() or char in '$') and prev_char!= ' ' else char for prev_char, char in zip('_' + input_string, input_string)])
    output_string = output_string.lstrip()  # Remove leading space if any
    #print(output_string)
    return(output_string)



def Scrape(link):

    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text,'lxml')
    info = ""

    elements = soup.find_all('div', class_='text-left')
    L=[element for element in elements]
    L= L[1:]


    for element in L:
        element= element.text

        info = info + prettyprint(element)
        info = info + '\n'
        info = info + '---------------------- \n'

    return info



client = OpenAI(api_key="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")


##### -------------------------------------function-----------------------------------
def show_json(obj):
    parsed_json = json.loads(obj.model_dump_json())
    # Print the parsed JSON data
    print(json.dumps(parsed_json, indent=4))

def submit_message( thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    
def run_thread(assistant_id,thread_id ):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions= ' make sure to output everything in the message, I cant see the files you create ' 
    )

def wait_on_run(run, thread):
    while run.status in ['queued', 'in_progress', 'cancelling']:
        time.sleep(2)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
    return run

def pretty_print(messages):
    for m in messages:
        if m.role == 'assistant':
            rating = m.content[0].text.value
            #print(f" {m.content[0].text.value}")
            
            print(rating)
    return rating





def pretty_file(messages, index):
     with open(f'tex/{index}.tex', 'w', encoding="utf-8") as f:
        for m in messages:
            if m.role == 'assistant':
                for l in m.content[0].text.value :
                    f.write(f"{l}")
            
            
   


def get_response(thread):

    thread_message= client.beta.threads.messages.list(thread_id=thread.id, order="asc")

    return  thread_message


def extract_number(input_string):
    # Search for a continuous sequence of digits in the input string
    match = re.search(r'\d+', input_string)
    
    if match:
        extracted_number = int(match.group())  # Convert the extracted string to an integer
        return extracted_number
    else:
        return None 