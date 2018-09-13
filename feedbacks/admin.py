from django.contrib import admin
from .models import feedback
from .models import subscribe
from .models import tokens

# Register your models here.

admin.site.register(feedback)
admin.site.register(subscribe)
admin.site.register(tokens)