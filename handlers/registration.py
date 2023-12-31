import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from const import PROFILE_TEXT
from database.sql_commands import Database


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    gender = State()
    number = State()
    street = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    db = Database()
    tg_id = call.from_user.id
    if db.sql_registration_profile(tg_id):
        await bot.send_message(
            chat_id=tg_id,
            text='You are already registered'
        )
        return
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me you are Nickname, please!!!'
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Tell me about you are self, please!!!'
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old r u?\n'
             'Send me only numeric answer\n'
             'Example: 26, 89, 18\n'
             'Not good: Twenty, Seventeen'
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='I said send me only numeric answer\n'
                 'Re-Registration, ur state of registration is over!!!'
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur gender'
    )
    await RegistrationStates.next()


async def load_gender(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur number '
    )
    await RegistrationStates.next()


async def load_number(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur street'
    )
    await RegistrationStates.next()


async def load_street(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['street'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text=' Send me ur photo'
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(path.name)
    async with state.proxy() as data:
        try:
            db.sql_insert_profile(
                tg_id=message.from_user.id,
                nickname=data['nickname'],
                bio=data['biography'],
                age=data['age'],
                gender=data['gender'],
                number=data['number'],
                street=data['street'],
                photo=path.name
            )
        except sqlite3.IntegrityError:
            await message.reply(
                text="You have registered before"
            )
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['biography'],
                    age=data['age'],
                    gender=data['gender'],
                    number=data['number'],
                    street=data['street']
                ),
                parse_mode=types.ParseMode.MARKDOWN
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="You have registered successfully"
        )
        await state.finish()


def registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == 'registration'
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_number,
        state=RegistrationStates.number,
        content_types=['text']
    )
    dp.register_message_handler(
        load_street,
        state=RegistrationStates.street,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
