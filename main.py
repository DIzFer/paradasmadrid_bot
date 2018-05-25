#!/usr/bin/env python3

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tokens
from lib import obtener_autobuses, presentar_autobuses

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = tokens.TELEGRAM["token"]
ID_CLIENT = tokens.API_TRANSPORTES["id_client"]
KEY = tokens.API_TRANSPORTES["key"]


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

def obtener_parada(bot, update):
    update.message.reply_text(
        presentar_autobuses(
            obtener_autobuses(
                parada=update.message.text,
                claves={"id_client": ID_CLIENT, "key": KEY}
                )
            )
        )

UPDATER = Updater(TOKEN)

UPDATER.dispatcher.add_handler(CommandHandler('start', start))
UPDATER.dispatcher.add_handler(CommandHandler('help', help))
UPDATER.dispatcher.add_handler(CommandHandler('parada', obtener_parada))
UPDATER.dispatcher.add_handler(MessageHandler(Filters.text, obtener_parada))

UPDATER.start_polling()
UPDATER.idle()
