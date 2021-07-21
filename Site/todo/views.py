import django
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import request




class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    
    priority = forms.IntegerField(label="Priority",min_value=1 ,max_value=3)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "index.html",{
        "tasks" : request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "add.html",{
                "form": form
            })
    return render(request, "add.html",{
        "form": NewTaskForm()
    })