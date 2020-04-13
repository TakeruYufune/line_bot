# line_bot
LINE Bot の練習

## Heroku の設定
1. Herokuに登録 ( https://jp.heroku.com/ )
2. create new app する

## LINE Developers の設定
1. LINE Developersに登録 ( https://developers.line.biz/ja/ )
2. プロダクトのMessaging APIにGO
3. 今すぐはじめよう
4. チャンネルの種類はMessaging APIのまま、他の項目を任意で設定して作成
5. チャネル基本設定タブ内の「チャネルシークレット」を発行(あとで使う)
6. Messaging API設定タブ内の「チャネルアクセストークン(ロングターム)」を発行(あとで使う)
7. 応答メッセージを無効に(API経由で応答するため)

## LINE の設定
LINE Developersのチャネル基本設定にLINE Official Account Manager のリンクがあるので、
そこから飛んで、ログイン(自分の個人LINEでOK)
そこでアイコンとか諸々変更できる。
(もし上記設定とか下記デプロイ方法で詰まったら、ここの設定が反映されてない場合があるので確認してみて。
自分はwebhookがdeveloperと違ってて動かないのを経験した。)

## conf.jsonの設定
"CHANNEL_SECRET"を自分の「チャネルシークレット」に変更
"CHANNEL_ACCESS_TOKEN"を自分の「チャネルアクセストークン(ロングターム)」に変更

## デプロイ方法
Herokuで作ったAppの「Open App」ボタンを押して、Viewを開く。
(mainはなんもいじってないのでnotFoundになるはず)
そこのリンク+"/callback"がwebhookになる。
webhookの設定は、LINE DevelopersのMessaging API設定内にあるので設定してwebhookの利用を有効にする。
(ちなみに同じ場所にあるQRコードで友達登録できるよ)
### GitHub の場合
Herokuで作ったAppのDeployタブ内にあるDeployment methodをGithubに変更
自分のアカウントとHerokuを紐付け。
Automatic deploysはgitにcommitがあったら自動でデプロイしてくれるやつ
Manual deployは手動でデプロイ(最初はこっちでいじいじした方が良き)
Manual deployのDeploy Branchを押してViewが出てくればDeploy完了
### Heroku Git の場合
コンソールで
$ heroku login
$ git push heroku master
*masterは作業してるbranch

## 使用言語、ライブラリ等
- python3
- Flask==1.1.2
- future==0.18.2
- gunicorn==20.0.4
- line-bot-sdk==1.16.0
- requests==2.23.0
*いい感じでインストール。
*pythonさえ入れば、それ以下はpip installでいけます。