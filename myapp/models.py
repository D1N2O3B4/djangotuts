from django.db import models

# Create your models here.
class Feature:
    title: str
    content: str

class Facts:
    ratings: int
    title: str
    description: str