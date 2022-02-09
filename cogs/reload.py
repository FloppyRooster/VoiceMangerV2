#import utilities
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.core import has_permissions
from typing import List


class Debug(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx: commands.Context, extension: str):
        """Loads a module."""
        try:
            self.bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.message.add_reaction("\N{PISTOL}")
            await ctx.send(f"{type(e).__name__}: {e}")
        else:
            await ctx.message.add_reaction("\N{OK HAND SIGN}")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, extension: str):
        """Unloads a module."""
        try:
            self.bot.unload_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.message.add_reaction("\N{PISTOL}")
            await ctx.send(f"{type(e).__name__}: {e}")
        else:
            await ctx.message.add_reaction("😮")

    @commands.command(name="reload", hidden=True)
    @commands.is_owner()
    async def _reload(self, ctx: commands.Context, extension: str):
        """Reloads multiple modules."""
        try:
            self.bot.unload_extension(f"cogs.{extension}")
            self.bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.message.add_reaction("\N{PISTOL}")
            await ctx.send(f"{type(e).__name__}: {e}")
        else:
            await ctx.message.add_reaction("\N{OK HAND SIGN}")


def setup(bot: commands.Bot):
    bot.add_cog(Debug(bot=bot))
