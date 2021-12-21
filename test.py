# testing bot
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(
    f'{bot.user} has connected to Discord!')

@bot.command(name="notify")
@commands.has_role('Staff')
async def notify(ctx, *members: discord.Member):
    channel = bot.get_channel(804507689664118834)
    await channel.send('Winners have been contacted!')
    for member in members:
        await member.send(':tada: Hello, congratulations on winning the giveaway! :tada: \nIn one message, please reply with: Your IGN, character, and set you would like. Prizes will be sent by ADM soon. Thank you! :gift_heart:')
        msg = await bot.wait_for('message', check=lambda message: message.author == member)
        await channel.send(f'{member}: {msg.content}')

bot.run(TOKEN)
