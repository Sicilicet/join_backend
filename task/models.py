import datetime
from django.db import models
from users.models import CustomUser


class Task(models.Model):
    title = models.CharField(max_length=100)
    descripton = models.TextField()
    category = "models.PositiveSmallIntegerField()"
    assigned_to = models.ManyToManyField(
        CustomUser,
        related_name="todo_users",
        blank=True,
    )
    due_date = models.DateField(default=datetime.date.today)
    priority = "models.PositiveSmallIntegerField()"

    def __str__(self):
        return f"({self.id})  {self.title}"


class Subtask(models.Model):
    todo_item = models.ForeignKey(
        Task, related_name="subtasks", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    def get_subtasks(self):
        return self.subtasks.all()
