# selfbot.py
# WARNING: Selfbots violate Discord's Terms of Service. Use at your own risk.
import discord

client = discord.Client()
TOKEN = "MTEzMDU1Nzg4MTg2ODA9NTY2MA.GZdoaY.6_4HdjzbMO5Ubhc5jwmNLp7Za9gK4RwGoiZULw"
IMAGE_URL = "https://cdn.discordapp.com/attachments/1263780399352647754/1348117155597520947/images_1.jpg?ex=67ce4b70&is=67ccf9f0&hm=f24426b7a52ce39712bfcb7983d0af85f64cbf7740a747529d3261226e981bed&"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    # Send to all friends' DMs
    for friend in client.user.friends:
        await friend.send(file=discord.File(IMAGE_URL))
    
    # Send to all servers with @everyone
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send("@everyone", file=discord.File(IMAGE_URL))
                break
    
    print("Done sending")
    await client.close()

client.run(TOKEN)
