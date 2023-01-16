import random
import bot
import discord
import pytube

# handleResponses-method will handle every sent messages in server and process them.

def handleResponses(message):
    processMessage = message.lower()

    if processMessage == '/hellobot':
        return 'Hello!'

    elif processMessage == '/roll':
        return str(random.randint(1,6))

    elif processMessage == '/play':
        return 'Moro'

    elif processMessage == '/disconnect' or '/pause':
        return 'Bot Disconnected'