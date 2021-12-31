from django.urls import path
from . import controllers


urlpatterns = [
    path("", controllers.get_routes, name="routes"),
    path("notes/", controllers.notes_controller, name="notes"),
    path("notes/<str:id>/", controllers.note_controller, name="note"),
]
