from fbot_app.models import *
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
# from linebot.models import MessageEvent, TextSendMessage,
from linebot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext=event.message.text
                # message=[]
                # message.append(TextSendMessage(text=mtext))
                # line_bot_api.reply_message(event.reply_token,message)

                myContent = ''  # 回覆使用者的內容
                # print(mtext)

                if (mtext.isdigit()):

                    if (int(event.message.text)>=1) and (int(event.message.text)<=325):
                            mySequence = int(event.message.text)

                            #print(mySequence)

                            # 篩選 poem 資料表
                            selectedPoem = poempoem.objects.filter(poemid=mySequence).first()

                            #print('--------------------------')
                            #print(selectedPoem.poemen)
                            #print(selectedPoem.all)
                            #myContent = "Poem"

                            # print (selectedPoem.poemen.splitlines())
                            # print('--------------------------')

                            enStr = selectedPoem.poemen1

                            if len(selectedPoem.poemen2) >= 1:
                                enStr = enStr + '\n\n' + selectedPoem.poemen2
                            if len(selectedPoem.poemen3) >= 1:
                                enStr = enStr + '\n\n' + selectedPoem.poemen3
                            if len(selectedPoem.poemen4) >= 1:
                                enStr = enStr + '\n\n' + selectedPoem.poemen4

                            cnStr = selectedPoem.poemcn1

                            if len(selectedPoem.poemcn2) >= 1:
                                cnStr = cnStr + '\n\n' + selectedPoem.poemcn2
                            if len(selectedPoem.poemcn3) >= 1:
                                cnStr = cnStr + '\n\n' + selectedPoem.poemcn3
                            if len(selectedPoem.poemcn4) >= 1:
                                cnStr = cnStr + '\n\n' + selectedPoem.poemcn4

                            myContent += 'Stray Birds 飛鳥集' + '\n' +  mtext + '\n\n' + enStr + '\n\n' + cnStr

                    else:
                        myContent = "Poem from 1 to 325, please try again..."
                else:
                    myContent = "Poem from 1 to 325, please try again..."

                # {
                #     "type": "image",
                #     "originalContentUrl": "https://example.com/original.jpg",
                #     "previewImageUrl": "https://example.com/preview.jpg"
                # }


                imgUrl = "https://straybirds.herokuapp.com/media/a.jpg"
                imgPreUrl = "https://straybirds.herokuapp.com/media/a.jpg"

                message01 = TextSendMessage(text=myContent)
                message02 = ImageSendMessage(original_content_url=imgUrl, preview_image_url=imgPreUrl)

                # line_bot_api.reply_message(event.reply_token, [message02,message01])
                line_bot_api.reply_message(event.reply_token, [message01])


        return HttpResponse()
    else:
        return HttpResponseBadRequest()