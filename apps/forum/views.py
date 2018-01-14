from django.shortcuts import render

from rest_framework.filters import(
    SearchFilter,
    OrderingFilter
)

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from .serializers import *


class BoardList(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer
    permission_classes = [AllowAny]

class BoardDetail(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    permission_classes = [AllowAny]



class ThreadCreate(CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadCreateUpdateSerializer
    permission_classes = [AllowAny]


class ThreadDetail(RetrieveAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadDetailSerializer
    permission_classes = [AllowAny]


class ThreadList(ListAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadListSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['content', 'title']





class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [AllowAny]

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]

class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]
