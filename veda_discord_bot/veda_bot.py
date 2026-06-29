# BOT requires the 'message_content' intent.
import os
import discord
from dotenv import load_dotenv
import random
import re
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


class BOT(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # ignore bot messages
        if message.author == self.user:
            return
        # make msg for convenience
        msg = message.content
        # ping
        if msg == "!ping":
            await message.channel.send("Pong!")
        # hello
        elif msg == "!hello":
            await message.channel.send(f"Hi {message.author.name}!")
        # say
        elif msg.startswith("!say "):
            await message.channel.send(msg[5:])
        # roll (random number selector)
        elif msg.startswith("!roll "):
            if re.match(r"^!roll \d+ \d+$", msg.strip()):
                lower_num, upper_num = msg[6:].strip().split()
                if lower_num > upper_num:
                    await message.channel.send(f"INVALID RANGE, {int(lower_num)} is greater than {int(upper_num)}")
                    return
                await message.channel.send(random.randint(int(lower_num), int(upper_num)))
            else:
                await message.channel.send(
                    "INVALID FORMAT!\nUse: *!roll `lowerNumber` `upperNumber`*\neg: !roll 1 10")
        # reminder
        elif msg.startswith("!rem "):
            if re.match(r"^!rem \d+[\s\S]*", msg.strip()):
                parts = msg[5:].strip().split(maxsplit=1)
                timer = parts[0]
                if len(parts) == 2:
                    rem_message = parts[1]
                else:
                    rem_message = "REMINDER!"
                await message.channel.send(
                    f"Timer set for `{rem_message}` after {int(timer)}secs")
                await asyncio.sleep(int(timer))
                await message.channel.send(
                    f"```{rem_message}```{message.author.mention}")
            else:
                await message.channel.send(
                    "INVALID FORMAT!\nUse: *!rem `time_in_seconds` `message(optional)`*\neg: *!rem 500 water break*")


intents = discord.Intents.default()
intents.message_content = True

client = BOT(intents=intents)
client.run(TOKEN)
