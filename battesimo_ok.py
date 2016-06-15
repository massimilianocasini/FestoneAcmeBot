#!/usr/bin/env python 
 
import telegram
import logging

import time
import os				
import os.path				

from random import randint	
	
# Enable logging
logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.DEBUG)

logger = logging.getLogger(__name__)

def cmd_start(bot, update):
	bot.sendMessage(update.message.chat_id, "Ciao ! Sono il VIDEOBOX del Battesimo di Sofia e Federico. Contribuisci al video ricordo!!! Fai un VIDEO o scatta una FOTO con il tuo cellulare e invialo!! \n");
	
#Definisco le variabili globali
def echo(bot, update):	
	global username
	global firstLastname
	global ringraziamentoText
	global sticker_image_file_webp
	print " Username  : [" + update.message.from_user.username + "]" ,
	print " Firstname : [" + update.message.from_user.first_name + "]" ,
	print " Lastname  : [" + update.message.from_user.last_name + "]" ,

	username = update.message.from_user.username
	firstname = update.message.from_user.first_name
	firstLastname = update.message.from_user.first_name+"_"+update.message.from_user.last_name
	ringraziamentoText = 'Grazie ' +firstname+'! \n Ho ricevuto il tuo Upload!! \n Tra qualche giorno riceverai, sul tuo account Telegram, il video ricordo di questo giorno!'
	sticker_image_file_webp = open("minions.webp")
	
	if update.message.video:
		newVideo = bot.getFile(update.message.video.file_id)
		
		while True:	
	
			filename="download/video_"+username+"_"+firstLastname+"_%d.mov" % randint(1,999999);
			if os.path.isfile(filename):
				continue
			else:
				newVideo.download(filename)
				bot.sendMessage(update.message.chat_id, text=ringraziamentoText)
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
				bot.sendDocument(update.message.chat_id, document= sticker_image_file_webp);
				bot.sendMessage(update.message.chat_id, text=ringraziamentoText);
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
				bot.sendDocument(update.message.chat_id, document= sticker_image_file_webp);
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
				#Invia uno sticker su base sticker.file_id
				#bot.sendSticker(update.message.chat_id, sticker= 'BQADBAADHAADyIsGAAFZfq1bphjqlgI');
				
				#Invia uno sticker su base file presente sul disco
				#bot.sendDocument(update.message.chat_id, document= sticker_image_file_pdf);
				#bot.sendSticker(update.message.chat_id, sticker= sticker_image_file_fede);
				#bot.sendSticker(update.message.chat_id, sticker= sticker_image_file_sofi);
				bot.sendDocument(update.message.chat_id, document= sticker_image_file_webp);
				bot.sendMessage(update.message.chat_id, text=ringraziamentoText);
				break
				
def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():	
	global update_queue
	global screen
	
	updater = telegram.Updater("210389773:AAEfUq6tMf87Zb2g209hmL0SAJKUz8XbBhI")	
	
	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# Definisce gli handler di gestione dei comandi
	dp.addTelegramCommandHandler("start", cmd_start)
		
	# on noncommand i.e message - echo the message on Telegram
	dp.addTelegramMessageHandler(echo)

	# log all errors
	dp.addErrorHandler(error)

	# Start the Bot
	update_queue = updater.start_polling()


	try:  
		# Run the bot until the you presses Ctrl-C or the process receives SIGINT,
		# SIGTERM or SIGABRT. This should be used most of the time, since
		# start_polling() is non-blocking and will stop the bot gracefully.
		updater.idle()

	except KeyboardInterrupt:  
		print "Exit"	

if __name__ == '__main__':
	main()
