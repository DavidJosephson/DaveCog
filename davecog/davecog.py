import discord
from discord.ext import commands

class Mycog:
    def __init__(self, bot):
        self.bot = bot
    @commands.command()

    async def autoupdate(self, bot):
        bot.update()

def setup(bot):
    bot.add_cog(Mycog(bot))
