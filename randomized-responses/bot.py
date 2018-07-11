import time
import random

responses = {
    'how is the weather today?': ['It\'s nice and sunny!', 'It\'s a really bad day', 'Try not to stay in the sun for too long'],
    'do you have school on Monday?': ['No, I do not.', 'Next Monday is a holiday'],
    'default': ['Sorry I didn\'t get the question, could you rephrase?', 'Sorry I got distracted, try again!']
}


while True:
    utter = input()
    time.sleep(0.2)
    if utter == 'bye': break
    if utter in responses: print(random.choice(responses[utter]))
    else: print(random.choice(responses['default']))

time.sleep(1)
print('Going to sleep...')
