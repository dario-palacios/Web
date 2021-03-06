from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Post, Category

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category': category})

