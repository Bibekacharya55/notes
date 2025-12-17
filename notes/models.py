from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    file = models.FileField(upload_to="notes_files", null=True, blank=True)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
