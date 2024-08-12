# master_channels/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import channels_app.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'master_channels.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket" : URLRouter(
        channels_app.routing.websocket_urlpatterns
    )
})
    