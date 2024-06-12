from django.shortcuts import render, redirect
from .forms import DogForm
from .models import Dog


def home(request):
    dogs = Dog.objects.all()
    return render(request, 'main/home.html', {'dogs': dogs})


from django.shortcuts import render, redirect
from .forms import DogForm

def add_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # Перенаправляем на ту же страницу после сохранения
    else:
        form = DogForm()
    return render(request, 'main/add_dog.html', {'form': form})