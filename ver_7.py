import urllib.request
import re
import telebot
from telebot import apihelper
import random
import MySQLdb
import time
from collections import Counter
from functools import reduce
import traceback

bot = telebot.TeleBot('5369965560:AAHgQUIDbsbQN5USy9qd8_DMPh5kv5jDmjA')

bac = 'Назад'
global user
global timer
uchenik1 = ['belgorod1','96805379']
uchenik2 = ['belgorod2','76922711']
uchenik3 = ['belgorod3','19429298']
uchenik4 = ['belgorod4','69609823']
uchenik5 = ['belgorod5','28505726']
uchenik6 = ['belgorod6','38620750']
uchenik7 = ['belgorod7','29339699']
uchenik8 = ['belgorod8','46485296']
uchenik9 = ['belgorod9','79390531']
uchenik10 = ['belgorod10','10129189']
uchenik11 = ['belgorod11','58831748']

user = {
    #Ракитин Роман
    "389412849" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': '*Ребенок 7 класс:* \n логин: ' + uchenik7[0] + ' пароль: ' + uchenik7[1] + 
              ' \n *Ребенок 8 класс:* \n логин: ' + uchenik8[0] + ' пароль: ' + uchenik8[1] + 
              ' \n *Ребенок 9 класс:* \n логин: ' + uchenik9[0] + ' пароль: ' + uchenik9[1] + 
              ' \n *Ребенок 10 класс:* \n логин: ' + uchenik10[0] + ' пароль: ' + uchenik10[1] + 
              ' \n *Ребенок 11 класс:* \n логин: ' + uchenik11[0] + ' пароль: ' + uchenik11[1],
        'login': 'rakitin.re',
        'pasword': '85417961',
    },
    #Вигантс Яна
    "2096176956" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': '*Ребенок 7 класс:* \n логин: ' + uchenik7[0] + ' пароль: ' + uchenik7[1] + 
              ' \n *Ребенок 8 класс:* \n логин: ' + uchenik8[0] + ' пароль: ' + uchenik8[1] + 
              ' \n *Ребенок 9 класс:* \n логин: ' + uchenik9[0] + ' пароль: ' + uchenik9[1] + 
              ' \n *Ребенок 10 класс:* \n логин: ' + uchenik10[0] + ' пароль: ' + uchenik10[1] + 
              ' \n *Ребенок 11 класс:* \n логин: ' + uchenik11[0] + ' пароль: ' + uchenik11[1],
        'login': 'vigants.iav',
        'pasword': '84430280',
    },
    #Акинина Анастасия
    "353987182" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik':
              ' \n *Ребенок 1 класс:* \n логин: ' + uchenik1[0] + ' пароль: ' + uchenik1[1] +
              ' \n *Ребенок 2 класс:* \n логин: ' + uchenik2[0] + ' пароль: ' + uchenik2[1] + 
              ' \n *Ребенок 3 класс:* \n логин: ' + uchenik3[0] + ' пароль: ' + uchenik3[1] +
              ' \n *Ребенок 4 класс:* \n логин: ' + uchenik4[0] + ' пароль: ' + uchenik4[1] +
              ' \n *Ребенок 5 класс:* \n логин: ' + uchenik5[0] + ' пароль: ' + uchenik5[1] + 
              ' \n *Ребенок 6 класс:* \n логин: ' + uchenik6[0] + ' пароль: ' + uchenik6[1] +           
              ' \n *Ребенок 7 класс:* \n логин: ' + uchenik7[0] + ' пароль: ' + uchenik7[1] + 
              ' \n *Ребенок 8 класс:* \n логин: ' + uchenik8[0] + ' пароль: ' + uchenik8[1] + 
              ' \n *Ребенок 9 класс:* \n логин: ' + uchenik9[0] + ' пароль: ' + uchenik9[1] + 
              ' \n *Ребенок 10 класс:* \n логин: ' + uchenik10[0] + ' пароль: ' + uchenik10[1] + 
              ' \n *Ребенок 11 класс:* \n логин: ' + uchenik11[0] + ' пароль: ' + uchenik11[1],
        'login': 'akinina.aa',
        'pasword': '22607702',
    },
    #Подлесная Анастасия
    "928321431" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': 
              ' *Ребенок 5 класс:* \n логин: ' + uchenik5[0] + ' пароль: ' + uchenik5[1] + 
              ' \n *Ребенок 6 класс:* \n логин: ' + uchenik6[0] + ' пароль: ' + uchenik6[1] +           
              ' \n *Ребенок 7 класс:* \n логин: ' + uchenik7[0] + ' пароль: ' + uchenik7[1] + 
              ' \n *Ребенок 8 класс:* \n логин: ' + uchenik8[0] + ' пароль: ' + uchenik8[1] + 
              ' \n *Ребенок 9 класс:* \n логин: ' + uchenik9[0] + ' пароль: ' + uchenik9[1] + 
              ' \n *Ребенок 10 класс:* \n логин: ' + uchenik10[0] + ' пароль: ' + uchenik10[1] + 
              ' \n *Ребенок 11 класс:* \n логин: ' + uchenik11[0] + ' пароль: ' + uchenik11[1],
        'login': 'podlesnaia.ab',
        'pasword': '28940283',
    },
    #Колесова ольга
    "382126831" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik':
              ' *Ребенок 1 класс:* \n логин: ' + uchenik1[0] + ' пароль: ' + uchenik1[1] +
              ' \n *Ребенок 2 класс:* \n логин: ' + uchenik2[0] + ' пароль: ' + uchenik2[1] + 
              ' \n *Ребенок 3 класс:* \n логин: ' + uchenik3[0] + ' пароль: ' + uchenik3[1] +
              ' \n *Ребенок 4 класс:* \n логин: ' + uchenik4[0] + ' пароль: ' + uchenik4[1],
        'login': 'kolesova.om',
        'pasword': '13238637',
    },
    #Махортова Татьяна
    "5264617139" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik':
              ' *Ребенок 1 класс:* \n логин: ' + uchenik1[0] + ' пароль: ' + uchenik1[1] +
              ' \n *Ребенок 2 класс:* \n логин: ' + uchenik2[0] + ' пароль: ' + uchenik2[1] + 
              ' \n *Ребенок 3 класс:* \n логин: ' + uchenik3[0] + ' пароль: ' + uchenik3[1] +
              ' \n *Ребенок 4 класс:* \n логин: ' + uchenik4[0] + ' пароль: ' + uchenik4[1],
        'login': 'makhortova.tn',
        'pasword': '96874521',
    },
    #Меркулова Елена
    "995091538" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': 
              ' *Ребенок 5 класс:* \n логин: ' + uchenik5[0] + ' пароль: ' + uchenik5[1] + 
              ' \n *Ребенок 6 класс:* \n логин: ' + uchenik6[0] + ' пароль: ' + uchenik6[1] +           
              ' \n *Ребенок 7 класс:* \n логин: ' + uchenik7[0] + ' пароль: ' + uchenik7[1] + 
              ' \n *Ребенок 8 класс:* \n логин: ' + uchenik8[0] + ' пароль: ' + uchenik8[1] + 
              ' \n *Ребенок 9 класс:* \n логин: ' + uchenik9[0] + ' пароль: ' + uchenik9[1] + 
              ' \n *Ребенок 10 класс:* \n логин: ' + uchenik10[0] + ' пароль: ' + uchenik10[1] + 
              ' \n *Ребенок 11 класс:* \n логин: ' + uchenik11[0] + ' пароль: ' + uchenik11[1],
        'login': 'merkulova.ea',
        'pasword': '45125606',
    },
    #Берестовая Ира
    "1807607141" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Доношенко Ольга
    "1773357563" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Кукин Руслан
    "1800178468" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Липунова Ксения
    "5269785760" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Саганова Маргарита
    "5101188245" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Шеин Генадий
    "5255426756" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik':
              ' \n *Ребенок 1 класс:* \n логин: ' + uchenik1[0] + ' пароль: ' + uchenik1[1] +
              ' \n *Ребенок 2 класс:* \n логин: ' + uchenik2[0] + ' пароль: ' + uchenik2[1] + 
              ' \n *Ребенок 3 класс:* \n логин: ' + uchenik3[0] + ' пароль: ' + uchenik3[1] +
              ' \n *Ребенок 4 класс:* \n логин: ' + uchenik4[0] + ' пароль: ' + uchenik4[1] +
              ' \n *Ребенок 5 класс:* \n логин: ' + uchenik5[0] + ' пароль: ' + uchenik5[1] + 
              ' \n *Ребенок 6 класс:* \n логин: ' + uchenik6[0] + ' пароль: ' + uchenik6[1] +           
              ' \n *Ребенок 7 класс:* \n логин: ' + uchenik7[0] + ' пароль: ' + uchenik7[1] + 
              ' \n *Ребенок 8 класс:* \n логин: ' + uchenik8[0] + ' пароль: ' + uchenik8[1] + 
              ' \n *Ребенок 9 класс:* \n логин: ' + uchenik9[0] + ' пароль: ' + uchenik9[1] + 
              ' \n *Ребенок 10 класс:* \n логин: ' + uchenik10[0] + ' пароль: ' + uchenik10[1] + 
              ' \n *Ребенок 11 класс:* \n логин: ' + uchenik11[0] + ' пароль: ' + uchenik11[1],        
        'login': 'shein.ga',
        'pasword': '66425119',
    },
    #Юрченко Алина
    "883028491" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Солдатова Виктория
    "1346924988" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': 
              ' *Ребенок 5 класс:* \n логин: ' + uchenik5[0] + ' пароль: ' + uchenik5[1] + 
              ' \n *Ребенок 6 класс:* \n логин: ' + uchenik6[0] + ' пароль: ' + uchenik6[1] +           
              ' \n *Ребенок 7 класс:* \n логин: ' + uchenik7[0] + ' пароль: ' + uchenik7[1] + 
              ' \n *Ребенок 8 класс:* \n логин: ' + uchenik8[0] + ' пароль: ' + uchenik8[1] + 
              ' \n *Ребенок 9 класс:* \n логин: ' + uchenik9[0] + ' пароль: ' + uchenik9[1] + 
              ' \n *Ребенок 10 класс:* \n логин: ' + uchenik10[0] + ' пароль: ' + uchenik10[1] + 
              ' \n *Ребенок 11 класс:* \n логин: ' + uchenik11[0] + ' пароль: ' + uchenik11[1], 
        'login': 'soldatova.vi',
        'pasword': '21135426',
    },
    #Тяпугина Ирина
    "867692282" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Скоренок Татьяна
    "1593362801" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
    #Капрелова Анастасия
    "5156347056" : {
        'mes': None,
        'children': None,
        'pr': None,
        'otdel': None,
        'maks': None,
        'chil': None,
        'sub': None,
        'uchenik': None,
        'login': None,
        'pasword': None,
    },
}

