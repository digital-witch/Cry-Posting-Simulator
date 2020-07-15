import keyboard
import random

keys = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

def missedKey(key):
    keyboard.send('backspace')

def fatFinger(key):
    to_write = ''
    if key == 'p' or key == 'l' or key == 'm': 
        to_write = keys[keys.index(key)-1]
    elif key == 'q' or key == 'a' or key == 'z':
        to_write = keys[keys.index(key)+1]
    else:
        to_write = random.choice([keys[keys.index(key)-1],keys[keys.index(key)+1]])
    with_original = random.choices([0,1],[1,10])
    if not with_original:
        keyboard.send('backspace')
    if key.isupper():
        with_original = with_original.upper()
    keyboard.write(to_write)

def doubleKey(key):
    keyboard.write(key)

def randomSpace(key):
    keyboard.write(' ')

def keyEvent(event):
    key = event.name.lower()
    print('In key event:',key)
    outcome = random.choices(['0','1','2','3','4'],[80, 2, 15, 2, 1])
    outcome_map = {
    '0': None,
    '1': missedKey,
    '2': fatFinger,
    '3': doubleKey,
    '4': randomSpace
    }
    value = outcome_map.get(''.join(outcome))
    if value:
        value(key)

for key in keys:
    keyboard.on_press_key(key,keyEvent)