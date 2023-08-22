from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegistrationForm
from .models import User

# Create your views here.
# Function for Add and Show Records
def add_show(request):
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = RegistrationForm()
    else:
        fm = RegistrationForm()
    student_data = User.objects.all()

    return render(request, "App/addandshow.html", {
        "form": fm, "stu": student_data})
    
# Update Function
def update_data(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        fm = RegistrationForm(request.POST, instance= data)
        if fm.is_valid():
            fm.save()
    else:
        data = User.objects.get(pk=id)
        fm = RegistrationForm(instance= data)
    return render(request, "App/update.html", {
        "form": fm
    })


# Delete Function
def delete_data(request, id):
     if request.method == "POST":
        data = User.objects.get(pk=id)
        data.delete()
        return redirect("App:addandshow")