from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q, Count
from .serializers import  LikeSerializer,  NewsSerializer,  CommentSerializer
from .models import News, Comments, Likes
from .permissions import NewsPermissions, CommentDeletePermissions, LikePermission


class NewsAPIPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 10000

class NewsAPIView(generics.ListCreateAPIView): 
    queryset = News.objects.annotate(likes=Count("newslike", filter=Q(newslike__liked=True), distinct=True), 
    comments=Count("newscomment", distinct=True))
    serializer_class = NewsSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
    pagination_class = NewsAPIPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class NewsAPIUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset =     queryset = News.objects.annotate(likes=Count("newslike", filter=Q(newslike__liked=True), distinct=True), 
    comments=Count("newscomment", distinct=True))
    serializer_class = NewsSerializer
    permission_classes = (NewsPermissions,)


class LikeAPIView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class LikeAPIDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (LikePermission,)

class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class CommentAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (CommentDeletePermissions,)