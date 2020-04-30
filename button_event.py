
import os

# ButtonsTemplate -> 返信時のbuttonのtemplate
# URIAction ->
from linebot.models import (
    ImageSendMessage, FollowEvent, UnfollowEvent, MessageEvent, PostbackEvent,
    TextMessage, TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, CarouselTemplate, CarouselColumn,
    PostbackTemplateAction,URIAction,MessageAction
)

url_current_path = 'https://line-ilan.herokuapp.com/image/'

# def make_button_template():
#     message_template = TemplateSendMessage(
#         alt_text="[緊急]",
#         template=ButtonsTemplate(
#             text="ボタン押したらどこかに飛ぶよ！",)
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
                thumbnail_image_url=url_current_path+'A.png',
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
                thumbnail_image_url=url_current_path+'B.png',
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
                thumbnail_image_url=url_current_path+'C.png',
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
                thumbnail_image_url=url_current_path+'D.png',
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
                thumbnail_image_url=url_current_path+'E.png',
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
                thumbnail_image_url=url_current_path+'F.jpg',
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
                thumbnail_image_url=url_current_path+'G.png',
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

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'H.png',
            preview_image_url=url_current_path+'H.png'
        )

        button_template = TemplateSendMessage(
            alt_text="ジェネラルエンジニア",
            template=ButtonsTemplate(
                text="あなたはチーム開発における、リーダーやマネージャーに向いています。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return [image_message,button_template]

    def answer_i(self):

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'I.png',
            preview_image_url=url_current_path+'I.png'
        )

        button_template = TemplateSendMessage(
            alt_text="キラキラエンジニア",
            template=ButtonsTemplate(
                text="あなたはエンジニア以外ともうまく付き合うことができ、営業と開発を同時に行えます。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return [image_message,button_template]

    def answer_j(self):

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'J.png',
            preview_image_url=url_current_path+'J.png'
        )

        button_template = TemplateSendMessage(
            alt_text="アーティストエンジニア",
            template=ButtonsTemplate(
                text="あなたはデザイン、コード、などを拘ることで質の高いものを作ることができます。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return [image_message,button_template]

    def answer_k(self):

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'K.png',
            preview_image_url=url_current_path+'K.png'
        )

        button_template = TemplateSendMessage(
            alt_text="スポンジエンジニア",
            template=ButtonsTemplate(
                text="あなたは何色にでも染まるタイプです。チーム開発では周りに合わせることが得意。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                  
                ]
            )
        )
        return [image_message,button_template]

    def answer_l(self):

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'L.png',
            preview_image_url=url_current_path+'L.png'
        )

        button_template = TemplateSendMessage(
            alt_text="自由奔放エンジニア",
            template=ButtonsTemplate(
                text="あなたは好きなものを自分のペースで作る力に長けています。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                  
                ]
            )
        )
        return [image_message,button_template]

    def answer_m(self):

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'M.png',
            preview_image_url=url_current_path+'M.png'
        )

        button_template = TemplateSendMessage(
            alt_text="超集中エンジニア",
            template=ButtonsTemplate(
                text="あなたは一度集中すると完成するまでプログラミングを続けてしまう才能があります。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                  
                ]
            )
        )
        return [image_message,button_template]

    def answer_n(self):

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'N.png',
            preview_image_url=url_current_path+'N.png'
        )

        button_template = TemplateSendMessage(
            alt_text="二刀流エンジニア",
            template=ButtonsTemplate(
                text="あなたはフロントエンド・バックエンド問わず学習することができます。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return [image_message,button_template]

    def answer_o(self):

        image_message = ImageSendMessage(
            original_content_url=url_current_path+'O.png',
            preview_image_url=url_current_path+'O.png'
        )

        button_template = TemplateSendMessage(
            alt_text="モチベーションエンジニア",
            template=ButtonsTemplate(
                text="あなたは報酬や成果があると凄まじい力を発揮します。ハッカソンに出てみてはいかがでしょう？",
                actions=[
                  URIAction(
                    uri="https://hackz.connpass.com/event/138742/",
                    label="開催中のハッカソン"
                  )
                ]
            )
        )
        return [image_message,button_template]
