from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages

# import todo froms and models
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    item_list=Todo.objects.order_by("-date")
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    form = TodoForm()

    page ={
        "forms":form,
        "list": item_list,
        "title":"TODO LIST",
    }
    return render(request, 'index.html', page)

def remove(request, item_id):
    item= Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"item removed!!")
    return redirect('base')