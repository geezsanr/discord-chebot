import threading, queue
import gui
import chebot

q = queue.Queue()

bot = threading.Thread(target=chebot.discordBot)
#gui = threading.Thread(target=gui.main)
#bot.daemon=True
bot.start()

