from django.contrib import admin

from tts.models import Project, Audio, Title

admin.site.register(Title)
admin.site.register(Project)
admin.site.register(Audio)
