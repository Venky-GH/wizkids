from django.contrib import admin
from .models import course
from .models import topic
from .models import content

# Register your models here.

admin.site.register(course)
admin.site.register(topic)
admin.site.register(content)
