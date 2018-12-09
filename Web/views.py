# -*- coding: utf-8 -*-

from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from Utils.db_connections import get_redis

channel_layer = get_channel_layer()

# class MyConsumer(WebsocketConsumer):
#
#     def connect(self):
#         self.username = "Anonymous"
#         self.accept()
#         # __import__("pdb").set_trace()
#         # async_to_sync(channel_layer.send)(self.channel_name, {"type": "chat.force_disconnect", "text": "123"})
#         # self.send(text_data="[Welcome %s!]" % self.username)
#         channel_layer.send(self.channel_name, {"type": "chat.message", "text": "Hello there!"})
#
#     def receive(self, *, text_data):
#         # if text_data.startswith("/name"):
#         #     self.username = text_data[5:].strip()
#         #     self.send(text_data="[set your username to %s]" % self.username)
#         # else:
#         #     self.send(text_data=self.username + ": " + text_data)
#         pass
#
#     def disconnect(self, message):
#         pass


# 自定义websocket处理类
class MyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # 创建连接时调用
        await self.accept()
        # await self.send(text_data="Hello world!")
        import time
        from asgiref.sync import async_to_sync
        channel_layer = get_channel_layer()
        username = self.scope['user'].username
        redis = get_redis()
        redis.set("sock" + username, self.channel_name)
        # __import__("pdb").set_trace()
        # await channel_layer.send(c_name, {"type": "send.message", "text": "Hello there!"})
        # time.sleep(5)
        # await channel_layer.send(self.channel_name, {"type": "chat.message", "text": "Hello there!"})
        # time.sleep(5)
        # await channel_layer.send(self.channel_name, {"type": "chat.message", "text": "Hello there!"})
        # time.sleep(5)
        # await channel_layer.send(self.channel_name, {"type": "chat.message", "text": "Hello there!"})
        # data = {"type": "chat.message", "text": "Hello there!"}
        from asgiref.sync import async_to_sync
        # await channel_layer.send(self.channel_name, {"type": "chat.force_disconnect", "text": "23"})
        # await channel_layer.send(self.channel_name, data)
        # 将新的连接加入到群组
        # await self.channel_layer.group_add("chat", self.channel_name)

    async def send_message(self, data):
        print(self.channel_name)
        channel_layer = get_channel_layer()
        await channel_layer.send(self.channel_name, {"type": "chat.message", "text": "Hello there!"})
        # await channel_layer.send(text_data=data)

    async def receive(self, text_data=None, bytes_data=None):
        # 收到信息时调用

        # 信息单发
        # await self.send(text_data="Hello world!")
        # 信息群发
        await self.channel_layer.group_send(
            "chat",
            {
                "type": "chat.message",
                "text": "Hello world!",
            },
        )

    async def disconnect(self, close_code):
        # 连接关闭时调用
        # 将关闭的连接从群组中移除
        # await self.channel_layer.group_discard("chat", self.channel_name)

        await self.close()

    async def chat_message(self, event):
        # Handles the "chat.message" event when it's sent to us.
        await self.send(text_data=event["text"])

