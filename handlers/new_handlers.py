from aiogram import types

from config import bot
from const import PARSER_TEXT
from scraper.scraper import NewsScraper
from scraper.parser import AnimeParser


async def scrape_news(call: types.CallbackQuery):
    global url
    scraper = NewsScraper()
    data = scraper.parse_data_anime()
    for url in data:
        await call.message.answer(
            f"{url}",
        )
    print(url)


async def parser_anime(call: types.CallbackQuery):
    parser = AnimeParser()
    data = parser.parse_data()
    for anime in data:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=anime['photo'],
            caption=PARSER_TEXT.format(
                title=anime['title'],
                link=anime['link']
            ),
            parse_mode=types.ParseMode.MARKDOWN,
        )


def register_news_handlers(dp):
    dp.register_callback_query_handler(scrape_news, lambda call: call.data == "anime_menu")
    dp.register_callback_query_handler(
        parser_anime, lambda call: call.data == "parsing_menu"
    )
