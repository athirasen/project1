from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mysite.core.models import *

from mysite.core.forms import SignUpForm




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#def tech_list(request):
 #   techs = tech.objects.all()
  #  return render(request, '/home.html', {'techs': techs})
@login_required
def home(request):
  user = request.user
  profile = Profile.objects.get(user = user)
  techs = tech.objects.filter(user = profile)
  print(techs.values())
  data = {'techs':techs.values(),
          'username': user.username}
  return render(request,"home.html", data)

@login_required
def change_status(request):
  name = (request.GET.get('name'))
  value = (request.GET.get('value'))
  t = tech.objects.get(id = name)
  if value == 'true':
    t.status = True 
  else:
    t.status = False
  t.save()
  return render(request,"status_changed.html")

@login_required
def addcomp(request):
  user = request.user
  profile = Profile.objects.get(user = user)
  return render(request,"add.html")


