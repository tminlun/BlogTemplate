from django.db import models
from django.contrib.auth.models import User

#博客分类,次文章的类型
class BlogType(models.Model):
	type_name = models.CharField(max_length=15)

	def __str__(self):
		return self.type_name

#模型(博客)
class Blog(models.Model):
	title = models.CharField(max_length=50)
	blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
	content = models.TextField()
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING) #User关联到用户
	created_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "<Blog :%s>" % self.title

