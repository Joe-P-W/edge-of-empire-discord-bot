import re

import discord
import os
import dice
import random
import dice_sides as ds
from discord.ext import commands
from dice_roller import roll


client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Bot initialised")


@client.event
async def on_message(message):
    if message.content.startswith("/r"):
        channel = message.channel
        reply = f"{message.author.mention}"
        for dice_roll in message.content.split("+"):
            try:
                times = int(re.findall(r'\d+', dice_roll)[0])
            except IndexError:
                times = 1
            if "bd" in dice_roll or "boost die" in dice_roll:
                reply += f"\n`Boost Die` = {roll(dice.boost_die, times)}"
            elif "sbd" in dice_roll or "set back die" in dice_roll:
                reply += f"\n`Set Back Die` = {roll(dice.set_back_die, times)}"
            elif "ad" in dice_roll or "ability die" in dice_roll:
                reply += f"\n`Ability Die` = {roll(dice.ability_die, times)}"
            elif "dd" in dice_roll or "difficulty die" in dice_roll:
                reply += f"\n`Difficulty Die` = {roll(dice.difficulty_die, times)}"
            elif "pd" in dice_roll or "proficiency die" in dice_roll:
                reply += f"\n`Proficiency Die` = {roll(dice.proficiency_die, times)}"
            elif "cd" in dice_roll or "challenge die" in dice_roll:
                reply += f"\n`Challenge Die` = {roll(dice.challenge_die, times)}"
            elif "fd" in dice_roll or "force die" in dice_roll:
                reply += f"\n`Force Die` = {roll(dice.force_die, times)}"
            else:
                reply += "\nMeow"

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
