from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('movie.urls'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
