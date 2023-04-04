from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

from fbot_app.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt

def callback(request):
    if request.method == 'POST':
        #先設定一個要回傳的message空集合
        message=[]
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        
        #在這裡將body寫入機器人回傳的訊息中，可以更容易看出你收到的webhook長怎樣#
        #message.append(TextSendMessage(text=str(body)))

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            #如果事件為訊息
            if isinstance(event, MessageEvent):
                #print(event.message.type)
                if event.message.type=='text':
                    # message.append(TextSendMessage(text='文字訊息'))

                    myContent = 'Hello Postgres'  # 回覆使用者的內容

                    print(event.message.text)
                                 
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=myContent))
                    #上面这个是正式的
     
        return HttpResponse()

    else:
        return HttpResponseBadRequest()