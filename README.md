# PDF Converter Discord Bot in Python
 A discord bot that converts PDF files to PNG images made in Python
 For now, it's just a simple bot for a particular server.

 ## Attention!!!
 **This bot is limited by the RAM of the server it's hosted.**
 **And I didn't limit the RAM usage! So only use it on servers with people of trust to avoid someone sending a gigantic file to abuse the RAM of your server.**

 But just running the *PDF_Reader.py* with the Token and Channel ID configured correctly will make it work.

 So if you want to test it or use, you will have to [create a bot account](https://www.writebots.com/discord-bot-token/).
 And have some channel of your choice to set the bot to send the images there.

## How to configure?

If you did the other steps above now, it's easy.

* first, [turn on the developer mode on Discord](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/).
* Right-click the channel you want the bot to send the images and **copy the ID.**
* Access your bot account and copy it's token, you can find it in the: [Retrieve Your Token](https://www.writebots.com/discord-bot-token/) section.
* **Open the file** *PDF_Reader.py*, you can use an IDE (Easier) or just the Notepad if you want.
* Scroll down to the end of the file until you **find that part:**

~~~Python
#==========================================================
# Down here is the channel ID and the Bot Token to test it.
#V=========================VVV============================V

@client.event
async def on_ready():
    canalgeral = client.get_channel( YourId ) # <- Put the ID of a channel you want to receive the images here.

    myEmbed = discord.Embed(title='Hello! = D', description="My job is basically to convert your PDF files to PNG images and send one by one to easy the reading of it's content for the users.", color=0x8000ff)
    myEmbed.add_field(name='Command:', value='.up "Optional name in quotes" [Uploaded File]', inline=False)

    await canalgeral.send(embed=myEmbed)

# Run the client on the server
client.run('token here')# <- Put a Discord Bot Token here.
~~~

* Do as it says, change the **"YourId"** to the **ID of the channel you copied.**
* And change the **'token here'** to the **token of your bot.** *(Keep it inside the quotes)*.
* Bot configured!

## Running and using.
Now just **invite the bot to your server** (The [Bot account](https://www.writebots.com/discord-bot-token/) link also says how to do it in the "Inviting Your Bot" section).

In the permissions I put **all "Text Permissions"**, and for it to **"View Channels"** and **"Manage WebHooks" in "General Permissions"** just to make sure it will work.
 
**Run the *PDF_Reader.py* and make it come to life,** I would really suggest downloading an IDE to do it like [PyCharm](https://www.jetbrains.com/pt-br/pycharm/) and run the file from there by just right-clicking in the *PDF_Reader.py* and choosing the option to run it, but you can search other ways to run a .py file.