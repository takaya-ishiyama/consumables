from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import apis

app_name='consumables'
urlpatterns=[
    # path(r'', IndexView.as_view(template_name='src/index.html'), name='index'),
    path('api/', apis.api.as_view(), name = "api")
] 



