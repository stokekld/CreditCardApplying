from django.conf.urls import url
from .views import UsuarioViews, UsuarioAuth

# views = UsuarioViews()
# authObject = UsuarioAuth()

urlpatterns = [
    url(r'^$', UsuarioViews.as_view(), name='usuarios'),
    url(r'^/auth$', UsuarioAuth.as_view(), name='auth'),
]

