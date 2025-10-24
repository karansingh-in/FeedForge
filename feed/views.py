from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'name' : 'karan',
        'title' : 'text 1',
        'content' : 'this is testinggggggggggggggggggggggggggggggggggggggggggggggggggg',
        'source' : 'github'
    },
    {
        'name' : 'kkkkkk',
        'title' : 'text 2',
        'content' : 'this si test 2222222222222222222222222222222222222222222',
        'source' : 'insta'
    }
]

def home(request):
    context = {
        'posts' : post
    }
    return render(request, 'feed/home.html', context) # location should be folder inside the templates directory/html file name

def about(request):
    return render(request, 'feed/about.html')

# Create your views here.
