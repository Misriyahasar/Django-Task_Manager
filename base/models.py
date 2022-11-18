from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    STATUS_CHOICE=(
        ('1','Open'),
        ('2','In-Progress'),
        ('3','Closed')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=20,choices=STATUS_CHOICE,default='1')
    assignee = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='assigned_tasks')
    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
