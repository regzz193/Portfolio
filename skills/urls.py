from skills import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'skills'
urlpatterns = [
    path('', views.skills, name='skills'),
    path('<int:category_id>', views.skills_recipe, name='skills_recipe'),
]

urlpatterns += staticfiles_urlpatterns()