from django.contrib import admin
from .models import Theitchlist

# Register your models here.
class TheitchlistAdmin(admin.ModelAdmin):
    list = ('title', 'description', 'completed')


admin.site.register(Theitchlist, TheitchlistAdmin)
