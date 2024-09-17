from django.contrib import admin
from django.urls import path
from task.views import TaskItemView, SubtaskView
from users.views import (
    LoginView,
    RegisterUserView,
    LogoutView,
    CustomUserView,
    GuestLoginView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("todos/", TaskItemView.as_view()),
    path("todos/<int:pk>/", TaskItemView.as_view()),
    path("todos/<int:pk>/delete/", TaskItemView.as_view()),
    path("subtasks/", SubtaskView.as_view()),
    path("subtasks/<int:pk>/", SubtaskView.as_view()),
    path("subtasks/<int:pk>/delete/", SubtaskView.as_view()),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("users/", CustomUserView.as_view()),
    path("users/<int:pk>/", CustomUserView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", CustomUserView.as_view(), name="delete_user"),
    path("guest/", GuestLoginView.as_view()),
]
