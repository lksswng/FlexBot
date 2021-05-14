from discord.ext import commands
import discord
class CommandEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            print(guild)
            if guild.name == "Unbroken-Discord":
                break

        print(
            f'{self.bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')
        banned_users = await guild.bans()
        print(f"Banned users are: {banned_users}" )


def setup(bot):
    bot.add_cog(CommandEvents(bot))