#!/usr/bin/env python3.4 
# -*- coding: utf-8 -*-
 
import telegram
import logging

import time
import os				
import os.path				

from telegram import Emoji, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

from random import randint
from configobj import ConfigObj	
	
# Enable logging
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG) #livello DEBUG
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) #livello INFO
logger = logging.getLogger(__name__)

global log
photo_counter=0
##########################################################

# Config file inserire token nel file .ini
config_ini = ConfigObj('config.ini')
log = config_ini['GestioneLog']['log']
telegram_token = config_ini['TokenBotTelegram']['telegram_token']

help_text = (
	"<b>Comandi per la gestione degli utenti:</b>\n"
	"/userslist Visualizza lista di tutti gli utenti\n"
	"/users Visualizza lista utenti\n"
	"/bans Visualizza lista bannati\n"
	"/deluser Visualizza lista utenti per la cancellazione\n"
	"/delban Visualizza lista bannati per la cancellazione\n"
	"/delallusers Cancella tutti gli utenti\n"
	"/delallbans Cancella tutti gli utenti bannati\n"
)

clear_keyboard = telegram.ReplyKeyboardHide()

def cmd_start(bot, update):
	bot.sendMessage(update.message.chat_id, "Ciao ! Sono il VIDEOBOX del Battesimo di Sofia e Federico. Contribuisci al video ricordo!!! Fai un VIDEO o scatta una FOTO con il tuo cellulare e invialo!! \n");
	

def messaggi_in_arrivo(bot, update):
#Definisco le variabili globali	
	global username
	global firstLastname
	global ringraziamentoText
	global sticker_image_file_webp
	global photo_counter
	print (" Username  : [" + update.message.from_user.username + "]") ,
	print (" Firstname : [" + update.message.from_user.first_name + "]") ,
	print (" Lastname  : [" + update.message.from_user.last_name + "]") ,

	username = update.message.from_user.username
	firstname = update.message.from_user.first_name
	firstLastname = update.message.from_user.first_name+"_"+update.message.from_user.last_name
	
	ringraziamentoText = 'Grazie ' +firstname+'! \n Ho ricevuto il tuo Upload!! \n Tra qualche giorno riceverai, sul tuo account Telegram, il video ricordo di questo giorno!'
	sticker_image_file_webp = open("pippo.webp")
	file_id='BQADBAADmAQAAvOYrgABM1S-cXknovMC'
	
	if update.message.video:
		video_id = update.message.video.file_id
		newVideo = bot.getFile(video_id)
		
		while True:	
	
			filename="download/video_"+username+"_"+firstLastname+"_%d.mov" % randint(1,999999);
			if os.path.isfile(filename):
				continue
			else:
				newVideo.download(filename)
				bot.sendSticker(update.message.chat_id, sticker=file_id);
				bot.sendMessage(update.message.chat_id, text=ringraziamentoText);
				video_counter = video_counter +1
				if log == "INFO" :
					print ("Sono nella routine Video, Video ricevuti:", video_counter)
				#os.system("vlc -f --video-on-top --no-video-title-show  video &")
				break


	if update.message.photo:
	# indice 0 foto piccolissima, 1 foto piccola, 2 foto media, 3 foto grande
			
		photo_id = update.message.photo[-1].file_id
		photo_file = bot.getFile(photo_id)
		
		while True:	
		
			filename="download/foto_"+username+"_"+firstLastname+"_%d.jpg" % randint(1,999999);
			#filename="download/foto_"+username+"_"+firstLastname+"_"+photo_id+".jpg"
			if os.path.isfile(filename):
				continue
			else:
				photo_file.download(filename)
				bot.sendSticker(update.message.chat_id, sticker=file_id);
				bot.sendMessage(update.message.chat_id, text=ringraziamentoText);
				photo_counter = photo_counter +1
				if log == "INFO" :
					print ("Sono nella routine Photo, Photo ricevute:", photo_counter)
				break
				
	if update.message.document:
	
		document_id = update.message.document.file_id
		document_name = update.message.document.file_name
		document_file = bot.getFile(document_id)
		while True:	
		
			filename="download/"+username+"_"+firstLastname+"_"+document_name;
			if os.path.isfile(filename):
				continue
			else:
				document_file.download(filename)
				bot.sendSticker(update.message.chat_id, sticker=file_id);
				bot.sendMessage(update.message.chat_id, text=ringraziamentoText);
				break	
				
				

	if update.message.sticker:
		#sticker_image_file_fede = open("federico.jpg")
		#sticker_image_file_sofi = open("sofia.jpg")
		#sticker_image_file_pdf = open("battesimo.pdf")
		#sticker_image_file_webp = open("minions.webp")
		
		sticker_id = update.message.sticker.file_id
		sticker_file = bot.getFile(sticker_id)
		while True:	
		
			filename="download/"+sticker_id+"_%d.webp" % randint(1,999999);
			if os.path.isfile(filename):
				continue
			else:
				sticker_file.download(filename)
				bot.sendSticker(update.message.chat_id, sticker=file_id);
				bot.sendMessage(update.message.chat_id, text=ringraziamentoText);
				break

def menu(bot, update):
	#Prima di elaborare un comando controlla che tipo di utente e':
	bot.sendMessage(update.message.chat_id, help_text, parse_mode=telegram.ParseMode.HTML, reply_markup=clear_keyboard);
		
				
def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():	
	global update_queue
	global screen
	
	#updater = telegram.Updater("210389773:AAEfUq6tMf87Zb2g209hmL0SAJKUz8XbBhI")	
	#updater = telegram.Updater(telegram_token)
	# Get the dispatcher to register handlers
	#dp = updater.dispatcher

	# Definisce gli handler di gestione dei comandi
	#dp.addTelegramCommandHandler("start", cmd_start)
		
	# on noncommand i.e message - echo the message on Telegram
	#dp.addTelegramMessageHandler(echo)

	# log all errors
	#dp.addErrorHandler(error)

	# Start the Bot
	#update_queue = updater.start_polling()

#updater.start_polling()
#updater.idle()

	#except KeyboardInterrupt:  
		#print ("Exit")	

if __name__ == '__main__':
	main()

	
updater = Updater(telegram_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler([Filters.photo, Filters.video],messaggi_in_arrivo))
dispatcher.add_handler(CommandHandler("start",cmd_start))
dispatcher.add_handler(CommandHandler("menu", menu))
dispatcher.add_handler(CommandHandler("help", menu))
#check.addAccessCheckCommandHandler(dispatcher)
updater.start_polling()
updater.idle()
