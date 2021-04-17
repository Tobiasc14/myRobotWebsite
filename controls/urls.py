from django.urls import path
from . import views

# After website urls (robotWebsite\urls) sends here, it looks to see what urls are associated
# with controls. What to do with a given URL is defined in the views page
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name = 'test')
]