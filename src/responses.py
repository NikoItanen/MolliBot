import random

def handleResponses(message) -> str:
    processMessage = message.lower()

    if processMessage == 'hellobot':
        return 'Hello!'

    if processMessage == 'roll':
        return str(random.randint(1,6))

    