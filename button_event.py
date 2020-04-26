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
    def question_a(self):
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

    def question_b(self):
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

    def question_c(self):
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

    def question_d(self):
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

    def question_e(self):
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

    def question_f(self):
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

    def question_g(self):
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
                    text='二刀流エンジニア'
                  ),
                  MessageAction(
                    label='No',
                    text='モチベーションエンジニア'
                  )
                ]
            )
        )
        return button_template

    def answer_h(self):
        button_template = TemplateSendMessage(
            alt_text="ジェネラルエンジニア",
            template=ButtonsTemplate(
                title="ジェネラルエンジニア",
                text="あなたはチーム開発における、リーダーやマネージャーに向いています。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return button_template

    def answer_i(self):
        button_template = TemplateSendMessage(
            alt_text="キラキラエンジニア",
            template=ButtonsTemplate(
                title="キラキラエンジニア",
                text="あなたはエンジニア以外ともうまく付き合うことができ、営業と開発を同時に行えます。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return button_template

    def answer_j(self):
        button_template = TemplateSendMessage(
            alt_text="アーティストエンジニア",
            template=ButtonsTemplate(
                title="アーティストエンジニア",
                text="あなたはデザイン、コード、などを拘ることで質の高いものを作ることができます。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return button_template

    def answer_k(self):
        button_template = TemplateSendMessage(
            alt_text="スポンジエンジニア",
            template=ButtonsTemplate(
                title="スポンジエンジニア",
                text="あなたは何色にでも染まるタイプです。チーム開発では周りに合わせることが得意。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                  
                ]
            )
        )
        return button_template

    def answer_l(self):
        button_template = TemplateSendMessage(
            alt_text="自由奔放エンジニア",
            template=ButtonsTemplate(
                title="自由奔放エンジニア",
                text="あなたは好きなものを自分のペースで作る力に長けています。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                  
                ]
            )
        )
        return button_template

    def answer_m(self):
        button_template = TemplateSendMessage(
            alt_text="超集中エンジニア",
            template=ButtonsTemplate(
                title="超集中エンジニア",
                text="あなたは一度集中すると完成するまでプログラミングを続けてしまう才能があります。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                  
                ]
            )
        )
        return button_template

    def answer_n(self):
        button_template = TemplateSendMessage(
            alt_text="二刀流エンジニア",
            template=ButtonsTemplate(
                title="二刀流エンジニア",
                text="あなたはフロントエンド・バックエンド問わず学習することができます。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return button_template

    def answer_o(self):
        button_template = TemplateSendMessage(
            alt_text="モチベーションエンジニア",
            template=ButtonsTemplate(
                title="モチベーションエンジニア",
                text="あなたは報酬や成果があると凄まじい力を発揮します。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return button_template