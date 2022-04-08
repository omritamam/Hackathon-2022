from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from upload_file import full_upload

log = {}

course_button0 = InlineKeyboardButton(text="Infi 1", callback_data="Infi 1")
course_button1 = InlineKeyboardButton(text="Linear 1", callback_data="Linear 1")
course_button2 = InlineKeyboardButton(text="Discrete", callback_data="Discrete")
course_button3 = InlineKeyboardButton(text="Intro to CS", callback_data="Intro to CS")

course_button4 = InlineKeyboardButton(text="Infi 2", callback_data="Infi 2")
course_button5 = InlineKeyboardButton(text="Linear 2", callback_data="Linear 2")
course_button6 = InlineKeyboardButton(text="DAST", callback_data="DAST")
course_button7 = InlineKeyboardButton(text="C/C++", callback_data="C/C++")

year1 = InlineKeyboardButton(text="Year 1", callback_data="Year 1")
year2 = InlineKeyboardButton(text="Year 2", callback_data="Year 2")
year3 = InlineKeyboardButton(text="Year 3", callback_data="Year 3")

moedA = InlineKeyboardButton(text="Moed A", callback_data="Moed A")
moedB = InlineKeyboardButton(text="Moed B", callback_data="Moed B")

year_button17 = InlineKeyboardButton(text="2017", callback_data="2017")
year_button18 = InlineKeyboardButton(text="2018", callback_data="2018")
year_button19 = InlineKeyboardButton(text="2019", callback_data="2019")
year_button20 = InlineKeyboardButton(text="2020", callback_data="2020")
year_button21 = InlineKeyboardButton(text="2021", callback_data="2021")
year_button22 = InlineKeyboardButton(text="2022", callback_data="2022")


DATES = InlineKeyboardMarkup().add(year_button17, year_button18, year_button19,
                                   year_button20, year_button21, year_button22)
CS_YEAR1 = InlineKeyboardMarkup().add(course_button0, course_button1, course_button2, course_button3)
CS_YEAR2 = InlineKeyboardMarkup().add(course_button4, course_button5, course_button6, course_button7)
YEARS = InlineKeyboardMarkup().add(year1, year2, year3)
MOEDS = InlineKeyboardMarkup().add(moedA, moedB)


TOKEN = "5297251485:AAFTtEAqdiHSNf_G3l5iRo2v2vOK6XnG0pY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['txt', 'text'])
async def get_file_details(message):
    if str(message.text).isnumeric():
        log["course"] = message.text
        await message.reply("Which year???", reply_markup=DATES)
    else:
        log["comments"] = message.text
        await bot.send_message(
            text="Uploading.... Wait for Confirmation!",
            chat_id=message.chat.id)
        full_upload(log)
        await message.reply("Thank you!! 😁😁")


@dp.message_handler(content_types=['photo', 'video', 'audio', 'document'])
async def file_sent(message):
    await bot.send_message(text="Hey!\n Welcome to Up-Grade bot!🦾🦾\nNavigate to your course course name or type its "
                                "number 🚀🚀",
                           reply_markup=YEARS,
                           chat_id=message.chat.id)
    filename = "downloaded.pdf"
    log["path"] = filename

    with open(filename, 'wb') as f:
        x1 = await bot.get_file(file_id=message.document.file_id)
        y2 = await x1.download(f)


@dp.callback_query_handler(text=["Year 1", "Year 2", "Year 3"])
async def year_handler(call: types.CallbackQuery):
    if call.data == "Year 1":
        next_keyboard_map = CS_YEAR1
    elif call.data == "Year 2":
        next_keyboard_map = CS_YEAR2
    else:
        next_keyboard_map = CS_YEAR1
    await bot.send_message(text="Choose course name\n🇮🇱🇮🇱",
                           reply_markup=next_keyboard_map,
                           chat_id=call.message.chat.id)


@dp.callback_query_handler(text=["2017", "2018", "2019", "2020", "2021", "2022"])
async def date_handler(call: types.CallbackQuery):
    log["year"] = call.data
    await bot.send_message(chat_id=call.message.chat.id, text="🥁🥁🥁🥁🥁\nWhich Moed?\n🥁🥁🥁🥁🥁", reply_markup=MOEDS)


@dp.callback_query_handler(text=["Intro to CS", "Discrete", "Linear 1", "Infi 1",
                                 "DAST", "C/C++", "Linear 2", "Infi 2"])
async def year_handler(call: types.CallbackQuery):
    if call.data == "Intro to CS":
        log["course"] = '67101'
    elif call.data == "Discrete":
        log["course"] = '80181'
    elif call.data == "Linear 1":
        log["course"] = '80134'
    elif call.data == "Infi 1":
        log["course"] = '80133'
    else:
        log["course"] = '80133'
    await bot.send_message(chat_id=call.message.chat.id, text="Which year?\n📅📅", reply_markup=DATES)


@dp.callback_query_handler(text=["Moed A", "Moed B"])
async def moed_picker(call: types.CallbackQuery):
    log["moed"] = call.data
    await bot.send_message(call.message.chat.id, 'Enter notes if there are any 🧧✉️🖇️🗂️')


executor.start_polling(dp)
