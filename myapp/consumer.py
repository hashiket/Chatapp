from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync
import json
from .models import Group,Chat,Message
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket Connected...', event)
        print('Channel Layer...', self.channel_layer)
        # print(self.scope['url_route']['kwargs']['groupkaname'])

        self.group_name  = self.scope['url_route']['kwargs']['groupname']
        # print(1)
        print(self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.send({
             'type':'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Messaged Received...", event)
        print("Message is", event['text'])
        messages = Message.objects.all()
        for message in messages:
            self.send({
                  'type':'websocket.send',
                  'text': message.message
              })



       
        group = Chat.objects.get(name= self.group_name)
        chat = Message(message = event['text'], chat=group)
        chat.save()
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
             'type': 'chat.message',
             'message': event['text']
         })

    def chat_message(self, event):
         print("Event....", event)
         print('Actual Data...', type(event['message']))
         print('Type of Actual Dta...', type(event['message']))
         self.send({
             'type': 'websocket.send',
             'text': event['message']
         })


    def websocket_disconnect(self, event):
        print('WebScoket Disconnected...', event)
        print('Channel Layer...', self.channel_layer)
        #async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

        raise StopConsumer()


