import discord
from discord.ext import commands

class Mycog:
    def __init__(self, bot):
        self.bot = bot
    @commands.command()

    async def autoupdate(self):
        self.update()

def setup(bot):
    bot.add_cog(Mycog(bot))
