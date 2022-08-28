from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'RobinCam'
urlpatterns = [
    path('', views.robinCam, name='robinCam'),

    # path('test/', views.test, name = 'test'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)