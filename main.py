# Telegram BOT
# Got API Key from BotFather message /newbot
import os

import telebot
from dotenv import load_dotenv
import requests
import json

load_dotenv(".env")
API_key = os.getenv("API_key")

bot = telebot.TeleBot(API_key)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
	bot.reply_to(message, "Hey, how are you doing?")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, "Buddy! let me know how can I help you!")

def weather_request(message):
    val = str(message.text)
    if val.startswith("weather") and len(val.split())>=2:
        print("in if block---")
        return True
    else:
        print("else portion --")
        return False

@bot.message_handler(func=weather_request)
def send_weather(message):
    val = str(message.text)
    city = val.replace("weather ", "")
    bot.send_message(message.chat.id, "Weather in "+city+" is: 40 degree")

bot.polling()
