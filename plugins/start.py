from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Website", url="https://mercads.ir")],
        [InlineKeyboardButton(
            "Contact Developer", url="https://t.me/sadult")]
    ])
    welcomed = f"Hello Dear <b>{message.from_user.first_name}</b>\n >> Send a Youtube Link to download it."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
