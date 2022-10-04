from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=70, null=True, blank=True)
  describtion = models.TextField(null=True, blank=True)
  image = models.ImageField(default='avatar.png', upload_to='post_img/', null=True, blank=True)
  posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  like = models.IntegerField(null=True, blank=True)

  def __str__(self) -> str:
    return f"{self.title}"

class likes(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Suggestion, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self) -> str:
    return f"{self.post}"
  
class comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Suggestion, on_delete=models.CASCADE, null=True, blank=True)
  describtion = models.TextField(null=True, blank=True)

  def __str__(self) -> str:
    return f"{self.post}"
  

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=70, null=True, blank=True)
  last_name = models.CharField(max_length=70, null=True, blank=True)
  dob = models.DateField(null=True, blank=True)
  contact = models.CharField(max_length=70, null=True, blank=True)
  phone = models.IntegerField(max_length=11, null=True, blank=True)
  email = models.EmailField(max_length=70, null=True, blank=True)
  location_state = models.CharField(max_length=20, null=True, blank=True)
  state = models.CharField(max_length=20, null=True, blank=True)
  country = models.CharField(max_length=20, null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)
  latitude = models.FloatField(null=True, blank=True)
  nin = models.IntegerField(max_length=11, null=True, blank=True)
  avatar = models.ImageField(default='avatar.png', upload_to='user_img/', null=True, blank=True)
  slug = models.CharField(max_length=9, null=True, blank=True, unique=True)

  def __str__(self) -> str:
    return f"{self.user}"

class Work(models.Model):
  code = models.CharField(max_length=9, null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)
  latitude = models.FloatField(null=True, blank=True)
  state = models.CharField(max_length=20, null=True, blank=True)
  country = models.CharField(max_length=20, null=True, blank=True)
  done = models.BooleanField(null=True, blank=True, default=False)
  period = models.DateTimeField(null=True, blank=True, auto_now_add=True)
  def __str__(self) -> str:
    return f"{self.code}"

class Task(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  work = models.ForeignKey(Work, on_delete=models.CASCADE)
  period = models.DateTimeField(null=True, blank=True, auto_now_add=True)
  def __str__(self) -> str:
    return f"{self.profile}"
