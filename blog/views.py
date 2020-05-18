from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Author, Tag
from . forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by("-date")
    paginator = Paginator(latest_posts, 8)
    page = request.GET.get("page")
    latest_posts = paginator.get_page(page)
    return render(request, "blog/index.html", {"posts": latest_posts})

def about_page(request):
    return render(request, "blog/about.html")

def single_post(request, slug):
    single_post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
    
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = single_post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail', args=[slug]))
    return render(request, "blog/detail.html", {
        "post": single_post,
        "all_tags": single_post.tags.all(),
        "form": CommentForm(),
        "comments":single_post.comments.all().order_by("-id")
    })
 
    