def dannie(message):
    try:
        global chil
        global sub
        global ip
        user[str(message.chat.id)]['chil'] = child(klass(message.chat.id))
        user[str(message.chat.id)]['sub']= predmet(message.chat.id)
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        bot.send_message(message.chat.id, text="Данные загружены")
        back(message)
    except:
        return  (bot.send_message(message.chat.id, text="Данных нет!"),print(message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.from_user.id))
            
    #--------------------------------------------------------------
def uroki(message):
    try:
        global chil
        global sub
        global ip

        ot = ['Онкогематология','Гнойная Хирургия','Хирургия','Реабилитация','Педиатрия','Травматология']
        mak = ['2','3','4','5','Н','+']
        named_tuple = time.localtime()
        time_string = time.strftime("Дата: %d.%m.%Y", named_tuple)
       
        if user[str(message.chat.id)]['mes'] == 'Ведомость':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in range(len(user[str(message.chat.id)]['chil'])):
                numbers = {"p{}".format(i):user[str(message.chat.id)]['chil'][i] for i in range(len(user[str(message.chat.id)]['chil']))}
                markup.add(numbers["p"+ str(i)])
            markup.add(bac)
            bot.send_message(message.chat.id, text="Выберите ученика или добавте нового" +"\n" + "Для добавления нового ученика/ов используйте" + "\n" + "Добавить ФИО"+ "\n" + "Пример: Добавить Иванов Иван"+ "\n" + "Пример: Добавить Иванов Иван, Василий Васильевич", reply_markup=markup)
        
        elif user[str(message.chat.id)]['mes'] == 'МЭО':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text="Для работы с МЭО:" +"\n" + "Перейти на сайт:" + "\n" + "https://mob.uchimznaem.ru/"+ "\n" + "логин: " + str(user[str(message.chat.id)]['login'])+ "\n" + "пароль: " + str(user[str(message.chat.id)]['pasword']), reply_markup=markup)
            bot.send_message(message.chat.id, text="Для доступа ребенка к МЭО:" +"\n" + str(user[str(message.chat.id)]['uchenik']))
            back(message)

        elif (message.text in user[str(message.chat.id)]['chil']) or (str(message.text.split(' ', 1)[0]) == 'Добавить') or (str(message.text.split(' ', 1)[0]) == 'добавить'):
            if str(message.text.split(' ', 1)[0]) == 'Добавить' or str(message.text.split(' ', 1)[0]) == 'добавить':
                user[str(message.chat.id)]['children'] = user[str(message.chat.id)]['mes'].split(' ', 1)[1]
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                for i in range(len(user[str(message.chat.id)]['sub'])):
                    numbers = {"p{}".format(i):user[str(message.chat.id)]['sub'][i] for i in range(len(user[str(message.chat.id)]['sub']))}
                    markup.add(numbers["p"+ str(i)])
                markup.add(bac)
                bot.send_message(message.chat.id, text="Выбери нужный предмет", reply_markup=markup)
            else:
                user[str(message.chat.id)]['children'] = user[str(message.chat.id)]['mes']
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                for i in range(len(user[str(message.chat.id)]['sub'])):
                    numbers = {"p{}".format(i):user[str(message.chat.id)]['sub'][i] for i in range(len(user[str(message.chat.id)]['sub']))}
                    markup.add(numbers["p"+ str(i)])
                markup.add(bac)
                bot.send_message(message.chat.id, text="Выбери нужный предмет", reply_markup=markup)
                    
        elif user[str(message.chat.id)]['mes'] in user[str(message.chat.id)]['sub'] :
            user[str(message.chat.id)]['pr'] = user[str(message.chat.id)]['mes']
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton('2')
            btn2 = telebot.types.KeyboardButton('3')
            btn3 = telebot.types.KeyboardButton('4')
            btn4 = telebot.types.KeyboardButton('5')
            btn5 = telebot.types.KeyboardButton('Н')
            btn6 = telebot.types.KeyboardButton('+')
            btn7 = telebot.types.KeyboardButton('Назад')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            bot.send_message(message.chat.id, text="Выбери нужную оценку", reply_markup=markup)  
        
        elif user[str(message.chat.id)]['mes'] in mak:
            user[str(message.chat.id)]['maks'] = user[str(message.chat.id)]['mes']
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in range(len(ot)):
                numbers = {"p{}".format(i):ot[i] for i in range(len(ot))}
                markup.add(numbers["p"+ str(i)])
            markup.add(bac)
            bot.send_message(message.chat.id, text="Выбери отделение", reply_markup=markup)


        elif user[str(message.chat.id)]['mes'] in ot:
            user[str(message.chat.id)]['otdel'] = user[str(message.chat.id)]['mes']
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = telebot.types.KeyboardButton("Сохранить")
            btn2 = telebot.types.KeyboardButton("Назад")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,"{}, Сохранить?"
                .format(message.from_user.first_name,
                        message.from_user.id), disable_web_page_preview=True, parse_mode="Markdown",reply_markup=markup)
        
        elif user[str(message.chat.id)][str('mes')] == 'Сохранить':
            if ((user[str(message.chat.id)]['children']) != None) and ((user[str(message.chat.id)]['maks']) != None) and ((user[str(message.chat.id)]['pr']) != None) and ((user[str(message.chat.id)]['otdel']) != None):
                if message.chat.id != 2096176956:
                    bot.send_message(chat_id=2096176956, text=(time_string + '\n' + 'Учитель: ' + teacher(message.from_user.id) + '\n' + 'Ученик: ' + (user[str(message.chat.id)]['children']) + '\n' + 'Предмет: ' + (user[str(message.chat.id)]['pr']) + '\n' + 'Оценка: '+ (user[str(message.chat.id)]['maks']) + '\n' + 'Отделение: '  + (user[str(message.chat.id)]['otdel'])))             
                if message.chat.id != 389412849:
                    bot.send_message(chat_id=389412849, text=(time_string + '\n' + 'Учитель: ' + teacher(message.from_user.id) + '\n' + 'Ученик: ' + (user[str(message.chat.id)]['children']) + '\n' + 'Предмет: ' + (user[str(message.chat.id)]['pr']) + '\n' + 'Оценка: '+ (user[str(message.chat.id)]['maks']) + '\n' + 'Отделение: '  + (user[str(message.chat.id)]['otdel'])))
                if message.chat.id != 5156347056:
                    bot.send_message(chat_id=5156347056, text=(time_string + '\n' + 'Учитель: ' + teacher(message.from_user.id) + '\n' + 'Ученик: ' + (user[str(message.chat.id)]['children']) + '\n' + 'Предмет: ' + (user[str(message.chat.id)]['pr']) + '\n' + 'Оценка: '+ (user[str(message.chat.id)]['maks']) + '\n' + 'Отделение: '  + (user[str(message.chat.id)]['otdel'])))              
                bot.send_message(message.chat.id,time_string + '\n' + 'Ученик: ' + (user[str(message.chat.id)]['children']) + '\n' + 'Предмет: ' + (user[str(message.chat.id)]['pr']) + '\n' + 'Оценка: '+ (user[str(message.chat.id)]['maks']) + '\n' + 'Отделение: '  + (user[str(message.chat.id)]['otdel']) + '\n' + 'Данные сохранены')
                vstavka(user[str(message.chat.id)]['children'],teacher(message.from_user.id),int(person(message.from_user.id)),user[str(message.chat.id)]['pr'],int(1),user[str(message.chat.id)]['maks'],user[str(message.chat.id)]['otdel'])
                back(message)
            else:
                bot.send_message(message.chat.id, text="Понабирают по объявлению! А где остальная информация!?")
        elif user[str(message.chat.id)]['mes'] == 'Назад':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            back(message)
        elif user[str(message.chat.id)]['mes'] == 'Помощь':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
                'Для выставления оценки за предмет необходимо:' + '\n' + 
                '---------------------------------' + '\n' + 
                '1) Выбрать ученика из списка' + '\n' + 
                '2) Выбрать нужный предмет' + '\n' + 
                '3) Выбрать оценку, если оценки нет то +' + '\n' + 
                '4) Выбрать отделение' + '\n' +
                '5) Нажать сохранить' + '\n' + 
                '---------------------------------' + '\n' + 
                'Для фиксации дополнительных занятий:' + '\n' + 
                '---------------------------------' + '\n' + 
                '1) Выбрать ученика из списка' + '\n' + 
                '2) Если ученика нет, добавить его' + '\n' + 
                '3) Для добавления использовать слово' + '\n' + 
                '   >Добавить ФИО<' + '\n' +
                '5) Выбрать оставшиеся пункты и нажать сохранить')
            back(message)
        elif user[str(message.chat.id)]['mes'] == 'Табель c оценками':
            bot.send_message(message.chat.id,'Для просмотра занятий внесенных в'  + '\n' + 'ведомость перейдите по ссылке на сайт:' + '\n' + 'https://itlama.ru/UchimZnaem.php')
        
        elif user[str(message.chat.id)]['mes'] == 'Сетевая папка':
            if ip == '146.120.176.103':
                bot.send_message(message.chat.id,'Доспут к папке сейчас закрыт')
            else:
                bot.send_message(message.chat.id,'Для доступа в папку используем: ' + '\n' + 'адрес: ftp://' + ip + '/UchimZnaem' + '\n' + 'логин: server' + '\n' + 'пароль: 1234')
        else:

            bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
            back(message)
    except:
        return  (
                bot.send_message(message.chat.id, text="Данные не загружены"),
                print(message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.from_user.id),
                dannie_error(message))
        
    #--------------------------------------------------------------

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = telebot.types.KeyboardButton("Загрузить данные")
    markup.add(btn3)
    user_info = {}
    user_id = {}
    user_info = str(message.from_user.username) + ' ' + str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(message.from_user.id)
    user_id = message.from_user.id
    print('Новый пользователь: ',user_info)
    my_file = open(str(user_id)+'.txt', "w+")
    my_file.write(user_info)
    my_file.close()
    bot.send_message(message.chat.id,"{}, чем я могу помочь?"
        .format(message.from_user.first_name,
                message.from_user.id), disable_web_page_preview=True, parse_mode="Markdown",reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    user [str(message.chat.id)]['mes'] = message.text
    named_tuple = time.localtime()
    ti = time.strftime('%H:%M:%S', named_tuple)
    print(ti, str(message.from_user.last_name),str(message.from_user.first_name), message.text)
    if message.text == 'Загрузить данные':
        dannie(message)
    else:
        uroki(message)

  #--------------------------------------------------------------     
def back(m):
        global chil
        global sub

        chil = None
        sub = None
        user[str(m.chat.id)]['maks'] = None
        user[str(m.chat.id)]['children'] = None
        user[str(m.chat.id)]['otdel'] = None
        user[str(m.chat.id)]['pr'] = None
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Ведомость")
        btn2 = telebot.types.KeyboardButton("Помощь")
        btn3 = telebot.types.KeyboardButton("Сетевая папка")
        btn4 = telebot.types.KeyboardButton("Табель c оценками")
        if user[str(m.chat.id)]['login'] != None:
            btn5 = telebot.types.KeyboardButton("МЭО")
            markup.add(btn1,btn2,btn3,btn4,btn5)
        else:
            markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(m.chat.id,"{}, чем я могу помочь?"
            .format(m.from_user.first_name,
                    m.from_user.id), disable_web_page_preview=True, parse_mode="Markdown",reply_markup=markup)

def dannie_error(m):
        global chil
        global sub
        chil = None
        sub = None
        user[str(m.chat.id)]['maks'] = None
        user[str(m.chat.id)]['children'] = None
        user[str(m.chat.id)]['otdel'] = None
        user[str(m.chat.id)]['pr'] = None
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Загрузить данные")
        markup.add(btn1)
        bot.send_message(m.chat.id,"{}, профиль пользователя не загружен"
            .format(m.from_user.first_name,
                    m.from_user.id), disable_web_page_preview=True, parse_mode="Markdown",reply_markup=markup)

def person(chat_id):
  myconn = MySQLdb.connect(host = "141.8.194.164",user = "f0556993_school",password = "533582baaB",db = "f0556993_school")
  cur = myconn.cursor()
  cur.execute("select t_id, fio, predmet from teacher") 
  result = cur.fetchall()
  k = 0
  for i in range(len(result)):
    if result[i][0] == chat_id:
      k = 1
      break
  if k == 1:
    return (result[i][0])

#--------------------------------------------------------------

def vstavka(chil, teach, t_id, predmet, kontrol, maks,otdel):
    myconn = MySQLdb.connect(host = "141.8.194.164",user = "f0556993_school",password = "533582baaB",db = "f0556993_school")
    cur = myconn.cursor()
    named_tuple = time.localtime()
    ti = time.strftime('%H:%M:%S', named_tuple)
    data = time.strftime("%Y-%m-%d", named_tuple)
    sql = "INSERT INTO tabel(id, data, time, children, teacher, t_id, predmet, kontrol, maks,otdel) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =("",data,ti,chil,teach,t_id,predmet,kontrol,maks,otdel) 
        
    try: 
        cur.execute(sql,val) 
        myconn.commit() 
        print(ti, teach, "Данные добавлены в базу данных id:",cur.lastrowid) 
    except: 
        myconn.rollback() 
    
    myconn.close() 
#--------------------------------------------------------------

#--------------------------------------------------------------

def teacher(t_id):
    myconn = MySQLdb.connect(host = "141.8.194.164",user = "f0556993_school",password = "533582baaB",db = "f0556993_school")
    cur = myconn.cursor()
    cur.execute("select fio from teacher where t_id = " + str(t_id)) 
    result = cur.fetchall()
    return (result[0][0])

#--------------------------------------------------------------

def predmet(t_id):
    myconn = MySQLdb.connect(host = "141.8.194.164",user = "f0556993_school",password = "533582baaB",db = "f0556993_school")
    cur = myconn.cursor()
    m =[]
    cur.execute("select predmet from teacher where t_id = " + str(t_id)) 
    result = cur.fetchall()
    for i in range(len(result)):
        m.append(result[i][0])
    return (m)

#--------------------------------------------------------------

#--------------------------------------------------------------

def klass(t_id):
    myconn = MySQLdb.connect(host = "141.8.194.164",user = "f0556993_school",password = "533582baaB",db = "f0556993_school")
    cur = myconn.cursor()
    cur.execute("select DISTINCT klass from teacher where t_id = " + str(t_id)) 
    result = cur.fetchall()
    ch =  list(set(reduce(lambda acc, x: [*map(int,acc), *map(int, x)], list(map(lambda x: x.split(","),[",".join(x) for x in (result)])))))
    return (ch)

def child(kl):
    myconn = MySQLdb.connect(host = "141.8.194.164",user = "f0556993_school",password = "533582baaB",db = "f0556993_school")
    cur = myconn.cursor()
    m =[]
    for a in kl:
        cur.execute("select fio from student where klass = " + str(a) +" and time_v = 0000-00-00")
        result = cur.fetchall()
        for i in range(len(result)):
            m.append(result[i][0])
    return (m)

#--------------------------------------------------------------

def telegram_polling():
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        traceback_error_string=traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(100)
        telegram_polling()
telegram_polling()