from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import Post

def index(request):
    post_list = Post.objects.order_by("pub_date")
    context = {"post_list": post_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "posts/detail.html", {"post": post})