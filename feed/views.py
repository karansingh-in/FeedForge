from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'name' : 'karan',
        'title' : 'text 1',
        'content' : 'this is testing'
    },
    {
        'name' : 'kkkk',
        'title' : 'text 2',
        'content' : 'this si test 2'
    }
]

def home(request):
    context = {
        'posts' : post
    }
    return render(request, 'feed/home.html', context) # location should be folder inside the templates directory/html file name

def about(request):
    return HttpResponse('<h1>aboutttttttttttttttt pageeeeeeeeeeeeeeeeeeeeee</h1>')

# Create your views here.
