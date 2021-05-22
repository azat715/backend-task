from django.urls import path

from core.views import ClientList

app_name = "core"

urlpatterns = [
    path("", ClientList.as_view(), name="clients"),
]
