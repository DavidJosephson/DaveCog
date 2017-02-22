import discord
from cogs.utils.downloader import update
from discord.ext import commands

class Mycog:
    def __init__(self, bot):
        self.bot = bot
    @commands.command()

    async def autoupdate(self):
        await self.bot.update()

def setup(bot):
    bot.add_cog(Mycog(bot))
