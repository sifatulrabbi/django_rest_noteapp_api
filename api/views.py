from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import NotesSerializer


@api_view(["GET"])
def get_routes(req):
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


@api_view(["GET"])
def get_notes(req: request):
    notes = Notes.objects.all()
    data = NotesSerializer(instance=notes, many=True).data

    return Response(data)


@api_view(["GET"])
def get_note(req: request, id: str):
    note = Notes.objects.get(id=id)
    data = NotesSerializer(instance=note, many=False).data

    return Response(data)


# @api_view(["POST"])
# def get_note(req: request):

#     return Response("Data")
