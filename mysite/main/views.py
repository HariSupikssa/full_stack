from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.contrib.auth import logout, authenticate
from django.contrib import messages

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if(response.method == "POST"):
            # print(response.POST)
            if(response.POST.get("save")):
                for item in ls.item_set.all():
                    if(response.POST.get("c"+str(item.id))=="clicked"):
                        item.complete= True
                    else:
                        item.complete = False
                    item.save()
                
            elif(response.POST.get("newItem")):
                txt = response.POST.get("new")
                
                if(len(txt)>2):
                    ls.item_set.create(text=txt,complete=False)
                else:
                    print("Invalid")
        return render(response,"main/list.html",{"ls":ls})
    return render(response,"main/viewlist.html",{})

def home(request):
    if(request.POST.get("logout")):
        logout(request)
        messages.success(request,("You are logged out"))
    # return redirect("/home")
    return render(request,"main/home.html",{})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if(form.is_valid()):
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            # response.user.todolist_set.create(name = n)
            response.user.todolist.add(t)
            return HttpResponseRedirect("/%i" %t.id)
            
    else:
        form = CreateNewList()
    return render(response,"main/create.html",{"form":form})

def listall(response):
    # ls = ToDoList.objects.all()
    # return render(response,"main/viewlist.html",{"ls":ls})
    return render(response, "main/viewlist.html", {})