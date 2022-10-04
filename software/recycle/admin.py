from django.contrib import admin
from .models import Profile, Work, Task, Suggestion

class TaskAdmin(admin.StackedInline):
    model = Task

class ProfileAdmins(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            "fields": (
                'first_name', 'last_name', 'email', 'phone', 'dob', 'avatar'
            ),
        }),

        ('Contact Info', {
            "fields": (
                'contact', 'state', 'country', 'longitude', 'latitude', 'nin'
            ),
        }),
    )
    inlines = [TaskAdmin]

admin.site.register(Profile, ProfileAdmins)
admin.site.register(Work)
admin.site.register(Suggestion)