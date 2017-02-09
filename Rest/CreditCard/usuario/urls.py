from django.conf.urls import url
from .views import UsuarioViews

# views = UsuarioViews()

urlpatterns = [
    url(r'^$', UsuarioViews.as_view(), name='inicio'),
]

