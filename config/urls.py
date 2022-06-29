from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bookmark/', include('bookmark.urls')),   # bookmark > urls.py 로 위임한다.
    path('admin/', admin.site.urls),
]
