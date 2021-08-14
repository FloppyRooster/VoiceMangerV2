from discord.ext import commands  # This is the part of discord.py that helps us build bots
from dotenv import load_dotenv
import os
import discord
import sys
from discord_slash import SlashCommand # Importing the newly installed library.

bot = commands.Bot(command_prefix="%", case_insnsitive = False)
slash = SlashCommand(bot, sync_commands=True)

bot.load_extension("cogs.voicechannels")
bot.load_extension("cogs.errors")

load_dotenv('voiceBotToken.env')

bot.run(os.getenv("TOKEN"))