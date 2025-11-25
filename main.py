# === main.py ===

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TELEGRAM_BOT_TOKEN
from modules import referrals, tasks, ads, withdraw, antifraud

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ref = None
    if len(message.text.split()) > 1:
        ref = message.text.split()[1]
        referrals.register_referral(message.from_user.id, ref)

    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("💰 ربح المال", callback_data="earn"),
        InlineKeyboardButton("📢 نشر إعلان", callback_data="create_ad"),
        InlineKeyboardButton("👥 الإحالة", callback_data="ref_system"),
        InlineKeyboardButton("💳 السحب", callback_data="withdraw")
    )

    await message.answer("مرحبًا بك في بوت الإعلان والربح 👋", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == "earn")
async def earn_menu(call):
    await call.message.edit_text("اختر مهمة للربح:", reply_markup=
        InlineKeyboardMarkup().add(
            InlineKeyboardButton("➕ انضم لقنوات", callback_data="task_join"),
            InlineKeyboardButton("▶ مشاهدة فيديو", callback_data="task_video")
        )
    )

@dp.callback_query_handler(lambda c: c.data == "create_ad")
async def ad_menu(call):
    await call.message.edit_text(
        "أرسل رابط قناتك/فيديوك + الميزانية.\nمثال:\nhttps://t.me/test 50",
    )

@dp.message_handler(lambda m: "https://" in m.text)
async def create_ad_handler(message):
    try:
        url, budget = message.text.split()
        ads.create_ad(message.from_user.id, url, float(budget))
        await message.answer("تم إنشاء الإعلان بنجاح ✨")
    except:
        await message.answer("صيغة خاطئة!")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
