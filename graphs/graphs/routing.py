from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import graphsBuilder.routing

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            graphsBuilder.routing.websocket_urlpatterns
        )
    ),
})
