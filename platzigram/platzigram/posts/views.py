from django.shortcuts import render

from django.http import HttpResponse

# List Existing Post
def list_posts(request):
    posts = [1, 2, 4, 10]
    return HttpResponse(str(posts))
    pass