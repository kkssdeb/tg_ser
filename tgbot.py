import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By

bot = telebot.TeleBot('')
chromedriver = 'C:\Program Files (x86)\chromedrive\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=chromedriver, options=options)

browser.get('https://generator-matov.github.io')
# Поиск тегов по имени
login = browser.find_element(by=By.CLASS_NAME,value='generatebutton')
login.click()

cyka = browser.find_element(by=By.CLASS_NAME,value='mat').text
#cyka = cyka.get_text()

print(cyka)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() != '':
        login = browser.find_element(by=By.CLASS_NAME,value='generatebutton')
        login.click()
        cyka ='Не пиши мне, ' + browser.find_element(by=By.CLASS_NAME,value='mat').text
        bot.send_message(message.chat.id, cyka)

bot.polling()
