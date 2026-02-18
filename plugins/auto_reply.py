import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_GRP

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

lock = asyncio.Lock()

@Client.on_message(filters.chat(FROM_GRP) & ~filters.bot)
async def auto_reply(bot, message):
    try:
        reply = await message.reply_text('''ʏօʊʀ ʍօʋɨɛ ɨռ ʍʏ քʀօʄɨʟɛ քʟɛǟֆɛ ƈɦɛƈӄ
''', reply_to_message_id=message.id)
        await asyncio.sleep(2)
        try:
            await asyncio.sleep(10)
            await reply.delete()
        except:
            pass
    except FloodWait as e:
        logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
        await asyncio.sleep(e.value + 10)
        logger.info("Floodwait ended")
