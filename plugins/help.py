from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Welcome to YT Downloader, I will help you to download any videos in every possible resolution. just send a **Youtobe Link** \n Report any bugs here : @Sadult "
    await message.reply_text(helptxt)
