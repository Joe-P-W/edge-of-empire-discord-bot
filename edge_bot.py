import re
import os
import dice
import dice_sides as ds

from discord.ext import commands
from dice_roller import roll
from command_map import dice_map


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

            try:
                die = re.sub(r"[0-9]", "", dice_roll).strip().lower()
            except IndexError:
                die = "Meow"

            if die not in list(dice_map.keys()):
                reply += "\nMeow"
            else:
                for key, value in dice_map.items():
                    if key == die:
                        reply += f"\n`{value[1]}` = {roll(value[0], times)}"

        await channel.send(reply)

    elif message.content == "/help":
        channel = message.channel
        await channel.send(f"{message.author.mention}\n"
                           "To roll a die type /r followed any number of the following:\n"
                           "Boost Die = bd\n"
                           "Set Back Die = sbd\n"
                           "Difficulty Die = dd\n"
                           "Proficiency Die = pd\n"
                           "Challenge Die = cd\n"
                           "Force Die = fd\n\n"
                           "The results of the dice rolls are:\n"
                           f"Success = {ds.success}\n"
                           f"Fail = {ds.fail}\n"
                           f"Triumph = {ds.triumph}\n"
                           f"Advantage = {ds.advantage}\n"
                           f"Despair = {ds.despair}\n"
                           f"Threat = {ds.threat}\n"
                           f"Light = {ds.light}\n"
                           f"Dark = {ds.dark}\n"
                           f"Blank = {ds.blank}")




client.run(os.getenv("edge_bot_token"))
