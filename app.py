from flask import Flask, request, abort
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# Your Channel Access Token
line_bot_api = LineBotApi('jOQBUAHdalhao70TWwvj14FpSkcJF2ejUkuDy1GmrR5tisBXROzLWxD54bhfAEZZOxHyX7JbTknmfCrSxdQ71Wf6lRlvpJf8anGwNSdg08+xpnF1uNvAJ3Rps5fFVw7lkxRQWHp9W3vRbn5KA2ViFwdB04t89/1O/w1cDnyilFU=')
# Your Channel Secret
handler = WebhookHandler('0598b4190ed972a34eac7fdfbe1eef16')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        #TextSendMessage(text=event.message.text))
        TextSendMessage(text="Hello")
    )

if __name__ == "__main__":
    app.run(port=8069)


from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# Your Channel Access Token
line_bot_api = LineBotApi('jOQBUAHdalhao70TWwvj14FpSkcJF2ejUkuDy1GmrR5tisBXROzLWxD54bhfAEZZOxHyX7JbTknmfCrSxdQ71Wf6lRlvpJf8anGwNSdg08+xpnF1uNvAJ3Rps5fFVw7lkxRQWHp9W3vRbn5KA2ViFwdB04t89/1O/w1cDnyilFU=')
# Your Channel Secret
handler = WebhookHandler('0598b4190ed972a34eac7fdfbe1eef16')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        #TextSendMessage(text=event.message.text))
        TextSendMessage(text="Hello")
    )

if __name__ == "__main__":
    app.run(port=8069)

