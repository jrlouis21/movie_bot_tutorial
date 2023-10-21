import discord
from discord.ext import commands

DISCORD_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.tree.command(name="marco", description="Marco Polo test command")
async def marco(ctx: discord.interactions.Interaction):
    await ctx.response.send_message("Polo!")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    await bot.tree.sync()
    print(f"Logged in as {bot.user} and synced commands")


bot.run(DISCORD_BOT_TOKEN)
