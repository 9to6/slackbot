# -*- coding: utf-8 -*-
from slackbot.bot import Bot, respond_to
import re
import json
from coinone import *


@respond_to('.*')
def help(message):
    message.reply(("avaliable command list:\n"
                  "*btc*, *bch*, *eth*, *etc*, *xrp*, *qtum*, *ltc*, *iota*"))
    # message.reply("못알아먹겠소")


@respond_to('github', re.IGNORECASE)
def github(message):
    attachments = [{
        'fallback': '깃허브',
        'author_name': '9to6',
        'author_link': 'https://github.com/9to6',
        'text': '이 사이트 말씀하신건가요?\nhttps://github.com/9to6',
        'color': '#59afe1'
    }]
    message.reply_webapi('혹시 이거?', json.dumps(attachments))

@respond_to('btc', re.IGNORECASE)
def btc(message):
    attachments = SlackResponder.currency("btc")
    message.reply_webapi('', json.dumps(attachments))

@respond_to('bch', re.IGNORECASE)
def btc(message):
    attachments = SlackResponder.currency("bch")
    message.reply_webapi('', json.dumps(attachments))

@respond_to('eth', re.IGNORECASE)
def eth(message):
    attachments = SlackResponder.currency("eth")
    message.reply_webapi('', json.dumps(attachments))

@respond_to('etc', re.IGNORECASE)
def etc(message):
    attachments = SlackResponder.currency("etc")
    message.reply_webapi('', json.dumps(attachments))

@respond_to('xrp', re.IGNORECASE)
def xrp(message):
    attachments = SlackResponder.currency("xrp")
    message.reply_webapi('', json.dumps(attachments))

@respond_to('qtum', re.IGNORECASE)
def qtum(message):
    attachments = SlackResponder.currency("qtum")
    message.reply_webapi('', json.dumps(attachments))

@respond_to('ltc', re.IGNORECASE)
def ltc(message):
    attachments = SlackResponder.currency("ltc")
    message.reply_webapi('', json.dumps(attachments))

@respond_to('iota', re.IGNORECASE)
def iota(message):
    attachments = SlackResponder.currency("iota")
    message.reply_webapi('', json.dumps(attachments))

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
