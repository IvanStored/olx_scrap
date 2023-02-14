import asyncio
import uuid

import aiohttp
from bs4 import BeautifulSoup


DOMAIN = "https://www.olx.ua"


PHONES_DATA = []
PAGES_COUNT = 2
PHONES_URL = (
    DOMAIN
    + "/d/uk/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/"
)
PARAMS = {"currency": "UAH", "search[order]": "created_at:desc"}


async def get_phone_data(session, page):

    if page > 1:
        PARAMS["page"] = page

    async with session.get(url=PHONES_URL, params=PARAMS) as response:

        response_text = await response.text()

        soup = BeautifulSoup(response_text, "html.parser")
        phones = soup.select(".css-1sw7q4x")

        for phone in phones[:-1]:
            phone_link = DOMAIN + phone.select_one("a")["href"]
            phone_name = phone.select_one("h6").text
            phone_price = phone.select_one("p[data-testid='ad-price']").text
            date = phone.select_one("p[data-testid='location-date']").text

            PHONES_DATA.append(
                {
                    "id": uuid.uuid4(),
                    "phone": phone_name,
                    "price": phone_price,
                    "date": date,
                    "link": phone_link,
                }
            )

        print(f"[INFO] Обработал страницу {page}")


async def gather_data():

    async with aiohttp.ClientSession(trust_env=True) as session:

        tasks = []

        for page in range(1, PAGES_COUNT + 1):
            task = asyncio.create_task(get_phone_data(session, page))
            tasks.append(task)

        await asyncio.gather(*tasks)


def scraping():
    global PHONES_DATA
    PHONES_DATA = []
    asyncio.run(gather_data())
    return PHONES_DATA
