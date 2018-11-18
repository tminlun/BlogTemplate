from django.urls import path
from . import views

urlpatterns = [
	#http://127.0.0.1:8000/blog博客首页
	path('',views.blog_list, name="blog_list"),
    path('<int:blog_pk>',views.blog_detail, name = 'blog_detail'),
    path('type/<int:blog_with_type_pk>',views.blogs_with_type,name="blogs_with_type"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),

]