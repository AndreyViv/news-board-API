from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostList(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        author_name = self.request.query_params.get('author_name')

        if author_name:
            queryset = queryset.filter(author_name=author_name)

        return queryset

    def perform_create(self, serializer):
        return serializer.save()


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PostUpvote(PostList):
    def get_queryset(self):
        queryset = Post.objects.all()
        post_id = self.request.query_params.get('post')

        if post_id:
            post = get_object_or_404(queryset, id=post_id)
            post.amount_of_upvotes += 1

            post.save()

        return queryset


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        post = self.request.query_params.get('post')

        if post:
            queryset = queryset.filter(post=post)

        return queryset

    def perform_create(self, serializer):
        return serializer.save()


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
