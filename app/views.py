import imp
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from app.forms import BookForm, UserRegistrationForm
from app.models import Book


def showbooks(request):
    data=Book.objects.all()
    print(data)
    return render(request,'adminshow.html',{'data':data})

def delete(request,id):
    data=Book.objects.get(id=id)
    data.delete()
    return redirect('/adminshow')

@login_required()
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, 'Book added to database')

            except:
                pass
    form = BookForm()
    return render(request, 'addbook.html', {'form': form})
@login_required()
def edit(request,id):
    data=Book.objects.get(id=id)
    return render(request,'edit.html',{"data":data})

@login_required()
def update(request, id):
    data = Book.objects.get(id=id)
    print(data)
    if request.method=='POST':
        form = BookForm(request.POST, instance=data)
        if form.is_valid:
            try:
                form.save()
            except:
                pass
    form=BookForm()
    return redirect('/adminshow')

def UserRegistration(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('/login')
    else:
        form=UserRegistrationForm()
    return render(request,'signup.html',{"form":form})

def home(request):
    return render(request,'home.html')

def studentview(request):
    data=Book.objects.all()
    return render(request,'studentview.html',{'data':data})
@login_required()
def select(request):
    return render(request,'select.html')