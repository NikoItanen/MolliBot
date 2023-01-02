def handleResponses(message) -> str:
    comingMessage = message.lower()

    if comingMessage == '!hellobot':
        return "Hello!"

