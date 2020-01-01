import re
import os
import pre_built_messages.help_messages as hm

from discord.ext import commands
from dice_logic.dice_roller import roll
from dice_logic.command_map import dice_map


client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Bot initialised")


@client.event
async def on_message(message):
    if message.content.startswith("/r"):
        channel = message.channel
        reply = f"{message.author.mention}"
        for dice_roll in message.content.replace("/r", "").split("+"):
            try:
                times = int(re.findall(r'\d+', dice_roll)[0])
            except IndexError:
                times = 1

            die = re.sub(r"[0-9]", "", dice_roll).strip().lower()

            if die not in list(dice_map.keys()):
                reply += "\nMeow"
            else:
                for key, value in dice_map.items():
                    if key == die:
                        reply += f"\n`{value['dice name']}` = {roll(value['dice faces'], times)}"
                        break

        await channel.send(reply)

    elif message.content.startswith("/help"):
        channel = message.channel
        reply = f"{message.author.mention}\n"
        if "dice" in message.content or "symbols" in message.content:
            reply += hm.dice_help
        elif "roll" in message.content or "rolling" in message.content:
            reply += hm.rolling_help
        else:
            reply += f"{hm.rolling_help}\n\nResult symbols:\n{hm.dice_help}"

        await channel.send(reply)


client.run(os.getenv("edge_bot_token"))
