from django.urls import path
from .views import  CommentAPIDelete, CommentAPIView, LikeAPIDeleteView, LikeAPIView, NewsAPIUpdateView, NewsAPIView

urlpatterns = [
    path('news/', NewsAPIView.as_view()),
    path('news/<int:pk>/', NewsAPIUpdateView.as_view()),
    path('likes/', LikeAPIView.as_view()),
    path('likes/<int:pk>/', LikeAPIDeleteView.as_view()),
    path('comments/', CommentAPIView.as_view()),
    path('comments/<int:pk>/', CommentAPIDelete.as_view()),
]
