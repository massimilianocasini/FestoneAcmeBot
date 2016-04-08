#!/usr/bin/env python 
 
import telegram.ext
import logging

import time
import os				
import os.path				

from random import randint	
	
# Enable logging
logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.INFO)

logger = logging.getLogger(__name__)

def cmd_start(bot, update):
	bot.sendMessage(update.message.chat_id, "Ciao ! Sono il video box del Festone Acme. Manda il tuo video ;-) \n");
	

def echo(bot, update):	
	print " Username  : [" + update.message.from_user.username + "]" ,
	print " Firstname : [" + update.message.from_user.first_name + "]" ,
	print " Lastname  : [" + update.message.from_user.last_name + "]"
 
	if update.message.video:
		newFile = bot.getFile(update.message.video.file_id)

		while True:	
			filename="video/V%06d.mov" % randint(1,999999);
			if os.path.isfile(filename):
				continue
			else:
				newFile.download(filename)
				bot.sendMessage(update.message.chat_id, text="Grazie ! Video ricevuto ;-)")
				#os.system("vlc -f --video-on-top --no-video-title-show  video &")
				break	
			
def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():	
	global update_queue
	global screen
	
	#@SpennellandoBot
	updater = telegram.ext.Updater("190231325:AAFgJ39Trmn1t4RsucDB6djLg64C1WVnNSE")	
	
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
