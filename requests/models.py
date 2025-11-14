from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(unique=True)

    def __str__(self):
        return f'({self.id}) {self.title}'

class Feedback(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.user.username}, {self.created_at}) {self.course.title}'

class Request(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROGRESS = 'PROGRESS', 'Progress'
        COMPLETED = 'COMPLETED', 'Completed'
    
    class Payment(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CARD = 'CARD', 'Card'

    # contact = models.ForeignKey("Contact", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(choices=Status, default=Status.PENDING)
    payment = models.CharField(choices=Payment)
    prefered_start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.created_at}) {self.course.title} {self.prefered_start_date}'

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField()
    first_name = models.CharField()
    middle_name = models.CharField()
    last_name = models.CharField()