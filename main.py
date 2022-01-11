# -*- coding: utf-8 -*-

import telebot
from telebot import types

bot = telebot.TeleBot("1793774849:AAGIoPM9if4L7EjOAxwZXRamdGUG0QjW5gk")

@bot.message_handler(commands=['start'])
def welcome(message):
	stick = open('assets/stickers/hello.webp', 'rb')
	bot.send_sticker(message.chat.id, stick)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #аргумент для того, чтобы клавиатура была маленькой.
	button1 = types.KeyboardButton("Как получить ГДЗ?")
	button2 = types.KeyboardButton("Кто такой Тот?")
	button3 = types.KeyboardButton("По каким предметам есть ГДЗ?")

	markup.add(button1, button2, button3)

	bot.send_message(message.chat.id, 'Привет! Меня зовут Тот, я помогу тебе с выполнением домашки.\nВозможно, когда я достигну пика своего самопознания, ты сможешь использовать меня для каких-нибудь других целей)', parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def talking(message):
	if message.chat.type == 'private':
		if message.text.lower() == "спасибо" or message.text.lower() == "благодарю" or message.text.lower() == "благодарствую" or message.text.lower() == "от души":
			bot.send_message(message.chat.id, "Всегда пожалуйста)")
		if message.text == "Как получить ГДЗ?":
			bot.send_message(message.chat.id, "{0.first_name}, для того, чтобы получить ГДЗ, напиши мне сообщение в следующем виде:\n\n<strong>ГДЗ *класс* *название предмета* *номер задания*</strong>\n\nВсе это делается без запятых, через пробел. Вот пример:".format(message.from_user),
				parse_mode='HTML')
			bot.send_message(message.chat.id, "гдз 9 алгебра 123")		
			# bot.send_message(message.chat.id, 'гдз русский 212р')
		elif message.text.lower() == 'кто такой тот?':
			bot.send_message(message.chat.id, "Тот - древнеегипетский бог мудрости, знаний и счета. Так же он является покровителем библиотек и ученных, а теперь, видимо, еще и школяров, которые не в состоянии выполнить дз по алгебре... В общем, я конечно не бог, да и ты не ученный, так что могу помочь лишь с выполнением дз😉.")

		elif message.text.lower() == 'по каким предметам есть гдз?':
			bot.send_message(message.chat.id, "На данный момент для тебя доступны ГДЗ по алгебре, русскому и геометрии. Скором в этом списке появятся география и английский.")

		elif message.text.lower() == 'как дела?':
			answ = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

			answ.add(item1, item2)

			bot.send_message(message.chat.id, 'Отлично! Вот, пытаюсь подобрать наилучший алгоритм для взлома жо... Жилищно-коммунальных услуг. А у тебя?', reply_markup=answ)
		else:
			# Если ни одна из предыдущих команд не срабатывает, мы будем рассматривать то, что пользователь хочет получить гдз
			# для этого разделяем строку на список и проверяем, равен ли первый элемент "ГДЗ"
			req = message.text.lower().split()

			# Проверяю, чтобы запрос начинался на "гдз" и состоял минимум из 3х символов, чтобы не появлялась ошибка.
			if req[0] == 'гдз' and len(req) > 3:
				if req[2] == 'алгебра':
					try:
						req[3] = int(req[3])
						if req[3] > 0 and req[3] <= 1043:   
							photo = open('assets/GDZ/{0}/algebra/{1}.jpg'.format(req[1], req[3]), 'rb')
							bot.send_message(message.chat.id, "Не благодари😎")
							bot.send_photo(message.chat.id, photo)
						else:
							bot.send_message(message.chat.id, 'Извини, но решения данного номера у меня нет😢 (а возможно такого и вовсе не существует...)')
					except Exception as e:
						print(repr(e))
						bot.send_message(message.chat.id, 'Напоминаю: номера заданий указываются цифрами, а не другими видами символов.')
					
				elif req[2] == 'русский':
					try:
						req[3] = int(req[3])
						if req[3] > 0 and req[3] <= 282: 
							photo = open('assets/GDZ/{0}/russian/{1}.jpg'.format(req[1], req[3]), 'rb')
							bot.send_message(message.chat.id, "Всегда пожалуйста")
							bot.send_photo(message.chat.id, photo) 
						else:
							bot.send_message(message.chat.id, 'Извини, но решения данного номера у меня нет😢 (а возможно такого и вовсе не существует...)')
					except Exception as e:
						print(repr(e))
						bot.send_message(message.chat.id, 'Напоминаю: номера заданий указываются цифрами, а не другими видами символов.')
				elif req[2] == 'геометрия':
					try:
						req[3] = int(req[3])
						if req[3] > 0 and req[3] <= 1310: 
							photo = open('assets/GDZ/{0}/geometry/{1}.jpg'.format(req[1], req[3]), 'rb')
							bot.send_message(message.chat.id, "Держи")
							bot.send_photo(message.chat.id, photo) 
						else:
							bot.send_message(message.chat.id, 'Извини, но решения данного номера у меня нет😢 (а возможно такого и вовсе не существует...)')
					except Exception as e:
						print(repr(e))
						bot.send_message(message.chat.id, 'Напоминаю: номера заданий указываются цифрами, а не другими видами символов.')
				else:
					bot.send_message(message.chat.id, "Извини, но на данный момент у меня нет решений для этого предмета(")
			else:
				bot.send_message(message.chat.id, "Даже не знаю, что сказать")

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, "Супер😀")
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, "Ну бывает🙁")

			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отлично! Вот, пытаюсь подобрать наилучший алгоритм для взлома ж... Жилищно-коммунальных услуг. А у тебя?", reply_markup=None)
	except Exception as e:
		print(repr(e))

bot.polling()