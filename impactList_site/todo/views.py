from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import TodoListForm
from .models import TodoList

# Create your views here.

def index(request):
    items=TodoList.objects.order_by('-date')
    if request.method=='POST':
        form=TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoListForm()
    page={
        'forms':form,
        'list':items,
        'title':'Impact List'
    }
    return render(request, 'todo/index.html', page)
def delete(request,item_id):
    item=TodoList.objects.get(id=item_id)
    item.delete()
    messages.info(request,'Item removed !!!')
    return redirect('todo')