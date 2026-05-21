import time

def slow_print(text, delay = 0.02):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)
    print()

def moreslow_print(text, delay = 0.1):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)
    print()
    
def veryslow_print(text, delay = 0.5):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)
    print()