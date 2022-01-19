"""
MIT License
Copyright (c) 2021 Nidusha Amarasinghe
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import telebot, requests, json
from telebot import types
from os import getenv

bot = telebot.TeleBot(getenv("BOT_TOKEN"))

# HPB API
response_API = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
data = json.loads(response_API.text)
local_new_cases     = str(data['data']['local_new_cases'])
update_date_time    = str(data['data']['update_date_time'])
local_new_cases     = str(data['data']['local_new_cases'])
local_active_cases  = str(data['data']['local_active_cases'])
local_total_cases   = str(data['data']['local_total_cases'])
local_deaths        = str(data['data']['local_deaths'])
local_recovered     = str(data['data']['local_recovered'])
local_total_number_of_individuals_in_hospitals = str(data['data']['local_total_number_of_individuals_in_hospitals'])
global_new_cases    = str(data['data']['global_new_cases'])
global_total_cases  = str(data['data']['global_total_cases'])
local_new_deaths    = str(data['data']['local_new_deaths'])
global_deaths       = str(data['data']['global_deaths'])
global_new_deaths   = str(data['data']['global_deaths'])
global_recovered    = str(data['data']['global_recovered'])

# /covid command menu
covidinfo = f"""
ශ්‍රී ලංකාවේ කොරෝනා තත්වය. 🇱🇰
🔄 {update_date_time} ට යාවත්කාලීන කරන ලදී.
• නව රෝගීන් ගණන 😷 - {local_new_cases}
• නව මරණ ගණන ⚰ - {local_new_deaths}
• තහවුරු කරන ලද මුළු රෝගීන් ගණන 🤒 - {local_total_cases}
• තවමත් ප්‍රතිකාර ලබන රෝගීන් ගණන 🤕 - {local_active_cases}
• මේ වන විට සුව වූ කොරෝන රෝගීන් ගණන 🙂 - {local_recovered}
• මුළු මරණ සංඛ්‍යාව ⚰ - {local_deaths}
Join @SlapTap
"""

# /gcovid command menu
gcovidinfo = f"""
සමස්ත ලෝකයේ කොරෝනා තත්වය. 🌎
🔄{update_date_time} ට යාවත්කාලීන කරන ලදී.
• නව රෝගීන් ගණන 😷 - {global_new_cases}
• නව මරණ ගණන ⚰ - {global_new_deaths}
• තහවුරු කරන ලද මුළු රෝගීන් ගණන 🤒 - {global_total_cases}
• මේ වන විට සුව වූ කොරෝන රෝගීන් ගණන 🙂 - {global_recovered}
• මුළු මරණ සංඛ්‍යාව ⚰ - {global_deaths}
Join @SlapTap
"""
# /help command menu
help = f"""
භාවිතා කළ හැකි විධාන 📌
 • /start - BOT start කිරීම සදහා.
 • /covid - ශ්‍රී ලංකාවේ නවතම කොරෝනා තොරතුරු සදහා.
 • /gcovid -සමස්ත ලෝකයේ නවතම කොරෝනා තොරතුරු සදහා.
 • /about - BOT ගැන දැන ගැනීම සදහා.
Inline mode 
 • Inline mode එකේ covid කියලා type කරන්න.
 Join @SlapTap
"""

# Markup
mark1 = telebot.types.InlineKeyboardMarkup()
mark1.add(telebot.types.InlineKeyboardButton(text='Updates', url='https://t.me/SlapTap'),
          telebot.types.InlineKeyboardButton(text='Support', url='https://t.me/SlapTaps')),
mark1.add(telebot.types.InlineKeyboardButton(text='Latest Details', callback_data=1)),
mark1.add(telebot.types.InlineKeyboardButton(text='Go Inline', switch_inline_query_current_chat="")),

mark2 = telebot.types.InlineKeyboardMarkup()
mark2.add(telebot.types.InlineKeyboardButton(text='Latest Details', callback_data=1),
          telebot.types.InlineKeyboardButton(text='Go Inline', switch_inline_query_current_chat=""))

# Commands
@bot.message_handler(commands=['start'])
def send_start(message):
   bot.send_message(message.chat.id, text="Hi, කොරෝනා පිළිබද තොරතුරු ලබා ගැනීම සදහා මාව භාවිතා කරන්න පුළුවන්. භාවිතා කරන ආකාරය දැන ගැනීමට /help භාවිතා කරන්න.",parse_mode='Markdown', reply_markup=mark1)

@bot.message_handler(commands=["covid"])
def send_covid(message):
    bot.send_message(message.chat.id, covidinfo)

@bot.message_handler(commands=["gcovid"])
def send_gcovid(message):
    bot.send_message(message.chat.id, gcovidinfo)

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, text=help, reply_markup=mark2) 

@bot.message_handler(commands=["about"])
def send_about(message):
    bot.send_message(message.chat.id, """
• මෙම BOT කොරෝනා තොරතුරු දැන ගැනීම සදහා Nidusha Amarasinghe විසින් සාදන ලද Bot කෙනෙකි.
• සියලු තොරතුරු [සෞඛ්‍ය ප්‍රවර්ධන කාර්‍යංශයෙන්](https://hpb.health.gov.lk) ලබා ගත් තොරතුරු ය.
                                      """, parse_mode='Markdown')

# Callback Data
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == '1':
        answer = covidinfo
    bot.send_message(call.message.chat.id, answer)           

# Inline Mode             
@bot.inline_handler(lambda query: query.query == 'covid')
def query_text(inline_query):
        in1 = types.InlineQueryResultArticle('1', "ශ්‍රී ලංකාවේ කොරෝනා තත්වය. 🇱🇰", types.InputTextMessageContent(covidinfo))
        in2 = types.InlineQueryResultArticle('2', "සමස්ත ලෝකයේ කොරෝනා තත්වය. 🌎", types.InputTextMessageContent(gcovidinfo))
        bot.answer_inline_query(inline_query.id, [in1, in2])
    
bot.polling()
