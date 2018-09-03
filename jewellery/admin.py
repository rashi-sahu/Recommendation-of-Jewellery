from django.contrib import admin

# Register your models here.
from .models import Jewellery,color,dress

admin.site.register(Jewellery)
admin.site.register(color)
admin.site.register(dress)