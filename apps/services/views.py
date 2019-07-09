from django.shortcuts import render

from rest_framework.filters import(
    SearchFilter,
    OrderingFilter
)

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

from rest_framework.generics import(
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.views import APIView
from rest_framework import status


from .permissions import IsOwnerOrReadOnly


from rest_framework.authtoken.models import Token
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

from .serializers import *



class ServiceList(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = [AllowAny]

class ServiceDetailSerializer(RetrieveAPIView):
    queryset = Service.object.all()
    serializer_class = ServiceDetailSerializer
    permission_classes = [AllowAny]
    search_fields = ('service')
