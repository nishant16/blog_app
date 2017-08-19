from rest_framework import generics
from .serializers import BlogSerializer
from blogs.models import Blog, Category

class BlogListAPIView(generics.ListAPIView):
	serializer_class = BlogSerializer
	# queryset = Blog.objects.all()
	def get_queryset(self):
		return Blog.objects.all()

	# return Blog.objects.all()
	# queryset = User.objects.all()
 #    serializer_class = UserSerializer
 #    permission_classes = (IsAdminUser,)
