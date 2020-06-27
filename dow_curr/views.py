from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

import os
# Create your views here.


def form_for_curr(request):
    if request.method == "POST":
        form = forms.Curr(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            return redirect(dowload_curr_file, date=date)

    else:
        form = forms.Curr()
        return render(request, 'form_curr.html', {'form':form})

def dowload_curr_file(request, date):
    file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tmp', '1.jpg')

    with open(file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file)
            return response
    
