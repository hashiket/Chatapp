from django.urls import path
from . import consumer


websocket_urlpatterns = [
    path('ws/sc/<str:groupname>', consumer.MySyncConsumer.as_asgi()),
    #path('ws/sc/', consumer.MySyncConsumer.as_asgi()),

    #path('ws/ac/', consumer.MyAsyncConsumer.as_asgi()),
]