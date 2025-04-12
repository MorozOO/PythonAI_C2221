# https://web.telegram.org/a/#8180384450
import random

from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
for href in soup_list_href:
    # print(href['href'])
    f.write(f"{href['href']}\n")

f.close()
links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

# print(links_list)
f = open('info.txt', 'w', encoding='utf-8')
list_name = []
list_desc = []
for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text,features="html.parser" )
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    if len(soup_list_name_film)> 0:
        f.write(f'{soup_list_name_film[0].text}\n')
        list_name.append(soup_list_name_film[0].text)
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    for item in soup_list_ul:
        f.write(f"{item.text}\n")
        list_desc.append(item.text)

f.close()
exchange_rate_list = []
def exchange_rate():
    url = "https://bank.gov.ua/ua/markets/exchangerates"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    soup_list_liter = soup.find_all('td', {'data-label': "Код літерний"})
    soup_list_count = soup.find_all('td', {'data-label': "Кількість одиниць валюти"})
    soup_list_course = soup.find_all('td', {'data-label': "Офіційний курс"})


    for line in range(len(soup_list_liter)):
        s = f"{soup_list_liter[line].text}\t {soup_list_count[line].text} : {soup_list_course[line].text} \n"
        exchange_rate_list.append(s)


command = """/help - список всіх команд бота
/hello - привітання,
/film - список найновіших фільмів
/rand - випадковий фільм
/rate - курс валют
"""
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}"
        await update.message.reply_text(text)

async def filmrandom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    num = random.randint(0,18)
    text = f"{list_name[num]}\n{list_desc[num]}\n{links_list[num]}"
    await update.message.reply_text(text)
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)

async def rate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    exchange_rate()
    for i in range(len(exchange_rate_list)):
        text = f"{exchange_rate_list[i]}"

        await update.message.reply_text(text)
    print(exchange_rate_list)

app = ApplicationBuilder().token("8180384450:AAF9TZI-QqCG_ElLbN2bBhz3wI5KvkiAqCM").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("rand", filmrandom))
app.add_handler(CommandHandler("rate", rate))

app.run_polling()



