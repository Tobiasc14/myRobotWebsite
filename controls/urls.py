from django.urls import path
from . import views

# After website urls (robotWebsite\urls) sends here, it looks to see what urls are associated
# with controls. What to do with a given URL is defined in the views page
urlpatterns = [
    path('', views.controls, name='Controls'),
    path('test/', views.test, name = 'test'),
    path('areyouready/', views.areYouReady, name = 'Ready to Go?'),
    path('ready', views.driving, name = 'Driving')
]