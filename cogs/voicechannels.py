from discord import activity
from discord.ext import commands
import sys
from discord.channel import VoiceChannel
import discord
from discord.ext.commands import check,Context, context
import utilities

create_channel_aliases = ["Create","CreateJoinForVC","newChannel"]
class voicechannels(commands.Cog):

    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="create_channel", aliases = create_channel_aliases, description = "Create a channel which when connected to will automatically create a new temporary channel for you!")
    @commands.has_permissions(manage_channels=True)
    async def createChannel(self, ctx: commands.context,*,text = "Join for a new VC"):
        channel = await discord.Guild.create_voice_channel(ctx.channel.guild, name = text, overwrites=None, bitrate=8000,reason="Channel to create new.")
        utilities.appendFile(r"data\joinForChannels.csv",str(channel.id))
        await ctx.send(f'"{text}" successfully set as active channel')



    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member,before,after):
        joinForChannels = utilities.readFileToList(r"data\joinForChannels.csv")

        if after.channel and after.channel.bitrate == 8000 and str(after.channel.id) in joinForChannels: #These ensure its the correct channel
            channel_name = utilities.getChannelName(member)
            duplicate_detector = discord.utils.get(after.channel.guild.voice_channels, name=channel_name)
            if duplicate_detector:
                await member.move_to(duplicate_detector)
            else:                            
                channel = await discord.Guild.create_voice_channel(after.channel.guild, name = channel_name, overwrites=None, category=after.channel.category, reason="Channel For Vibes",bitrate = utilities.getMaxBitRate(after.channel.guild))
                utilities.appendFile("data/temporary_channels.csv",str(channel.id))
                await member.move_to(channel)

                    
    
        if before.channel != None and len(before.channel.members) == 0:            
            temporary_channels = utilities.readFileToList("data/temporary_channels.csv")
            if str(before.channel.id) in temporary_channels:
                await utilities.deleteChannel(before.channel)
                utilities.removeFromFile(temporary_channels,r"data\temporary_channels.csv",str(before.channel.id))


    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        temporary_channels = utilities.readFileToList(r"data\temporary_channels.csv")
        if str(channel.id) in temporary_channels:
            utilities.removeFromFile(temporary_channels,r"data\temporary_channels.csv",str(channel.id))
        
        join_for_channels = utilities.readFileToList(r"data\joinForChannels.csv")
        if str(channel.id) in join_for_channels:
            utilities.removeFromFile(join_for_channels,r"data\joinForChannels.csv",str(channel.id))
    
            

def setup(bot: commands.Bot):
    bot.add_cog(voicechannels(bot))