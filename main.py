#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler

tokenfile = open("token", "r")
token = tokenfile.read().strip()


def start(bot, update):
    update.message.reply_text("""
Hola {}
Para usar este bot envia el codigo de la parada en la que estas.
Se te devolveran los buses que estan por llegar, y lo que tardaran en llegar
                              """.format(update.message.from_user.first_name))


def help(bot, update):
    update.message.reply_text("""
Para usar este bot envia el codigo de la parada en la que estas.
Se te devolveran los buses que estan por llegar, y lo que tardaran en llegar
""")


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()
