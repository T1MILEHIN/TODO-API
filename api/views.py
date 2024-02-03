from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class CREATE_TODO(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer

class VIEW_API(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class SINGLE_TODO(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UPDATE_TODO(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DELETE_TODO(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
