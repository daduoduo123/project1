from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        #　用户提交的数据存在request.post中，这是一个类字典对象
        # 我们利用这些数据构造了CommentForm的实例，这样Django的表单就生成了
        form = CommentForm(request.POST)
        #　检查数据是否合法
        if form.is_valid():
            # commit=false的作用是仅仅利用表单的数据生成comment模型类的实例，但不保存到数据库中
            comment = form.save(commit=False)
            # 江评论和文章关联起来
            comment.post = post
            # 保存到数据库中
            comment.save()
            return redirect(post)

        else:
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html', context=context)
    # 不是post请求直接重定向到详情页面
    return redirect(post)
