from django.contrib import admin
from . models import Posts,Author,Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tag","date",)
    list_display =("title","date","author",)

admin.site.register(Posts,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

# Register your models here.
