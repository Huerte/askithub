from django.shortcuts import render


def homepage_view(requests):
    return render(requests, 'forum/home.html')