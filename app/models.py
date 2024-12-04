from django.db import models
class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)  # Full name
    profession = models.CharField(max_length=100)  # Job title or profession
    bio = models.TextField()  # Short biography
    skills = models.TextField()  # Comma-separated skills
    experience = models.TextField()  # Detailed experience
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Optional profile picture

    def __str__(self):
        return self.name


