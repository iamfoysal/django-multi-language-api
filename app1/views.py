from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
