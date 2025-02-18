from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = "BookHub"

urlpatterns = [
    path('', views.main, name="BookHub"),
    path('bookmain', views.book, name="bookmain"),
    path("check_days", views.check_days, name="check_days"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
