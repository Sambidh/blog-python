from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Category, Post

# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    print(posts)

    cats = Category.objects.all()


    data = {
        'posts' : posts,
        'cats' : cats
    }
    return render(request, 'home.html', data)

def post(request,url):
    post = Post.objects.get(url=url)
    #print(post)
    cats = Category.objects.all()
    
    return render(request,'posts.html',{'post' : post,'cats' : cats})

def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    cats = Category.objects.all()
    return render(request,'category.html',{'cat':cat, 'posts':posts, 'cats': cats})

def about(request):
    # print("hi")
    return render(request, 'about.html')