from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.paginator import Paginator
from  django.db.models.aggregates import Count
from django.conf import settings #每一页的博客数量
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from read_startistics.utils import read_statistics_once_read
from comment.forms import CommentForm
from .models import Blog,BlogType

# Create your views here.

def get_blog_list_common_data(request,blog_all_list):
    # 分页
    paginator = Paginator(blog_all_list, settings.EACK_PAGE_BLOG_NUMBER)  # 每页10篇
    page_num = request.GET.get('page', 1)  # 获取page后面页码（?page={{ page_num }}）,默认显示第一页
    page_of_blogs = paginator.get_page(page_num)  # 页码，解析页码内容
    current_page_num = page_of_blogs.number  # 当前页面
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    # 添加...
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')  # 在第一位添加...
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 添加第一页和最后一页
    if page_range[0] != 1:  # 第一页永远都是 1
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:  # 如果最后一个页码不等于总页数
        page_range.append(paginator.num_pages)

    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")#order="DESC"倒序
    blog_date_dict = {}
    for blog_date in blog_dates:
        date_count = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        blog_date_dict[blog_date] = date_count

    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blogs'] = page_of_blogs.object_list  # 所有的博客
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    context['blog_dates'] = blog_date_dict
    context['blog_types'] = BlogType.objects.annotate(type_count = Count('blog')).filter(type_name__gt=0)
    return context

#博客首页
def blog_list(request):
    blog_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request,blog_all_list)
    return render(request,'blog/blog_list.html',context)

def blog_type(request,blog_type_pk):
    blog_type= get_object_or_404(BlogType,pk = blog_type_pk)
    blog_all_list = Blog.objects.filter(blog_type=blog_type)# 博客找到(筛选)自己的类型
    context = get_blog_list_common_data(request,blog_all_list)
    context['blog_type'] = blog_type
    return render(request,'blog/blog_type.html',context)

def blog_date(request,year,month):
    blog_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)
    context = get_blog_list_common_data(request,blog_all_list)
    context['blog_date'] = "%s年%s月" % (year, month)  # 当前的年月
    return render(request,'blog/blog_date.html',context)

#博客细节,因为每个博客主键不一样，所有要加主键pk来对应自己的pk
def blog_detail(request,blog_pk):
    context = {}
    blog = get_object_or_404(Blog,pk = blog_pk)#获取指定唯一的元素
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog.pk)

    cookie_key = read_statistics_once_read(request, blog)
    context['blog'] = blog
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['user'] = request.user
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type':blog_content_type.model,'object_id':blog.pk})#initial初始化
    response = render(request,'blog/blog_detail.html',context)
    response.set_cookie(cookie_key, 'true') #记得写值（true）
    return response