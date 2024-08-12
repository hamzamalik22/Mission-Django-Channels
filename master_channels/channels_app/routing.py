from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/first_route_sy/<str:name_of_group>/', consumers.MySyncConsumer.as_asgi()),
    path('ws/first_route_asy/', consumers.MyAsyncConsumer.as_asgi()),
]


