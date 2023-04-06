from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    chef_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="recipe")
    recipe_type = models.CharField(max_length=10,choices = [
        ('veg','veg'),
        ('nonveg','non-veg')
    ]   )

    def __str__(self) -> str:
        return self.name