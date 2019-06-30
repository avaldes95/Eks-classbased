from django.contrib import admin
from . import models

# Register your models here.
class ForumMemberInline(admin.TabularInline):
    model = models.ForumMember

admin.site.register(models.Forum)
