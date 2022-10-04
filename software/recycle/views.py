from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Task, Work, Suggestion, comment
import random
from geopy.geocoders import Nominatim
from geopy.point import Point
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

client = Client("AC6e0cc6c973c287570f121a12718e9db5", "b29af806cb1a081efe276158be9d2032")

def call(num, name, lon, lat):
  message = client.calls.create(
        from_='+13605357953',
        to = f"+{num}",
        twiml=f"<Response><Say>Hello {name}, please we come to notice that you are at longitude {lon} and latitude {lat} which is not far from the a recycle bin that is full. Please kindly dispose the plastic bin, thank you.</Say></Response>"
  )
  return message

def sms(num, name, lon, lat):
  print("ok")
  message = client.messages.create(
        body=f"Hello {name}, please we come to notice that you are at longitude {lon} and latitude {lat} which is not far from the a recycle bin that is full. Please kindly dispose the plastic bin, thank you.",
        from_='+13605357953',
        to = f"+{num}",
  )
  return message

geolocator = Nominatim(user_agent="geoapiExercises")

def verify(num, name):
  validation_request = client.validation_requests.create(
    phone_number=f"+{num}",
    friendly_name=name
  )
  return validation_request

def send_email(froms, to, long, lat):
  send_mail(
    "Recycle Bin",
    f"please we come to notice that you are at longitude {long} and latitude {lat} which is not far from the a recycle bin that is full. Please kindly dispose the plastic bin. Thank you",
    froms,
    to,
    fail_silently=False
  )

def get_random_code():
  num = 0
  count = 8
  rand = ""
  while num < count:
    ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    rand += str(ran)
    num += 1

  return rand

def receive(request):
  resp = VoiceResponse()

  resp.say("hello world", voice="alice")
  
  return str(resp)

def home(request):
  s = Suggestion.objects.all().order_by("posted")[::-1]
  contest = {
    "s": s,
  }
  return render(request, "home.html", contest)

@login_required(login_url = 'loginpage')
def comments(request):
    if request.method == 'POST':
        title = request.POST.get('post')
        describtion = request.POST.get('message')
        newsupport = comment()
        newsupport.user = request.user
        newsupport.post_id = title
        newsupport.describtion = describtion
        newsupport.save()
        return redirect(f'about/{title}/')

    return redirect('/')
def post(request):
  return render(request, "post/suggestion.html")

def about(request, id):
  s = Suggestion.objects.get(id = int(id))
  su = Suggestion.objects.filter(user = s.user)
  c = s.comment_set.all()
  context = {
    "s": s,
    "c": c,
    "su": su,
  }
  return render(request, "about.html", context)

def scavenger(request):
  return render(request, "scavenger/index.html")

@api_view(["GET"])
def check_work(request, *arg, **kwarg):
  ids = request.query_params.get("ids")

  res = Work.objects.filter(id=ids)
  res = res.done

  return Response({"status": res}, status=200)

def add_work(request, longitude, latitude):
  "http://127.0.0.1:8000/add_work/6.5437696/3.342336"
  loaction = geolocator.reverse("6.5437696, 3.342336")
  address = loaction.raw["address"]
  state = address.get("state", "")
  conutry = address.get("country", "")
  code = get_random_code()
  val = Work.objects.filter(code = code)
  while len(val)!=0:
    print("hello")
    code = get_random_code()
    val = Work.objects.filter(code = code)
    print("ok1", val, code)
  
  work = Work.objects.create(code = code, longitude = longitude, latitude = latitude, state = state, country = conutry)
  work.save()

  return JsonResponse({"ids": code})

@api_view(["GET"])
def call_someone(request, *arg, **kwarg):
  ids = request.query_params.get("ids")

  res = Work.objects.filter(code=ids).first()
  longitude = res.longitude
  latitude = res.latitude
  state = res.state

  results = Profile.objects.filter(longitude = longitude, latitude = latitude)
  result = Profile.objects.filter(location_state = state)

  froms = ""
  to = []
  if len(results) != 0:
    for i in results:
      if i.contact == "call":
        ans = call(i.phone, i.first_name, i.longitude, i.latitude)
        while ans.fetch().status != "no-answer" and ans.fetch().status != "completed":
          ins = ans.fetch()
          print(ins.status)
          if ins.status == "in-progress":
            print(ins.to)
            numb = ins.to.replace("+", "")
            p = Profile.objects.get(phone=numb)
            w = Work.objects.get(code=ids)
            w.done = True
            w.save()
            t = Task(profile_id = p.id, work_id = w.id)
            t.save()
            break
      elif i.contact == "sms":
        m = sms(i.phone, i.first_name, i.longitude, i.latitude)
        print(m.sid)
      elif i.contact == "email":
        ress = i.email
        to = list(ress)
        send_email(froms, to, longitude, latitude)
      
  elif len(result) != 0:
    for i in result:
      if i.contact == "call":
        ans = call(i.phone, i.first_name, i.longitude, i.latitude)
        while ans.fetch().status != "no-answer" and ans.fetch().status != "completed":
          ins = ans.fetch()
          print(ins.status)
          if ins.status == "in-progress":
            print(ins.to)
      elif i.contact == "sms":
        m = sms(i.phone, i.first_name, i.longitude, i.latitude)
        print(m.to)
      elif i.contact == "email":
        ress = i.email
        to = list(ress)
        send_email(froms, to, longitude, latitude)

  return Response({"results": "results", "result": "result"}, status=200)


