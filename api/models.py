from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_used = models.CharField(max_length=200, help_text="Python, Django, React nu comma potu eludhu")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"