from discord.ext import commands
import discord
import random
import asyncio

class CommandEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_not_pinned(self, mess):
        return not mess.pinned

    @commands.command(name="delete", help="Deletes a certain amount of messages passed as argument after command, for example(+delete 15)")
    @commands.has_role('Ehre')
    async def delete(self, ctx, args):
        channel = ctx.message.channel
        print(channel)
        if args.isdigit():
            count = int(args) + 1
            deleted = await channel.purge(limit=count, check=self.is_not_pinned)

def setup(bot):
    bot.add_cog(CommandEvents(bot))