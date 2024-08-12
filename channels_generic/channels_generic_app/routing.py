from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/first_route_wsc/<str:name_of_group>/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/first_route_awsc/', consumers.MyAsyncConsumer.as_asgi()),
]


