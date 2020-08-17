from django.urls import path

from .views import PostList, PostDetail, CommentList, CommentDetail, PostUpvote


app_name = 'articles'

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('upvote/', PostUpvote.as_view()),
]
