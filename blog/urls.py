from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='index'), # 初始界面
    url(r'^$', views.IndexView.as_view(), name='index'),

    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'), #文章详情页面
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'), #文章详情页面

    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'), # 归档界面
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'), # 归档界面

    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'), # 分类界面
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'), # 分类界面

    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'), # 标签云界面

    # url(r'^search/$', views.search, name='search') # 自己写的额搜索
]