from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class MyUser(AbstractUser):
  # user = models.CharField(max_length=100, blank=True, null=True)
  # REQUIRED_FIELDS = ['user']
  pass


class Ticket(models.Model):

  NEW = 'NEW'
  IN_PROGRESS = 'IN PROGRESS'
  DONE = 'DONE'
  INVALID = 'INVALID'
  TICKET_STATUS_LABELS = [
    (NEW, 'New'),
    (IN_PROGRESS, 'In Progress'),
    (DONE, 'Done'),
    (INVALID, 'Invalid'),
  ]
  title = models.CharField(max_length=100)
  date_time = models.DateTimeField(default=timezone.now)
  description = models.TextField()
  filed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

  current_ticket_process = models.CharField(
    max_length=20,
    default="NEW",
    choices=TICKET_STATUS_LABELS,
  )
  assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='assigned_user', null=True, blank=True)
  completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='completed_user', null=True, blank=True)

  def __str__(self):
      return self.title
  
