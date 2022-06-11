from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
User = get_user_model()


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='project_image', null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    technologies = models.TextField()



    def __str__(self):
        return self.title


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    design_rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    content_rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    usability_rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])

    def __str__(self):
        return self.project.title

    def user_avg(self):
        avg = self.design_rating + self.content_rating + self.usability_rating
        total_avg = avg // 3
        return total_avg