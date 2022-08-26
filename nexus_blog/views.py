from .forms import CommentForm, ReplyForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from nexus_blog.forms import CommentForm
from .models import Blog, Comment, Reply
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def PostList(request):
    object_list = Blog.objects.filter(status=1).order_by('-publish_date')
    paginator = Paginator(object_list, 2)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    context = {
        'page': page,
        'post_list': post_list
    }
    return render(request, 'blogs/blog.html', context)


def PostDetail(request, slug):
    post = Blog.objects.filter(slug=slug).first()

    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'blogs/post_detail.html', context)


def reply(request, post_id, comment_id):
    post = get_object_or_404(Blog, id=post_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            comment = get_object_or_404(Comment, id=comment_id)
            new_comment=Reply.objects.create(
                comment=comment,
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                phoneno=form.cleaned_data.get('phoneno'),
                message=form.cleaned_data.get('message') )
            new_comment.save()
    return redirect('post_detail', slug=post.slug)


# # class PostList(generic.ListView):
# #     queryset = Post.objects.filter(status=1).order_by('-publish_date')
# #     template_name = 'blogs/blog.html'
# #     paginate_by = 6

# # class PostDetail(generic.DetailView):
# #     model = Post
# #     template_name = 'blogs/post_detail.html'

