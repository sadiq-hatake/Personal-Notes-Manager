from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass')
        Note.objects.create(title="Test Note", content="Some content", user=self.user)

    def test_note_content(self):
        note = Note.objects.get(title="Test Note")
        self.assertEqual(note.content, "Some content")
        
def test_user_specific_notes(self):
    other_user = User.objects.create_user(username='other', password='pass')
    Note.objects.create(title="Other Note", content="Other content", user=other_user)
    notes = Note.objects.filter(user=self.user)
    self.assertEqual(notes.count(), 1)

