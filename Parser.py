# https://web.telegram.org/a/#8180384450
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
command = """/help - список всіх команд бота
/hello - привітання,
/film - список найновіших фільмів"""
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}"
        await update.message.reply_text(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)


app = ApplicationBuilder().token("8180384450:AAF9TZI-QqCG_ElLbN2bBhz3wI5KvkiAqCM").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))

app.run_polling()



