from django.urls import path
from gponmap.views import GponmapView

app_name = "gponmap"

urlpatterns = [
    path("map/", GponmapView.as_view()),
]
