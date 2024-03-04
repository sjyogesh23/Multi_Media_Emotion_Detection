import re

def has_offensive_words(text):
    offensive_words = [
        'fuck',
        'fucker',
        'fucking',
        'holy shit',
        'nigga',
        'fck',
        'ass',
        'your mom ass',
        'nice ass',
        'nice boobs',
        'bastard',
    ]
    pattern = re.compile(r'\b(?:' + '|'.join(offensive_words) + r')\b', re.IGNORECASE)
    if pattern.search(text):
        return True
    else:
        return False

def has_threatening_words(text):
    threatening_words = [
        'gonna kill you',
        'knell down',
        'will punch you',
        'will punch your',
        'will kick you',
        'will kick your',
        'will kill you',
        'kill you',
        'kill your',
        'kill your family',
        'cut your throat',            
        'cut your own throat',
        'cut your body',
        'slice your body'
    ]
    pattern = re.compile(r'\b(?:' + '|'.join(threatening_words) + r')\b', re.IGNORECASE)
    if pattern.search(text):
        return True
    else:
        return False
