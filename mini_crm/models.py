from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Note(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:20] + '...' if len(self.content) > 20 else self.content[0:20] + '...' if len(self.content) > 0 else 'No content'  # Handle empty notes for better readability.

class Reminder(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='reminders')
    message = models.CharField(max_length=255)
    reminder_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message