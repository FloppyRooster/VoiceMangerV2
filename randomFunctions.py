from nextcord import activity
from nextcord.ext import commands
import sys
from nextcord.channel import VoiceChannel
import netcord
from netcord.ext.commands import check,Context, context

def bitrateIs8000(*bitrate):
    async def predicate(ctx:commands.context):
        return ctx.channel.bitrate == bitrate
    return check(predicate)

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
    elif guild.premium_subscription_count > 2:
        return 128000
    else: 
        return 96000

def readTemporaryChannels():
    with open("data/temporary_channels.csv","r") as f:
        temporary_channels = f.read().split(',')
    return list(filter(None, temporary_channels))

def removeFromFile(temporary_channels:list,channel_id: str):
    temporary_channels.remove(channel_id)

    #overwrite the file without the unwanted channel ID
    output = ""
    for j in temporary_channels:
        output += "," + j
    with open("data/temporary_channels.csv","w") as f:
        f.write(output)
