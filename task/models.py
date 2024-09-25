import datetime
from django.db import models
from users.models import CustomUser


class Task(models.Model):
    priority_choices = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("urgent", "Urgent"),
    ]
    status_choices = [
        ("todo", "To do"),
        ("progress", "In progress"),
        ("feedback", "Await feedback"),
        ("done", "Done"),
    ]
    category_choices = [("userstory", "User Story"), ("technical", "Technical Task")]
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=50, choices=priority_choices, default="low")
    users = models.ManyToManyField(CustomUser, related_name="task_users", blank=True)
    category = models.CharField(
        max_length=20, choices=category_choices, default="userstory"
    )
    status = models.CharField(max_length=20, choices=status_choices, default="task")

    def get_subtasks(self):
        return self.subtasks.all()

    def __str__(self):
        return f"({self.id}, {self.status}) {self.title}"


class Subtask(models.Model):
    task_item = models.ForeignKey(
        Task, related_name="subtasks", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"
