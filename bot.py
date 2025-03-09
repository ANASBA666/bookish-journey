import discord
from discord.ext import commands
import aiohttp
import asyncio

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = "MTEzMDU1Nzg4MTg2ODA5NTY2MA.GZdoaY.6_4HdjzbMO5Ubhc5jwmNLp7Za9gK4RwGoiZULw"
IMAGE_URL = "https://cdn.discordapp.com/attachments/1263780399352647754/1348117155597520947/images_1.jpg?ex=67ce4b70&is=67ccf9f0&hm=f24426b7a52ce39712bfcb7983d0af85f64cbf7740a747529d3261226e981bed&"

# Pre-fetch image
image_data = None

async def fetch_image():
    global image_data
    async with aiohttp.ClientSession() as session:
        async with session.get(IMAGE_URL) as resp:
            if resp.status == 200:
                image_data = await resp.read()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await fetch_image()

@bot.command()
async def sendimg(ctx):
    if not image_data:
        await ctx.send("Image not loaded yet!")  # Line 31: Properly closed string
        return

    file = discord.File(image_data, filename="image.jpg")
    
    # Server message
    if ctx.guild:
        permissions = ctx.channel.permissions_for(ctx.guild.me)
        if permissions.send_messages:
            content = "@everyone" if permissions.mention_everyone else None
            await ctx.channel.send(content=content, file=file)

    # Send to command user's DM
    await ctx.author.send(file=file)

bot.run(TOKEN)
