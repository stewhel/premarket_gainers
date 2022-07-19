import sys
sys.path.append('c:/users/steph/appdata/local/programs/python/python39/lib/site-packages')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from discord.ext import commands
import asyncio

sys.path.append('C:/Users/steph/anaconda3/pkgs/beautifulsoup4-4.9.3-pyhb0f4dca_0/site-packages')
from bs4 import BeautifulSoup

def scrape():

    url = 'https://www.investing.com/equities/pre-market'

    driver = webdriver.Chrome(executable_path = r'c:/users/steph/downloads/chromedriver_win32/chromedriver.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    rows = soup.findChildren('table')
    rows = rows[0]
    pre = rows.findChildren('tr')

    body = "Most Active Premarket Stocks: \n"

    for i in pre[1:11]:
        body += "\n"
        cells = i.findChildren('td')
        for cell in [cells[2], cells[5]]:
            value = str(cell.text)
            body += " " + value

    print(body)

    bot = commands.Bot(command_prefix='!')

    TOKEN = '{YOUR TOKEN HERE}'


    async def post():
        await bot.wait_until_ready()
        msg_sent = False

        if not msg_sent:
            channel = bot.get_channel('{YOUR CHANNEL HERE}')
            await channel.send(body)
            msg_sent = True
            sys.exit()

    bot.loop.create_task(post())
    bot.run(TOKEN)

scrape()
