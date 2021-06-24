import discord
from discord.ext import commands
import requests
import os
import fitz

client = commands.Bot(command_prefix='.')

@client.command(name='up')
async def up(ctx, name=''):

    await ctx.send('Converting...')

    try:
        attachment_url = ctx.message.attachments[0].url
        url = attachment_url
        r = requests.get(url, allow_redirects=True)
        open(f'{name}.pdf', 'wb').write(r.content)
    except:
        await ctx.send("I'm sorry... Something went wrong saving the PDF file. = (")
        return

    try:
        # Open a PDF file and generate an object
        images = fitz.open(f'{name}.pdf')
        for pg in range(images.pageCount):
            page = images[pg]
            rotate = int(0)
            # Each size has a scaling factor of 2, which will give us an image that is quadrupled in resolution.
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG(f'{name}{pg + 1}.png')
    except:
        await ctx.send("I'm sorry... Something went wrong trying to convert. = (")
        return

    for pg in range(images.pageCount):
        await ctx.send(f'{name} Page {pg+1}')
        await ctx.send(file=discord.File(f'{name}{pg+1}.png'))
        os.remove(f'{name}{pg+1}.png')


    images.close()
    os.remove(f'{name}.pdf')

#==========================================================
# Down here is the channel ID and the Bot Token to test it.
#V=========================VVV============================V

@client.event
async def on_ready():
    canalgeral = client.get_channel() # <- Put the ID of a channel you want to receive the images here.

    myEmbed = discord.Embed(title='Hello! = D', description="My job is basically to convert your PDF files to PNG images and send one by one to easy the reading of it's content for the users.", color=0x8000ff)
    myEmbed.add_field(name='Command:', value='.up "Optional name in quotes" [Uploaded File]', inline=False)

    await canalgeral.send(embed=myEmbed)

# Run the client on the server
client.run('token here')# <- Put a Discord Bot Token here.
