from aiogram import Router, F
from aiogram.types import Message

from download import Download

router = Router()

router.message.filter(F.chat.type == 'private')


@router.message()
async def download_audio_handler(message: Message):
    urls = [
        message.text[entity.offset:entity.offset + entity.length]
        for entity in message.entities
        if entity.type == 'url'
    ]
    for url in urls:
        with Download(url) as dwnl:
            audio_id = dwnl.audio()
            await message.answer_audio(audio_id)
        await message.delete()
