# -*- coding: utf-8 -*-

import os
import sys
import json

# try:
#     import MySQLdb
# except:
#     import pymysql
#     pymysql.install_as_MySQLdb()
#     import MySQLdb

from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import ( # 使用するモデル(イベント, メッセージ, アクションなど)を列挙
    FollowEvent, UnfollowEvent, MessageEvent, PostbackEvent,
    TextMessage, TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, CarouselTemplate, CarouselColumn,
    PostbackTemplateAction,URIAction
)

# 自作のbutton_eventライブラリをimport
import button_event

app = Flask(__name__)

# インスタンス化
engineer_check = button_event.EngineerCheck()

# インスタンス化
follow_event = button_event.FollowUpEvent()

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
with open(ABS_PATH+'/conf.json', 'r') as f:
    CONF_DATA = json.load(f)

CHANNEL_SECRET = CONF_DATA['CHANNEL_SECRET']
CHANNEL_ACCESS_TOKEN = CONF_DATA['CHANNEL_ACCESS_TOKEN']
REMOTE_HOST = CONF_DATA['REMOTE_HOST']
REMOTE_DB_NAME = CONF_DATA['REMOTE_DB_NAME']
REMOTE_DB_USER = CONF_DATA['REMOTE_DB_USER']
REMOTE_DB_PASS = CONF_DATA['REMOTE_DB_PASS']
REMOTE_DB_TB = CONF_DATA['REMOTE_DB_TB']

if CHANNEL_SECRET is None:
    print('Specify LINE_CHANNEL_SECRET.')
    sys.exit(1)
if CHANNEL_ACCESS_TOKEN is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN.')
    sys.exit(1)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# https://アプリ名.herokuapp.com/test にアクセスしてtest okが表示されればデプロイ自体は成功してる
# flaskは@app.route("/ディレクトリ名")でルーティングする
@app.route("/test")
def test():
    return('test ok')

# LINE APIにアプリがあることを知らせるためのもの
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# メッセージが来た時の反応
@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    message_text = event.message.text

    if message_text == 'エンジニア診断':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.question_a()
        )
    elif message_text == 'ジェネラルエンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_h()
        )
    elif message_text == 'キラキラエンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_i()
        )
    elif message_text == 'アーティストエンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_j()
        )
    elif message_text == 'スポンジエンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_k()
        )
    elif message_text == '自由奔放エンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_l()
        )
    elif message_text == '超集中エンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_m()
        )
    elif message_text == '二刀流エンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_n()
        )
    elif message_text == 'モチベーションエンジニア':
        line_bot_api.reply_message(
            event.reply_token,
            engineer_check.answer_o()
        )

# 値が帰ってきたときの反応
@handler.add(PostbackEvent)
def on_postback(event):
    reply_token = event.reply_token
    user_id = event.source.user_id
    postback_msg = event.postback.data

    app.logger.info(postback_msg)

    question = getattr(engineer_check, postback_msg)

    # 次の質問投げつける
    line_bot_api.reply_message(
        event.reply_token,
        question()
    )


# Follow Event ## フォローとかブロックとか監視したいときに使う。まだ理解してない。
@handler.add(FollowEvent)
def on_follow(event):
    reply_token = event.reply_token
    user_id = event.source.user_id
    profiles = line_bot_api.get_profile(user_id=user_id)
    display_name = profiles.display_name
    picture_url = profiles.picture_url
    status_message = profiles.status_message

    # DBへの保存
    # try:
        # conn = MySQLdb.connect(user=REMOTE_DB_USER, passwd=REMOTE_DB_PASS, host=REMOTE_HOST, db=REMOTE_DB_NAME)
        # c = conn.cursor()
        # sql = "SELECT `id` FROM`"+REMOTE_DB_TB+"` WHERE `user_id` = '"+user_id+"';"
        # c.execute(sql)
        # ret = c.fetchall()
        # if len(ret) == 0:
        #     sql = "INSERT INTO `"+REMOTE_DB_TB+"` (`user_id`, `display_name`, `picture_url`, `status_message`, `status`)\
        #       VALUES ('"+user_id+"', '"+str(display_name)+"', '"+str(picture_url)+"', '"+str(status_message)+"', 1);"
        # elif len(ret) == 1:
        #     sql = "UPDATE `"+REMOTE_DB_TB+"` SET `display_name` = '"+str(display_name)+"', `picture_url` = '"+str(picture_url)+"',\
        #     `status_message` = '"+str(status_message)+"', `status` = '1' WHERE `user_id` = '"+user_id+"';"
        # c.execute(sql)
        # conn.commit()
    # finally:
    #     conn.close()
    #     c.close()

    # メッセージの送信
    line_bot_api.reply_message(
        reply_token=reply_token,
        messages=TextSendMessage(text='{Nickname}さん、はじめまして🇮🇷\n友だち追加ありがとうございます。\n自称イラン人のどりーです！\n「エンジニア診断」\nと送るとあなたがどんなエンジニアなのかを簡単に診断します。\nその他の相談や質問は随時受け付けています！')
        follow_event.follow_button()
    )

# def send_push_message(user_id=None, content=None):
#     if user_id is None or content is None:
#         return False
#     line_bot_api.push_message(
#         to=user_id,
#         messages=TextSendMessage(text='メッセージがPushされたよ！')
#     )

# def show_carousel(user_id): ## よくわかんない
#     carousel_columns = [
#         CarouselColumn(
#             text=value,
#             title=value+'の通知',
#             actions=[
#                 PostbackTemplateAction(
#                     label='ON',
#                     data=value+'1'
#                 ),
#                 PostbackTemplateAction(
#                     label='OFF',
#                     data=value+'0'
#                 )
#             ]
#         ) for key, value in (
#             zip(
#                 ('取引所', '取引所', '取引所', '取引所', '取引所'),
#                 ('Binance', 'KuCoin', 'Hupbipro', 'Poloniex', 'Bittrex')
#             )
#         )
#     ]
#     message_template = CarouselTemplate(columns=carousel_columns)
#     line_bot_api.push_message(
#         to=user_id,
#         messages=TemplateSendMessage(alt_text='carousel template', template=message_template)
#     )


if __name__ == "__main__":
    app.run(debug=True)
