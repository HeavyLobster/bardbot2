import configparser
import random

from discord.ext import commands
import discord

def _get_prefix(bot, message):
    prefixes = ["!"]

    return prefixes

class BardBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=_get_prefix)

        # Read configuration
        self.config = configparser.ConfigParser()
        self.config.read("bot.ini")
        
    def run(self):
        super().run(self.config["auth"]["discordkey"])

    async def on_member_join(self, member):
        # Get greeting channel from configs
        channel = member.guild.get_channel(
            int(self.config[str(member.guild.id)]["greetchannel"])
        )
        if random.randrange(6) != 0:
            await channel.send(
                f"Welcome, {member.mention}, to the "
                f"{member.guild.name}! "
                "Head to <#265551115901206528> to get Roles! "
                "<:bardlove:242942446072233984>"
            )
        else:
            await channel.send(
                f"Welcome {member.mention}!"
                "<:bardhi2:269858268048916480> Have some "
                "<:cacao:269857893086527488> and "
                "<:porosnax:278951733609234433> "
                "<:bardhug:269858053820645389> \nHead to "
                "<#265551115901206528> to get Roles! "
                "<:bardlove:242942446072233984>"
            )

        return

if __name__ == "__main__":
    bardBot = BardBot()
    bardBot.run()
