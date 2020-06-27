from django.shortcuts import render
from . import forms
# Create your views here.

def add_post(request):
    if request.method == "POST":
        form = forms.AddPost(request.POST)
        if form.is_valid():
            form.save()
        return 

    else:
        form = forms.AddPost()
        return render(request, 'forum_add.html', {"form":form})
