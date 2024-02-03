from django.urls import path
from . views import VIEW_API, SINGLE_TODO, CREATE_TODO, UPDATE_TODO, DELETE_TODO

urlpatterns = [
    path("", VIEW_API.as_view(), name="view-all"),
    path("create/", CREATE_TODO.as_view(), name="create"),
    path("<int:pk>/", SINGLE_TODO.as_view(), name="single-todo"),
    path("update/<int:pk>/", UPDATE_TODO.as_view(), name="update"),
    path("delete/<int:pk>/", DELETE_TODO.as_view(), name="delete")
]