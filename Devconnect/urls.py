from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/profile/', include('profiles.urls')),
    path('api/projects/', include('projects.urls')),
]
