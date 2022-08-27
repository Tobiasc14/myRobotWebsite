from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# After website urls (robotWebsite\urls) sends here, it looks to see what urls are associated
# with controls. What to do with a given URL is defined in the views page
app_name = 'controls'
urlpatterns = [
    path('', views.controls, name='controls'),
    # path('test/', views.test, name = 'test'),
    path('ready/', views.ready, name = 'ready'),
    path('secret/', views.secret, name = 'secret'),
    path('driving/', views.driving, name = 'driving'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)