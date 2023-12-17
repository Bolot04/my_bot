from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_bottons


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo",
        reply_markup=await inline_bottons.start_questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="oh cool,Python Developer\n"
             "Backand or Frontend ?",
        reply_markup=await inline_bottons.backend_or_frontend_menu_keyboard()
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Dont lie to me \n"
             "Backand or Frontend ?",
        reply_markup=await inline_bottons.backend_or_frontend_menu_keyboard()
    )


async def backend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What Backend Programs do you like?",
        reply_markup=await inline_bottons.backend_programs_keyboard()
    )


async def c_plus2_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh you love such a complex program!!! \n"
             "Which company would you like to work for? ",
        reply_markup=await inline_bottons.future_job_in_company_keyboard()
    )


async def java_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="I also like this program even though it doesn’t exist ) \n"
             "Which company would you like to work for? ",
        reply_markup=await inline_bottons.future_job_in_company_keyboard()
    )


async def frontend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What Frontend Programs do you like?",
        reply_markup=await inline_bottons.frontend_programs_keyboard()
    )


async def javascript_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="I would also like to learn \n"
             "Which company would you like to work for? ",
        reply_markup=await inline_bottons.future_job_in_company_keyboard()
    )


async def html_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="I'm also interested in this style of programming \n"
             "Which company would you like to work for? ",
        reply_markup=await inline_bottons.future_job_in_company_keyboard()
    )


async def google_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Yes, you are a future genius!!!",
    )


async def tesla_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Working under Elon Musk is good) ",
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "mojo")
    dp.register_callback_query_handler(backend_call,
                                       lambda call: call.data == "backend")
    dp.register_callback_query_handler(c_plus2_call,
                                       lambda call: call.data == "c++")
    dp.register_callback_query_handler(java_call,
                                       lambda call: call.data == "java")
    dp.register_callback_query_handler(frontend_call,
                                       lambda call: call.data == "frontend")
    dp.register_callback_query_handler(javascript_call,
                                       lambda call: call.data == "script")
    dp.register_callback_query_handler(html_call,
                                       lambda call: call.data == "html")
    dp.register_callback_query_handler(google_call,
                                       lambda call: call.data == "google")
    dp.register_callback_query_handler(tesla_call,
                                       lambda call: call.data == "tesla")
