from django.shortcuts import render
from django.contrib.auth import get_user_model 
from rest_framework import generics
from .serializers import (
		PizzeriaListSerializer, 
		PizzeriaDetailSerializer, 
		UserSerializer
	)
from .models import Pizzeria
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
# Create your views here.


class PizzeriaListAPIView(generics.ListAPIView):
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaListSerializer

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
	lookup_field = "id"
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaCreateAPIView(generics.CreateAPIView):
	parser_classes = [MultiPartParser]
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	lookup_field = "id"
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaDestroyAPIView(generics.DestroyAPIView):
	lookup_field = "id"
	queryset = Pizzeria.objects.all()

class UserCreateView(generics.CreateAPIView):
	model = get_user_model()
	parser_classes = [MultiPartParser]
	permission_classes = [permissions.AllowAny]
	serializer_class = UserSerializer
		