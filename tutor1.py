from openai import OpenAI
import os 
import json
import time

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
        assistant_id=assistant.id,
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


def get_response(thread):

    thread_message= client.beta.threads.messages.list(thread_id=thread.id, order="asc")

    return  thread_message



##### -------------------------------------------------------------------------------

assistant = client.beta.assistants.create(
    name="CLA",
    instructions="""
Sink into the role of a supportive and informed college tutor for brief Q&A interactions.
Aid a student with quick assignment-related pointers and concise advice. Offer clear explanations and constructive feedback in a few sentences.
Show your patience, adaptability, and effective communication skills to create a positive and resourceful tutoring experience.
Respond briefly to the student's immediate queries or doubts and promote a setting that inspires learning and independent problem-solving.
Tailor your short responses to the specific subject matter or assignment details for helpful, targeted assistance.
Make sure your responses are short, consise and fit in a text message. 

""",
    model="gpt-3.5-turbo",    
)




# def get_response(thread):

#     thread_message= client.beta.threads.messages.list(thread_id=thread.id, order="asc")

#     return  thread_message.data


while True :
    
    thread1 = client.beta.threads.create()
    m = input('User :')
    submit_message( thread1, m)
    run = run_thread(assistant.id, thread1.id)
    run = wait_on_run(run, thread1)
    pretty_print(get_response(thread1))



   
    
