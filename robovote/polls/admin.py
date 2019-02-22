from django.contrib import admin
from .models import Team, Backer
# Register your models here.
admin.sites.site.register(Team)
admin.sites.site.register(Backer)