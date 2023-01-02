import discord
import responses

async def sendMessage(message, userMessage, isPrivate):
    try:
        response = response.handleResposes(userMessage)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)


def runMolliBot():
    TOKEN = 'MTA1ODUxNzIyMTIyOTQ3Nzk0OA.GavomC.iJfcIxy0DFiNQGKrbCT90vpR8LN8keiIXESEGQ'
    client = discord.Client()

    @client.event
    async def onReady():
        print(client.user + " is no running!")


    client.run(TOKEN)