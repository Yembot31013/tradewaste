from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required(login_url = 'loginpage')
def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        state = request.POST.get('state')
        lon = request.POST.get('lon')
        lat = request.POST.get('lat')
        location_state = request.POST.get('location_state')
        nin = request.POST.get('nin')
        avatar = request.FILES.get('avatar')
        newsupport = Profile.objects.filter(user=request.user)
        if newsupport:
            messages.success(request, "You already have an account")
            return redirect('/')
        newsupport = Profile()
        newsupport.user = request.user
        newsupport.first_name = fname
        newsupport.last_name = lname
        newsupport.contact = contact
        newsupport.phone = phone
        newsupport.email = email
        newsupport.location_state = location_state
        newsupport.state = state
        newsupport.country = country
        newsupport.longitude = lon
        newsupport.latitude = lat
        newsupport.nin = nin
        newsupport.avatar = avatar
        newsupport.save()

        messages.success(request, "Account created successfully")
        return redirect('/')

    return redirect('/')
