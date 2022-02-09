from nextcord.ext import commands
import nextcord
import utilities
from typing import List

class ErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        error_value = f"Command invoke error: {type(error).__name__}"
        embed = nextcord.Embed(color=0xff0000)
        fields = [
            ("Error", error_value, False)
        ]
        utilities.add_fields(embed=embed, fields=fields)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))


