from discord.ext import commands
import discord
class CommandEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="connects Bot to your voice channel")
    @commands.has_role('Ehre')
    async def connect(self, ctx, *args):
        member = ctx.message.author
        print(member.voice.channel)
        channel = member.voice.channel
        print(channel.members)
        [print(x.name) for x in channel.members]
        for x in self.bot.voice_clients:
            if (x.guild == ctx.message.guild):
                return await ctx.send("test Der bot ist bereits in einem channel")
        await channel.connect()
        # member.voice.mute = True

    @commands.command(help="Removes Bot to your voice channel")
    @commands.has_role('Ehre')
    async def disconnect(self, ctx, *args):
        for x in self.bot.voice_clients:
            if (x.guild == ctx.message.guild):
                return await x.disconnect()
        await ctx.send("Der bot ist in keinem channel")

    @commands.command(help="Mutes user passed as Argument")
    @commands.has_role('Ehre')
    async def mute(self, ctx, member: discord.Member):
        await member.edit(mute=True)

    @commands.command(help="removes mute-status from the user passed as Argument")
    @commands.has_role('Ehre')
    async def entmute(self, ctx, member: discord.Member):
        await member.edit(mute=False)

def setup(bot):
    bot.add_cog(CommandEvents(bot))