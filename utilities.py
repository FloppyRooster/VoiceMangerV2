from discord.ext import commands
import discord
from discord.ext.commands import context

def getChannelName(member: discord.member):
    if member.nick == None:
        return str(member)[:-5] + "'s Channel"
    else:
        return str(member.nick) + "'s Channel"

async def deleteChannel(old_channel):
    await discord.VoiceChannel.delete(old_channel, reason = "don't flood server with channels")

def getMaxBitRate(guild:discord.guild):
    if guild.premium_subscription_count >= 30:
        return 384000
    elif guild.premium_subscription_count < 30 and guild.premium_subscription_count > 15:
        return 256000
    elif guild.premium_subscription_count >= 2:
        return 128000
    else: 
        return 96000

def readTemporaryChannels():
    with open("data/temporary_channels.csv","r") as f:
        temporary_channels = f.read().split(',')
    return list(filter(None, temporary_channels))

def removeFromFile(data:list,file:str,item_to_remove: str):
    data.remove(item_to_remove)
    data = [string for string in data if string != ""]


    #overwrite the file without the unwanted channel ID
    output = ""
    for i in data:
        output += "," + i
    with open(file,"w") as f:
        f.write(output)

def saveChannelID(ctx: commands.Context,ID: int,channel_name:str):
    with open(r"data\active_channels.csv", "a") as f:
        f.write(","+str(ID))
    
def appendFile(file:str,new_element:str):
    with open(file, "a") as f:
        f.write(","+new_element)

def readFileToList(file:str):
    with open(file, "r") as f:
        return f.read().split(",")
