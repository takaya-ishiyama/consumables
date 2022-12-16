from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name='consumables'
urlpatterns=[
    path(r'', views.item_list),
    path(r'<int:pk>/', views.item_detail),
    # path('api/', apis.api.as_view(), name = "api")
] 



