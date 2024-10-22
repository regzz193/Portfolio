from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]


