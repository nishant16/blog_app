from rest_framework import serializers
from blogs.models import Blog,Category

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = '__all__'


