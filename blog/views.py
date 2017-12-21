from django.shortcuts import render
from .models import Posts
from django.utils import timezone


def post_list(request):
    posts = Posts.objects.filter(published_date__lte= timezone.now())
    return render(request, 'blog/post_list.html', {'posts':posts})