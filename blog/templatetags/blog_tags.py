from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()


# 装饰获取最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-create_time")[:num]


# 装饰归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


# 　分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_categories():
    # 计算分类下的文章数，其接受的参数为需要计数的模型名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    # 计算标签云下的文章数，其接受的参数为需要计数的模型名称
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
