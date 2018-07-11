import time

responses = {
    'how is the weather today?': 'It\'s nice and sunny!',
    'do you have school on Monday?': 'No, I do not.',
    'default': 'Sorry I didn\'t get the question, could you rephrase?'
}


while True:
    utter = input()
    time.sleep(0.2)
    if utter == 'bye': break
    if utter in responses: print(responses[utter])
    else: print(responses['default'])

time.sleep(1)
print('Going to sleep...')
