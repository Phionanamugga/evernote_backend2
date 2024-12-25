from django.test import TestCase
from .models import Note

class NoteModelTest(TestCase):
    def test_create_note(self):
        note = Note.objects.create(title="Test Note", content="This is a test.")
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.content, "This is a test.")
