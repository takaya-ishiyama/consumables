from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import apis

app_name='accounts'
urlpatterns=[
    path(r'', views.user_list),
    path(r'<int:pk>/', views.user_detail),

    ]
