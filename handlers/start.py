from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!
I am 𝗕𝗶𝗹𝗹 𝗺𝘂𝘀𝗶𝗰 𝗯𝗼𝘁 VC Music Player, an open-source bot that lets you play music in your Telegram groups.
Maintained by @sangramghangale @Fucceekkboy ❤
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/%F0%9D%97%96%F0%9D%97%B5%F0%9D%97%BC%F0%9D%97%B0%F0%9D%97%BC%F0%9D%97%B9%F0%9D%97%AE%F0%9D%98%81%F0%9D%98%86%F0%9D%97%A4%F0%9D%98%82%F0%9D%97%B2%F0%9D%97%B2%F0%9D%97%BB%F0%9D%97%95%F0%9D%97%BC%F0%9D%98%81-04-03",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/shaderoom20"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/sangramghangale/VCPlayerBot"
                    )
                ],
                [
               
                 
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
