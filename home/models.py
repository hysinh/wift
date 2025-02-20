from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    Stores a single contact form entry
    """

    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact Form Inquiry from {self.name}"
    
    class Meta:
        verbose_name_plural = 'Messages from Website'