import logging
from MusicKen.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicKen.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAFF-KFg-jaEvlhu_kNknYQjxsuyDvp--AACjAMAAtpWSVeocCICILIfRSAE")
    await message.reply_text(
        f"""๐๐ป Hallo, Nama saya [{PROJECT_NAME}](https://telegra.ph/file/ed136c19e7f6afddb4912.jpg)
Dikekolah oleh @{OWNER}
โโโโโโโโโโโโโโโโโโโโโ
โ๏ธ Saya memiliki banyak fitur untuk anda yang suka lagu
๐ Memutar lagu di group 
๐ Mendownload lagu
๐ Mencari link youtube
๐ Mencari lirik lagu
โโโโโโโโโโโโโโโโโโโโโ
โ๏ธ Klik tombol bantuan untuk informasi lebih lanjut
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก สแดษดแดแดแดษด", callback_data = f"help+1"),
                    InlineKeyboardButton(
                        "โ แดแดแดสแดสแดแดษด โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "๐ฎ ษขสแดแดแด", url=f"https://t.me/{SUPPORT_GROUP}"), 
                    InlineKeyboardButton(
                        "แดสแดษดษดแดส ๐ฃ", url=f"https://t.me/{UPDATES_CHANNEL}")],
                [
                    InlineKeyboardButton("๐ ๐ณ๐พ๐ฝ๐ฐ๐๐ธ ๐", url=f"boyfriendnice")
                ]        
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**๐ด {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฌ sแดแดแดแดสแด แดสแดแด", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'โฌ๏ธ Sebelummya', callback_data = "help+7"),
             InlineKeyboardButton(text = 'Selanjutnya โก๏ธ', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton(text = '๐ก สแดษดแดแดแดษด', callback_data = f"help+1"),
             InlineKeyboardButton(text = 'โ แดแดแดสแดสแดแดษด โ', url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '๐ ษขสแดแดแด', url=f"https://t.me/{SUPPORT_GROUP}"),
             InlineKeyboardButton(text = 'แดสแดษดษดแดส ๐ฎ', url=f"https://t.me/{UPDATES_CHANNEL}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'โฌ๏ธ sแดสแดสแดแดษดสแด', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'sแดสแดษดแดแดแดษดสแด โก๏ธ', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**๐โโ๏ธ  Halo yang disana! Saya dapat memutar musik di obrolan suara grup & saluran telegram.โโ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐๐ฒ๐ฐ๐๐ฐ ๐ฟ๐ด๐ฝ๐ถ๐ถ๐๐ฝ๐ฐ๐ฐ๐ฝ ๐ฑ๐พ๐๐", url = "https://t.me/BeKing_Bots/9")
                ]
            ]
        ),
    )

@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""โ Bot **berhasil dimulai ulang!**\n\nโข **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ GROUP", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "OWNER ๐ฉโ๐ป", url=f"https://t.me/{OWNER}"
                    )
                ]
            ]
        )
   )

