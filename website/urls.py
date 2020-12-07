from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="home"),
    # path('privacy-policy.html', views.privacy, name="privacy"),
   
]
#THIS PATH IS IMPORTANT TO RENDER OUR IMG IN OUR ADMIN
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
