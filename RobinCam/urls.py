from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'RobinCam'
urlpatterns = [
    path('robincam/', views.robinCam, name='robinCam'),

    # path('test/', views.test, name = 'test'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)