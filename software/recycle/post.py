from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Suggestion, likes
import datetime


@login_required(login_url = 'loginpage')
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        describtion = request.POST.get('describtion')
        image = request.FILES.get('image')
        newsupport = Suggestion()
        newsupport.user = request.user
        newsupport.title = title
        newsupport.describtion = describtion
        newsupport.image = image
        newsupport.posted = datetime.datetime.now()
        newsupport.like = 0
        newsupport.save()

        messages.success(request, "posted successfully")
        return redirect('suggestion')

    return redirect('/')

@login_required(login_url = 'loginpage')
def add_likes(request, post):
    like = likes.objects.filter(user=request.user, post_id=post)
    if like == []:
        like = likes.objects.create(user=request.user, post_id=post)
        v = Suggestion.objects.get(id=post)
        v.like += 1
        v.save()
    else:
        like = likes.objects.get(user=request.user, post_id=post)
        like.delete()
        v = Suggestion.objects.get(id=post)
        v.like -= 1
        v.save()
    v = Suggestion.objects.get(id=post)
    return JsonResponse({"status":"success", "likes": v.like, "id": post})
