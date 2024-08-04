from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
Hallo saya bot antijomok yang akan menghapus konten nsfw.
"""

@Client.on_message(filters.command(["start","help","repo","source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="Source",url="https://github.com/commithobbies/Antijomok")
                ]
            ]
        )
    )
