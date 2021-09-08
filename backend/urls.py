from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('database.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/jwtauth/', include('jwtauth.urls'), name='jwtauth'), # new
]