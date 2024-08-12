from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import *


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        # print("websocket connected...", event)
        # print("channel Layer...", self.channel_layer)
        # print("channel Name...", self.channel_name)
        self.group_name = self.scope["url_route"]["kwargs"]["name_of_group"]
        print(self.group_name)

        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Message Received...", text_data)
        data = json.loads(text_data)
        # message = data["msg"]
        # user_name = data["username"]
        # print("Username : ", user_name)

        group = Group.objects.get(name=self.group_name)
        chat = Chat(content=data["msg"], group=group)
        chat.save()
        # print("mesage :", event["text"])
        # print(type(event["text"]))
        async_to_sync(self.channel_layer.group_send)(
            # self.group_name, {"type": "chat.message", "message": message}
            self.group_name, {"type": "chat.message", "data": data}
        )

    def chat_message(self, event):
        print("Event.. ", event)
        # print("Message.. ", event['message'])
        self.send(text_data=json.dumps({"msg": event['data']}))

    def disconnect(self, close_code):
        print("websocket disconnected...", close_code)
        # print("channel Layer...", self.channel_layer)
        # print("channel Name...", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        raise StopConsumer()


class MyAsyncConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):
        print("websocket connected...", event)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print("Message Received...", event)

    async def websocket_disconnect(self, event):
        print("websocket disconnected...", event)
        raise StopConsumer()
