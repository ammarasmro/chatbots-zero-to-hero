import time

while True:
    utter = input()
    time.sleep(0.2)
    print('You just said: {}!'.format(utter))
    if utter == 'bye': break

time.sleep(1)
print('Going to sleep...')
