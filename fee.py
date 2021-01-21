import aiohttp
from typing import Tuple, Union

from telethon.errors import rpcerrorlist

from userbot import client
from userbot.utils.events import 

plugin_category = "misc"

@client.onMessage(
    command=("fees", plugin_category),
    outgoing=True, regex="fees$"
)
async def fees(event: NewMessage.Event) -> None:
    """
    Get btc fees.


    `{prefix}fees`
    """  
    fees = await _request('https://bitcoinfees.earn.com/api/v1/fees/list')
    if not fees:
        await event.answer("`Error on fetching fees.`")
        return

    _, json = fees
    try:
        await event.answer(file=json[0], reply_to=event.reply_to_msg_id)
        await event.delete()
    except rpcerrorlist.TimeoutError:
        await event.answer("`Event timed out!`")