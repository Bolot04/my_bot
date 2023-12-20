from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Start Registration 🔥",
        callback_data="registration "
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def start_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python 🐍",
        callback_data="python"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo 🔥",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def backend_or_frontend_menu_keyboard():
    markup = InlineKeyboardMarkup()
    backend_button = InlineKeyboardButton(
        "Backend",
        callback_data="backend"
    )
    frontend_button = InlineKeyboardButton(
        "Frontend",
        callback_data="frontend"
    )
    markup.add(frontend_button)
    markup.add(backend_button)
    return markup


async def backend_programs_keyboard():
    markup = InlineKeyboardMarkup()
    c_plus2_button = InlineKeyboardButton(
         "C++",
         callback_data="c++"
    )
    java_button = InlineKeyboardButton(
        "Java",
        callback_data="java"
    )
    markup.add(c_plus2_button)
    markup.add(java_button)
    return markup


async def frontend_programs_keyboard():
    markup = InlineKeyboardMarkup()
    javascript_button = InlineKeyboardButton(
        "JavaScript",
        callback_data="script"
    )
    ux_ui_button = InlineKeyboardButton(
        "HTML",
        callback_data="html"
    )
    markup.add(javascript_button)
    markup.add(ux_ui_button)
    return markup


async def future_job_in_company_keyboard():
    markup = InlineKeyboardMarkup()
    google_button = InlineKeyboardButton(
        "Google",
        callback_data="google"
    )
    tesla_button = InlineKeyboardButton(
        "Tesla",
        callback_data="tesla"
    )

    markup.add(google_button)
    markup.add(tesla_button)
    return markup
