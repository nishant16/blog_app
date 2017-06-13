from django.shortcuts import render, get_object_or_404

from .models import Category, Blog
from django.core.exceptions import ObjectDoesNotExist
import datetime




def index(request):
    context = {'categories':Category.objects.all(),'posts':Blog.objects.all()} 
    return render(request,'blogs/index.html',context)


def view_post(request, id):
    post = get_object_or_404(Blog , pk= id)
    return render(request,'blogs/view_post.html',{'posts': post})


def view_category(request, id):
    category = get_object_or_404(Category, pk= id)
    return render(request,'blogs/view_category.html',{'category':category,'posts':Blog.objects.filter(category=category)})
    

def create(request):
    
    if request.method == 'POST':
        blog_title= request.POST['title']
        blog_content=request.POST['Content']
        
        if (len(blog_title) <=40 or len(blog_title) >=120):
            msg='enter char. between 40 to 120'
            return render(request,'blogs/create_blog.html',{'msg':msg})
    
        try:
            category = Category.objects.get(title=str(request.POST['category']))
        except ObjectDoesNotExist as exc:
            qs='category doesnot exist'
            return render(request,'blogs/create_blog.html',{'q':qs})
        
        q=Blog.objects.create(title=blog_title, category=category,Content= blog_content, posted=datetime.date.today())
        if (blog_title =='' or blog_content == '' or blog_title.isspace() or blog_content.isspace()):
            qt='enter the the details'
            return render(request,'blogs/create_blog.html',{'qt':qt})
        else:
            return render(request, 'blogs/create_blog.html',{'q':q})
    else:
        return render(request,'blogs/create_blog.html')


def edit(request):
    category=Category.objects.all()
    blog=Blog.objects.all()
    return render(request,'blogs/edit_blog.html',{'category':category,'blog':blog})


def edit_blog_category(request, id):
    
    if request.method =='POST':
        blog_title= request.POST['title']
        blog_content=request.POST['Content']
        blog_update= Blog.objects.filter(title= blog_title).update(Content= blog_content)
        return render(request,'blogs/edit_blog_category.html',{'blog_update':blog_update})

    else:
        blog= get_object_or_404(Blog, pk=id)
        return render(request,'blogs/edit_blog_category.html',{'blog':blog})





