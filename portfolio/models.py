from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    technologies = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    full_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='about/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    certificate_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='certifications/', blank=True)
    def __str__(self):
        return self.title


class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.institution} - {self.degree}"

