from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Note
import json

@csrf_exempt
def create_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        note = Note.objects.create(title=data['title'], content=data['content'])
        return JsonResponse({'id': note.id, 'title': note.title, 'content': note.content}, status=201)

@csrf_exempt
def get_notes(request):
    if request.method == 'GET':
        notes = Note.objects.all().values('id', 'title', 'content', 'created_at', 'updated_at')
        return JsonResponse(list(notes), safe=False, status=200)

@csrf_exempt
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        note.title = data.get('title', note.title)
        note.content = data.get('content', note.content)
        note.save()
        return JsonResponse({'id': note.id, 'title': note.title, 'content': note.content}, status=200)

@csrf_exempt
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'DELETE':
        note.delete()
        return JsonResponse({'message': 'Note deleted successfully'}, status=204)
