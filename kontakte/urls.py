from django.urls import path
from .views import *

urlpatterns = [
    path("<path:path>", contact_main),
    path("", contact_main),
]
