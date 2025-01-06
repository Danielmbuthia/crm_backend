from django.contrib import admin
from .models import Note,Contact,Lead,Reminder
# Register your models here.
@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','phone','lead']
    search_fields = ['name','email','phone','lead']
    list_filter =['name','lead']


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ['content','lead']
    search_fields = ['content',]
    list_filter =['content','lead']

@admin.register(Reminder)
class AdminReminder(admin.ModelAdmin):
    list_display = ['message','formatted_reminder_time','lead']
    search_fields = ['message']
    list_filter =['reminder_time','lead']

    def formatted_reminder_time(self, obj):
        return obj.reminder_time.strftime('%B %d, %Y at %I:%M %p') 
    formatted_reminder_time.admin_order_field = 'reminder_time' 
    formatted_reminder_time.short_description = 'Scheduled Time' 

@admin.register(Lead)
class AdminLead(admin.ModelAdmin):
    list_display = ['name','email','phone']
    search_fields = ['name','email','phone']
    list_filter =['name','email']
