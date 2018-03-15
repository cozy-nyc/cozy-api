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
    """
        This view is for API get request for a list of boards.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer
    permission_classes = [AllowAny]

class BoardDetail(RetrieveAPIView):
    """
        This view is for API get request for details of a board.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    permission_classes = [AllowAny]


class BoardCreate(CreateAPIView):
    """
        This view is for API post request to create a board.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Board.objects.all()
    serializer_class = BoardCreateUpdateSerializer
    permission_classes = [IsAdminUser]

class ThreadCreate(CreateAPIView):
    """
        This view is for API post request to create a thread.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadCreateUpdateSerializer
    permission_classes = [AllowAny]


class ThreadDetail(RetrieveAPIView):
    """
        This view is for API get request for details of a thread.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadDetailSerializer
    permission_classes = [AllowAny]


class ThreadList(ListAPIView):
    """
        This view is for API get request for a list of a threads.

        Note:
            "By default, this api call should return a list of threads by given
                board" - Rantahu

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
            filter_backends:
            search_fields:
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadListSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['title']


class PostCreate(CreateAPIView):
    """
        This view is for API post request to create a post.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [AllowAny]

class PostList(ListAPIView):
    """
        This view is for API get request to list posts in a given thread.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]

class PostDetail(RetrieveAPIView):
    """
        This view is for API get request details of posts.

        Attributes:
            queryset:
            serializer_class:
            perrission_classes:
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]
