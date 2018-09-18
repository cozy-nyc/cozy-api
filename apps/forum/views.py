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
            queryset: Query holding all of the Board objects.
            serializer_class: Using the Board List Serializer
            permission_classes: Anyone is allowed to access this call (even
            users who have not signed up)
    """
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer
    permission_classes = [AllowAny]


class BoardDetail(RetrieveAPIView):
    """
        This view is for API get request for details of a board.

        Attributes:
            queryset: Query holding all of the Board objects
            serializer_class: Using the Board Detail Serializer for more detailed
            information
            permission_classes: Anyone is allowed to access this call (even
            users who have not signed up)
    """
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    permission_classes = [AllowAny]


class BoardCreate(CreateAPIView):
    """
        This view is for API post request to create a board.

        Attributes:
            queryset: Query holds all of the Board Objects
            serializer_class: Using the Board Create Update Serializer in order
            to create and update specific information
            permission_classes: Only admin users are allowed to create and make
            edits to existing boards.
    """
    queryset = Board.objects.all()
    serializer_class = BoardCreateUpdateSerializer
    permission_classes = [IsAdminUser]

class ThreadCreate(CreateAPIView):
    """
        This view is for API post request to create a thread.

        Attributes:
            queryset: Query holds all of the Thread Objects
            serializer_class: The Thread create serializer is used so users can
            create thread.
            permission_classes: Only authenticated users are allowed to create
            threads.
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class ThreadDetail(RetrieveAPIView):
    """
        This view is for API get request for details of a thread.

        Attributes:
            queryset: Query holds all of the Thread Detail
            serializer_class: The Thread deteail serializer is used.
            permission_classes: Anyone is allowed to call ThreadDetails even
            those who are not authenticated users
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
            queryset: Query that holds all Threads in the order based off their
            latestReplyTime
            serializer_class: The ThreadListSerializer is used
            permission_classes: anyone is allowed to call ThreadList even those
            who are not authenticated users
            search_fields: Allow searched to be based off the following fields
                title,
                poster,
                board
            ordering_fields: Allow search query to be ordered in reverse latestReplyTime
    """
    queryset = Thread.objects.all().order_by('-latestReplyTime')
    serializer_class = ThreadListSerializer
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title', 'poster__user__username', 'board__name']
    ordering_fields = ('latestReplyTime',)




class PostCreate(CreateAPIView):
    """
        This view is for API post request to create a post.

        Attributes:
            queryset: Query that holds all of the Post objects
            serializer_class: the PostCreateUpdateSerializer is used
            permission_classes: Authenticated users are allowed to create Posts
    """
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class PostList(ListAPIView):
    """
        This view is for API get request to list posts in a given thread.

        Attributes:
            queryset: Query that holds all of the post Objects in order of their
            creation
            serializer_class: The PostListSerializer is used
            permission_classes: Anyone is allowed to access PostList even unathenticated
            users
            search_field: Allow search query to be filtered through the following fields:
                message,
                poster
    """
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter,)
    search_fields = ['message', 'poster__user__username']


class PostDetail(RetrieveAPIView):
    """
        This view is for API get request details of posts.

        Attributes:
            queryset: Query that holds all of the Post objects
            serializer_class: The PostDetailSerializer is used
            permission_classes: Anyone is allowed to access Post details even
            unathenticated users
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]
