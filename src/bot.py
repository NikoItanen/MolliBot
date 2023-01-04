import discord
import responses
import commands
import pytube
import io
import asyncio



async def playTube(domain, userMessage, message, voiceChannel):
    try:
        print('Song started!')
        yt = pytube.YouTube(url= domain)
        stream = yt.streams.get_by_itag(251)
        stream.download(filename="play.webm", output_path="./src")
        if voiceChannel is not None:
            vc = await voiceChannel.connect()
            vc.play(discord.FFmpegPCMAudio('./src/play.webm'))
            while vc.is_playing():
                await asyncio.sleep(1)
            vc.disconnect()
    except Exception as e:
        print(e)

#Method makes bot to send messages in the server. isPrivate will define that will the message go for author by itself or channel where the command were sent.

async def sendMessage(message, userMessage, isPrivate):
    try:
        response = responses.handleResponses(userMessage)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
        print(f'Bot sent message: {response}')
    except Exception as e:
        print(e)


# Run-method below

def runMolliBot():
    TOKEN = 'MTA1ODUxNzIyMTIyOTQ3Nzk0OA.GavomC.iJfcIxy0DFiNQGKrbCT90vpR8LN8keiIXESEGQ'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    # Avoids the loop that could happen if message sent by bot is a command.

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)
        botUser = (client.user)




        print(f"{username} said:'{userMessage}' ({channel}) ")

        # If there is "!" at begin of the command, bot will send message straight to the command author.

        if userMessage[0:5] == '/play':
            domain = userMessage[7:]
            voiceChannel = message.author.voice.channel
            await playTube(domain, userMessage, message,voiceChannel)

        if userMessage == '/connect':
            await message.author.voice.channel.connect()

        

        if userMessage[0] == '!':
            userMessage = userMessage[1:]
            await sendMessage(message, userMessage, isPrivate=True)
        else: 
            await sendMessage(message, userMessage, isPrivate=False)


    client.run(TOKEN)