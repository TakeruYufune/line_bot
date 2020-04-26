# ButtonsTemplate -> 返信時のbuttonのtemplate
# URIAction ->
from linebot.models import (
    FollowEvent, UnfollowEvent, MessageEvent, PostbackEvent,
    TextMessage, TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, CarouselTemplate, CarouselColumn,
    PostbackTemplateAction,URIAction,MessageAction
)


# def make_button_template():
#     message_template = TemplateSendMessage(
#         alt_text="[緊急]",
#         template=ButtonsTemplate(
#             text="ボタン押したらどこかに飛ぶよ！",
#             title="どりーの部屋にようこそ",
#             image_size="cover",
#             thumbnail_image_url="https://national-flag.com/material/019-national-flag.jpg",
#             actions=[
#                 URIAction(
#                     uri="https://twitter.com/Friedrich_buryu",
#                     label="Twitter"
#                 ),
#                 URIAction(
#                     uri="https://hackz.team/",
#                     label="ウホウホウホ"
#                 )
#             ]
#         )
#     )
#     return message_template

class EngineerCheck:
    def question_a():
        button_template = TemplateSendMessage(
            alt_text="エンジニア診断Q1",
            template=ButtonsTemplate(
                image_size="cover",
                thumbnail_image_url="https://任意の画像URL.jpg",
                title="Question.1",
                text="プログラミング以外もやりたい",
                actions=[
                  PostbackTemplateAction(
                    label='Yes',
                    data='question_b'
                  ),
                  PostbackTemplateAction(
                    label='No',
                    data='question_c'
                  )
                ]
            )
        )
        return button_template

    def question_b(data: str):
        button_template = TemplateSendMessage(
            alt_text="エンジニア診断Q2",
            template=ButtonsTemplate(
                image_size="cover",
                thumbnail_image_url="https://任意の画像URL.jpg",
                title="Question.2",
                text="人と話すのは得意だ",
                actions=[
                  PostbackTemplateAction(
                    label='Yes',
                    data='question_d'
                  ),
                  PostbackTemplateAction(
                    label='No',
                    data='question_e'
                  )
                ]
            )
        )
        return button_template

    def question_c(data: str):
        button_template = TemplateSendMessage(
            alt_text="エンジニア診断Q2",
            template=ButtonsTemplate(
                image_size="cover",
                thumbnail_image_url="https://任意の画像URL.jpg",
                title="Question.2",
                text="世界は自分中心に回っている",
                actions=[
                  PostbackTemplateAction(
                    label='Yes',
                    data='question_f'
                  ),
                  PostbackTemplateAction(
                    label='No',
                    data='question_g'
                  )
                ]
            )
        )
        return button_template

    def question_d(data: str):
        button_template = TemplateSendMessage(
            alt_text="エンジニア診断Q3",
            template=ButtonsTemplate(
                image_size="cover",
                thumbnail_image_url="https://任意の画像URL.jpg",
                title="Question.3",
                text="人を支配するのが好きだ",
                actions=[
                  MessageAction(
                    label='Yes',
                    text='ジェネラルエンジニア'
                  ),
                  MessageAction(
                    label='No',
                    text='キラキラエンジニア'
                  )
                ]
            )
        )
        return button_template

    def question_e(data: str):
        button_template = TemplateSendMessage(
            alt_text="エンジニア診断Q3",
            template=ButtonsTemplate(
                image_size="cover",
                thumbnail_image_url="https://任意の画像URL.jpg",
                title="Question.3",
                text="こだわりが強いタイプだ",
                actions=[
                  MessageAction(
                    label='Yes',
                    text='アーティストエンジニア'
                  ),
                  MessageAction(
                    label='No',
                    text='スポンジエンジニア'
                  )
                ]
            )
        )
        return button_template

    def question_f(data: str):
        button_template = TemplateSendMessage(
            alt_text="エンジニア診断Q3",
            template=ButtonsTemplate(
                image_size="cover",
                thumbnail_image_url="https://任意の画像URL.jpg",
                title="Question.3",
                text="同時に複数のことができる",
                actions=[
                  MessageAction(
                    label='Yes',
                    text='自由奔放エンジニア'
                  ),
                  MessageAction(
                    label='No',
                    text='超集中エンジニア'
                  )
                ]
            )
        )
        return button_template

    def question_g(data: str):
        button_template = TemplateSendMessage(
            alt_text="エンジニア診断Q3",
            template=ButtonsTemplate(
                image_size="cover",
                thumbnail_image_url="https://任意の画像URL.jpg",
                title="Question.3",
                text="自分に自信がない",
                actions=[
                  MessageAction(
                    label='Yes',
                    text='フルスタックエンジニア'
                  ),
                  MessageAction(
                    label='No',
                    text='モチベーションエンジニア'
                  )
                ]
            )
        )
        return button_template
