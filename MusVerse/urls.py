from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls, name='admin_site'),
    path("", include('new_app.urls'))
]
