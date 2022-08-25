from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ProjectNavigator'
urlpatterns = [
    path('', views.projectNavigator, name='projectNavigator'),
    #path('controls/', views.controls, name='controls'),


    # path('test/', views.test, name = 'test'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)