from django.shortcuts import render,redirect
from .forms import SignUpForm,ProfileForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile,Notifications,Followers
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required(login_url='/auth/login')
def profile(request):
    notifications = Notifications.objects.filter(user=request.user)
    link = "http://{}/malisafi/{}".format(get_current_site(request),request.user.username)
    if request.method == 'POST':        
        profForm = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if profForm.is_valid():
            profForm.save()
            user=request.user
            user.username = profForm.cleaned_data.get('username')
            user.email = profForm.cleaned_data.get('email')
            user.save()
            return redirect('/')  
    profForm= ProfileForm()    
    return render(request,'profile.html',{"notifications":notifications,"profForm":profForm,"link":link})

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,email=email, password=raw_password)
            profile = Profile(user=user,phone_number=form.cleaned_data.get('phone_number'))
            profile.save()
            BotMessage = "Hi {}, my name is javis and I'll be your virtual assistant. I'll be with you every step of the way. Mobilise,organise, stop sending messages, VIVA".format(user.username)
            notification = Notifications(user=user,message=BotMessage)
            notification.save()
            user.is_active = True
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})

@login_required(login_url='/auth/login')
def connections(request,user_name):
    user=User.objects.get(username=user_name)
    follower = Followers(user=user,follower=request.user)
    follower.save()
    return redirect('/')
