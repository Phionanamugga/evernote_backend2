from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)  # Title of the note
    content = models.TextField()  # Main content of the note
    created_at = models.DateTimeField(auto_now_add=True)  # Auto set when note is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto set when note is updated

    def __str__(self):
        return self.title
        