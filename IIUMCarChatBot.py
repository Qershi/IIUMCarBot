from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import numpy as np

daysInt = np.arange(1, 31)
array = np.arange(-1000, 1000)
days = [str(x) for x in array]
days = [s for s in days]
validDays = [str(x) for x in daysInt]

bot = Bot(token='5444736616:AAH31fMiL3fGkg8THvKp7t4dWXGfXY9Pujs')
dp = Dispatcher(bot)

# creating now time
now = datetime.now()
now_10 = now + timedelta(minutes=10)
current_time = now_10.strftime("%H:%M:%S")

salams = ["salam", "Assalamualikum", "hey", "hello", "hi", "yo", "i give you tahhiah"]
transport = ["transporter", "transport", "i want a transporter", "get a ride", "ride", "i want a ride",
             "give me a ride"]
rents = ['i want a car', 'rent', 'i need a car', 'car', 'car please', 'get a car']
pax_num = ["one", "two", "three", "four"]
mahallahs = ["faruq", "siddiq", "ali", "bilal", "uthman", "zubair", "salahuddin", "ruqayyah", "aminah"
    , "asiah", "asma", "hafsah ", "halimah", "maryam", "nusaibah", "safiyyah", "sumayyah", "fatimah", "ummu kalthum"]
time_now = ['now', 'curently', "now!", 'now please']
time_scheduled = ['time', 'scheduled time', 'scheduled']
cars = ["Bezza", "Axia", "Myvi", "Saga"]
time_rent= ["Now please", "Schedule please"]

button1_car = KeyboardButton("Bezza")
button2_car = KeyboardButton("Axia")
button3_car = KeyboardButton("Myvi")
button4_car = KeyboardButton("Saga")
keyboard_car = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1_car, button2_car).add(
    button3_car, button4_car)

button1_pax = KeyboardButton("One")
button2_pax = KeyboardButton("Two")
button3_pax = KeyboardButton("Three")
button4_pax = KeyboardButton("Four")
keyboard_pax = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1_pax, button2_pax,
                                                                                     button3_pax, button4_pax)

button1_tim = InlineKeyboardButton(text="Now", callback_data="tim1_id")
button2_tim = InlineKeyboardButton(text="Schedule time", callback_data="tim2_id")
keyboard_tim = InlineKeyboardMarkup().add(button1_tim, button2_tim)



button1_loc = KeyboardButton("Send my current location", request_location=True)
keyboard_loc = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1_loc)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello there, welcome to Car bot where you can either rent a car or get your ride.")


@dp.callback_query_handler(text=["tim1_id", "tim2_id"])
async def transportation(call: types.CallbackQuery):
    if call.data == "tim1_id":
        await call.message.answer("Alright, please come to mahallah Ali block c to pick up the car.")
        await call.message.answer("Thank you for using our service..")
    if call.data == "tim2_id":
        await call.message.answer("Alright, please state your time")
        await call.message.answer("The car will be available at the stated time")
        await call.message.answer("Thank you for using our service..")



@dp.message_handler()
async def main(message: types.Message):
    global sel
    if message.text.lower() in (salams):
        await message.answer("Hello there, welcome to Car bot where you can either rent a car or get your ride.")
    if message.text.lower() in (transport):
        await message.answer("How many pax!? \nChoose from 1 to 4", reply_markup=keyboard_pax)
    if message.text.lower() in (pax_num):
        await message.answer("Please type now or scheduled time to procced ")
    if message.text.lower() in (time_now):
        await message.answer("Alright, Transporter will come at " + current_time)
        await message.answer("Please type your pick up Mahallah")
        await message.answer(" Or you can send your location by clicking Send my current location",
                             reply_markup=keyboard_loc)
    if message.text.lower() in (time_scheduled):
        await message.answer("Alright, please state your time")
        await message.answer("Onc you send the time type confirm")
    if message.text.lower() in ('confirm'):
        await message.answer("Alright, Transporter will come at the stated time")
        await message.answer("Please type your pick up Mahallah")
        await message.answer("Or you can send your location by clicking Send my current location",
                             reply_markup=keyboard_loc)

    if message.text.lower() in (mahallahs):
        await message.answer("Well, Transporter will be at " + message.text.upper())
        await message.answer("Thank you for using our service..")

    if message.text.lower() in (rents):
        await message.answer_photo('https://ibb.co/7ymcWzQ', )
        await message.answer("Choose one", reply_markup=keyboard_car)
    if message.text in (cars):
        await message.answer("Alright, pleas determine for how many days, Choose from 1 to 30")
    if message.text in (days) :
        if message.text in (validDays):
            await message.answer("You have selected " + message.text + " Days")
            await message.answer("Please select now or scheduled time to proceed ", reply_markup=keyboard_tim)

        else:
            await message.answer("invalid number of days!! \nChoose from 1 to 30")



if __name__ == '__main__':
    executor.start_polling(dp)