from django.shortcuts import render, redirect
from .forms import AdmissionForm
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Admission
   

def add_admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    else:
        form = AdmissionForm()
    return render(request, 'add_admission.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        u_name =request.POST.get('username')
        email = request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1 != pass2:
            return HttpResponse("<h1>Your Password  And Confirm Password Are Not Same !!!</h1>")
        else:
            print("saved")
            my_user=User.objects.create_user(u_name,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request,'signup.html') 

def login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            pass1 = request.POST.get('pass')

            if not User.objects.filter(username=username).exists():
                return HttpResponse("<h1>User does not exist</h1>")

            my_user = authenticate(request, username=username, password=pass1)
            if my_user.is_active:
                login(request, my_user)
                return redirect('addmission')
            else:
                return HttpResponse("<h1>Invalid username or password</h1>")

        
        return render(request, 'login.html')
  
def admissions_list(request):
    if not request.my_user.is_authenticated:
        return redirect('login')
    admissions = Admission.objects.all()
    return render(request, 'student_view.html', {'admissions': admissions})