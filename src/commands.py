# handleResponses-method will handle every sent messages in server and process them.

def handleCommands(command) -> bool:
    processCommand = command.lower()

    if processCommand == '/connect':
        return True
