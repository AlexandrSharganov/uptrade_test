from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('menu_app.urls', namespace='menu_app')),
    path('admin/', admin.site.urls),
]

