import random

def phrase_generator():
    secret_message = {
        "Phrase": "It ain't over until the fat lady sings",
        "Person": "Software Engineer",
        "School": "NuCamp Bootcamp",
        "Famous People": "Albert Einstein",
        "Game Show": "The Price is Right",
        "Bible Verse": "The Lord is my shepard, I shall not want",
        "Phrase": "This is a test of the emergency broadcast system"
    }

    category = random.choice(list(secret_message.keys()))
    message = secret_message[category]
    message = message.upper()
    return(category, message)   