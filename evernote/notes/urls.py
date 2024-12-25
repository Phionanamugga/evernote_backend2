from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.get_notes, name='get_notes'),  # List all notes
    path('notes/create/', views.create_note, name='create_note'),  # Create a note
    path('notes/<int:note_id>/update/', views.update_note, name='update_note'),  # Update a note
    path('notes/<int:note_id>/delete/', views.delete_note, name='delete_note'),  # Delete a note
]
