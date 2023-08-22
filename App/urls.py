from django.contrib import admin
from django.urls import path, include
from .views import*

app_name = "App"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", add_show, name="addandshow"),
    path("delete/<int:id>", delete_data, name="deletedata"),
    path("update/<int:id>", update_data, name="updatedata")
]
