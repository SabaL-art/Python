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
    def format_time(self, time):
        hr = time//3600
        time %= 3600
        min = time//60
        time %= 60
        sec = time
        return f"{hr}hr {min}min {sec}sec"

    async def send_giveaway_message(self, message, giveaway_message, timer):
        giveaway = await message.channel.send(f"`GIVEAWAY!`\n`{giveaway_message}`\n**Time:** `{self.format_time(timer)}`")
        await giveaway.add_reaction("🎉")
        while timer > 0:
            await giveaway.edit(content=f"`GIVEAWAY!`\n`{giveaway_message}`\n**Time:** `{self.format_time(timer)}`")
            await asyncio.sleep(1)
            timer -= 1
        giveaway = await giveaway.channel.fetch_message(giveaway.id)
        winner = await self.choose_winner(giveaway)
        if winner == None:
            await giveaway.edit(content=f"`GIVEAWAY ENDED!`\n **Prize:**`{giveaway_message}`\n **Winner:**`NO ONE`")
            await message.channel.send(f"Noone entered the giveaway for`{giveaway_message}`")
        else:
            await giveaway.edit(content=f"`GIVEAWAY ENDED!`\n **Prize:**`{giveaway_message}`\n **Winner:**{winner.mention}")
            await message.channel.send(
                f"**GIVEAWAY RESULTS:**\nWinner for `{giveaway_message}` is: {winner.mention}")

    async def choose_winner(self, giveaway):
        list_of_participants = []
        for react in giveaway.reactions:
            if str(react.emoji) == "🎉":
                async for users in react.users():
                    if users != self.user:
                        list_of_participants.append(users)
                if not list_of_participants:
                    return None
                return random.choice(list_of_participants)

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
                lower_num, upper_num = map(int, msg[6:].strip().split())
                if lower_num > upper_num:
                    await message.channel.send(f"INVALID RANGE, {lower_num} is greater than {upper_num}")
                    return
                await message.channel.send(random.randint(lower_num, upper_num))
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

        # giveaway
        elif msg.startswith("!giveaway "):
            pack = msg[10:].split()
            try:
                if len(pack) < 2:
                    raise ValueError
                timer = int(float(pack[0].strip())*60)
                giveaway_message = " ".join(pack[1:])
                asyncio.create_task(self.send_giveaway_message(
                    message, giveaway_message, timer))

            except ValueError:
                await message.channel.send("INVALID FORMAT!\nUse: *!giveaway `timer (in mins)` `giveaway message`*")
                return


intents = discord.Intents.default()
intents.message_content = True

client = BOT(intents=intents)
client.run(TOKEN)
