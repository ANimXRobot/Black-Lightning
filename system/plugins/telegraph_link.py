# Copyright (C) 2021 KeinShin@Github.


from telegraph import Telegraph
from telegraph import upload_file
from system.decorators import zeda_cmd as zeda
from system import *
telegraph = Telegraph()

telegraph.create_account(short_name='TG_UB')


@zeda(["telegraph"])
async def tg(client, message):
    try:
     if not message.media:
         await message.edit_message_text("**Are you sure this is media?**")
     else:
     
         a=await app.download_media(message)


         a=upload_file("photo_2020-12-19_18-28-53.jpg")
 
         o = 'http://telegra.ph/{}'.format(a)
         await app.send_message(message.chat_id, f"__YOUR LINK SIR__\n\n{o}")
    except Exception as e:
        await app.send_message(message.chat_id,e)


COMMAND_HELP.update(
    {"telegram_link": f"{HNDLR}telegrah",
    "telegraph_link's help": f"Creates telegraph link for the given media can image or video"}
)