# paragraph/models.py
from django.db import models

# Define the Paragraph model
class Paragraph(models.Model):
    # Auto-incremented primary key field
    id = models.BigAutoField(primary_key=True)

    # Text content of the paragraph
    content = models.TextField()

    # String representation of the Paragraph object
    def __str__(self):
        return f"Paragraph {self.id}"
