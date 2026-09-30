import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

TOKEN = "8965155378:AAH8RCRT7rR2qVG__DFu51N7AxzrNHPCHJM"
URL_SAITA = "https://github.io"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔮 ОТКРЫТЬ HINATA SBORKS", 
                web_app=WebAppInfo(url=URL_SAITA)
            )
        ]
    ])
    
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Ты попал в приватный бот со сборками для **Black Russia**.\n"
        "Нажми на кнопку ниже, чтобы открыть наш крутой фиолетовый сайт и управлять своим профилем!",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.web_app_data)
async def web_app_data_handler(message: types.Message):
    mod_id = message.web_app_data.data
    
    if mod_id == "orange_fanta":
        await message.answer("📥 **Начинаю подготовку сборки ORANGE FANTA...**")
        await bot.send_chat_action(chat_id=message.chat.id, action="upload_document")
        
        try:
            ZIP_FILE_ID = "ЗАМЕНИ_ЭТОТ_ТЕКСТ_НА_FILE_ID_ИЗ_ТГ_БОТА" 
            await message.answer_document(
                document=ZIP_FILE_ID,
                caption="🚀 **Ваша сборка ORANGE FANTA успешно скачана!**\n\nРаспакуйте zip-архив и следуйте инструкции по установке в лаунчер Black Russia."
            )
        except Exception as e:
            await message.answer(
                "⚠️ Не удалось отправить zip-файл напрямую.\n"
                "Скачайте архив по резервной ссылке: https://yandex.ru\n\n"
                f"Error details: {str(e)}"
            )
    else:
        await message.answer("❌ Error: Not found.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
