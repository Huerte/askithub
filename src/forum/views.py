from django.shortcuts import render
from django.contrib import messages

def homepage_view(request):
    messages.success(request, "✅ Operation completed successfully!")
    return render(request, 'home.html')