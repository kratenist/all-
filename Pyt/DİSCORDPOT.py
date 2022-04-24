import discord
from discord.ext import commands

intens = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!mm ", intent=intens)

@Bot.event
async def on_ready():
    print("Hazırım Kaptan!")


@Bot.event
async def on_member_join(member):
    print(f"{member} Aramıza Katıldı Hoşgeldi ! ")


@Bot.event
async def on_member_remove(member):
    print(f"{member} Aramızdan Ayrıldı BB ! ")


@Bot.command()
async def slm(msg):
    await msg.send("En iyi server")


Bot.run('OTYzMjA0MTE0MjQwNjM4OTk2.YlSrvA.vLgqUXiiFxJ96Zw1-PMwiYvYyuE')
