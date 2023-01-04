import random
import bot
import discord
import pytube

# handleResponses-method will handle every sent messages in server and process them.

def handleResponses(message):
    processMessage = message.lower()

    if processMessage == '/hellobot':
        return 'Hello!'

    if processMessage == '/roll':
        return str(random.randint(1,6))

    if processMessage[0:5] == '/play':
        return ('Now Playing: ' + (pytube.YouTube.title))

    if processMessage == '/botstop':
        try:
            exit()
        except Exception as e:
            print ("Program has been stopped by using command")