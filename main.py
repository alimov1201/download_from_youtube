from aiogram import Bot, Dispatcher, filters, F, types
from aiogram.types import FSInputFile
from pytubefix import YouTube
import asyncio
import ssl
import os
import subprocess


ssl._create_default_https_context = ssl._create_unverified_context

bot = Bot(token="7436714902:AAH4uua0RZrK1kAgk5OxBYsX_BZL3CDTmmc")
dp = Dispatcher(bot=bot)


@dp.message(filters.CommandStart())
async def start_bot(message: types.Message):
    await message.answer("Salom")

@dp.message()
async def download_bot(message: types.Message):
    try:
        yt = YouTube(message.text, use_oauth=True, allow_oauth_cache=True)
        video = yt.streams.get_by_itag(137)
        result = video.download(filename="video.mp4")
        audio = yt.streams.get_by_itag(140)
        result2 = audio.download(filename="audio.mp4")

        videomp4 = FSInputFile("output.mp4")
        subprocess.run(["ffmpeg", "-i", "video.mp4", "-i", "audio.mp4", "-c", "copy", "output.mp4"])
        await message.answer_video(video=videomp4)
        os.remove(result)
        os.remove(result2)
        print(yt.streams)
    except:
        await message.answer("videoni yuklab bo'lmadi")
        print(yt.streams)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
