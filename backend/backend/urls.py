from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your app routes here if needed
    # path('api/', include('your_app_name.urls')),
]
