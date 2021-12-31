from django.http.request import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .notes_service import NotesService


@api_view(["GET"])
def get_routes(req: HttpRequest):
    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes",
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object",
        },
        {
            "Endpoint": "/notes/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting note",
        },
    ]

    return Response(routes)


@api_view(["GET", "POST"])
def notes_controller(req: HttpRequest):
    notes_service = NotesService()
    if req.method == "GET":
        return notes_service.get_all()


@api_view(["GET", "POST", "PUT", "DELETE"])
def note_controller(req: HttpRequest, id: str):
    notes_service = NotesService()

    if req.method == "GET":
        return notes_service.get_one(id)
    if req.method == "PUT":
        return notes_service.update(req.data, id)
