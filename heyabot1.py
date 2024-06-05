#importing the class libraries to access discord and the operating system to generate someting.
import discord
import os
import random
from ec2_metadata import ec2_metadata

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

# Creating a new instance of the Discord bot
token = 'token'
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
intents.members = True  # Enable the members intent if needed
intents.presences = True  # Enable the presence intent if needed
client = discord.Bot(command_prefix="!", intents=intents)
# Event is triggered when the bot is ready and logged in
@client.event
async def on_ready():
    print(f"Logged in as a bot {client.user}")

# Event is triggered when a new message is sent in a channel
@client.event
async def on_message(message):
    # Get the username and channel name from the message
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    # Log the message details to the console
    print(f'Message {user_message} by {username} on {channel}')

    # Ignore messages sent by the bot itself to prevent loops
    if message.author == client.user:
        return

    # Checking if the message is in the 'random' channel
    if channel == "random":
        # Respond to greetings
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'What do you want!')
            return
        # Respond to farewells
        elif user_message.lower() == "bye":
            await message.channel.send(f"Don't leave me {username}")
        # Respond to a lovely comment
        elif user_message.lower() == "i love you":
            comment = [
                "Love does not exist. Stop being delulu!",
                "I love you too",
                "I am not a human-being perhaps consider getting a boyfriend."
            ]
            await message.channel.send(random.choice(comment))
        return
# Run the bot using the token
client.run(token)