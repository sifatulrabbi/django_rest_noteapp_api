from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer


class NotesService:
    def get_all(self):
        notes = Notes.objects.all()
        data = NotesSerializer(instance=notes, many=True).data

        return Response(data)

    def get_one(self, id: str):
        note = Notes.objects.get(id=id)
        data = NotesSerializer(instance=note, many=False).data

        return Response(data)

    def update(self, data, id: str):
        note = Notes.objects.get(id=id)
        serializer = NotesSerializer(instance=note, many=False, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

    def remove_one(self, id: str):
        return Response(data={"message": "This will remove a note"}, status=200)
