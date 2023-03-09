from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
class BookAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number','description')

admin.site.register(MyfutureForm, BookAdmin)