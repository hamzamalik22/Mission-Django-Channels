from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("websocket connected...", event)
        print("channel Layer...", self.channel_layer)
        print("channel Name...", self.channel_name)
        async_to_sync(self.channel_layer.group_add)("test", self.channel_name)
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        print("Message Received...", event)
        print("mesage :", event["text"])
        print(type(event["text"]))
        async_to_sync(self.channel_layer.group_send)(
            "test", {"type": "chat.message", "message": event["text"]}
        )
        # self.send(
        #     {
        #         "type": "websocket.send",
        #         "text": "This is message from server or app",
        #     }
        # )

    def chat_message(self, event):
        print("Event.. ", event)
        print("Message.. ", event['message'])
        self.send(
            {
                "type": "websocket.send",
                "text": event["message"],
            }
        )

    def websocket_disconnect(self, event):
        print("websocket disconnected...", event)
        print("channel Layer...", self.channel_layer)
        print("channel Name...", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)("test", self.channel_name)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("websocket connected...", event)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print("Message Received...", event)

    async def websocket_disconnect(self, event):
        print("websocket disconnected...", event)
        raise StopConsumer()
