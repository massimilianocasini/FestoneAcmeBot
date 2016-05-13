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
	bot.sendMessage(update.message.chat_id, "Ciao ! Sono il video box del Battesimo di Sofia e Federico. Contribuisci al ricordo mandando il tuo video oppure la tua foto  ;-) \n");
	

def echo(bot, update):	
	global username
	global firstLastname
	print " Username  : [" + update.message.from_user.username + "]" ,
	print " Firstname : [" + update.message.from_user.first_name + "]" ,
	print " Lastname  : [" + update.message.from_user.last_name + "]" ,

	username = update.message.from_user.username
	firstLastname = update.message.from_user.first_name+"_"+update.message.from_user.last_name
	
	
	if update.message.video:
		newVideo = bot.getFile(update.message.video.file_id)
		
		while True:	
		#	filename="download/video_"+update.message.from_user.first_name+"_%d.mov" % randint(1,999999);
			filename="download/video_"+username+"_"+firstLastname+"_%d.mov" % randint(1,999999);
			if os.path.isfile(filename):
				continue
			else:
				newVideo.download(filename)
				bot.sendMessage(update.message.chat_id, text='Grazie ' +update.message.from_user.first_name+ '! Video ricevuto ;-)')
				#os.system("vlc -f --video-on-top --no-video-title-show  video &")
				break


	if update.message.photo:
		photo_id = update.message.photo[-1].file_id
		photo_file = bot.getFile(photo_id)
		while True:	
		#	filename="download/foto_"+update.message.from_user.first_name+"_%d.jpg" % randint(1,999999);
			filename="download/foto_"+username+"_"+firstLastname+"_%d.jpg" % randint(1,999999);
			if os.path.isfile(filename):
				continue
			else:
				photo_file.download(filename)
				bot.sendMessage(update.message.chat_id, text='Grazie ' +update.message.from_user.first_name+ '! Foto ricevuta ;-)')
				break
		
def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():	
	global update_queue
	global screen
	
<<<<<<< HEAD
	
	#@SpennellandoBot
=======
	#@MisiBot
>>>>>>> 1cb2f32241ff6353bec0fecad248460c6b52e50b
	updater = telegram.Updater("138682670:AAGpVS2brpdVCpJ872ZGl5sbe9KQbFUjAZQ")	
	
	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# Definisce gli handler di gestione dei comandi
	dp.addTelegramCommandHandler("start",   cmd_start)
		
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
