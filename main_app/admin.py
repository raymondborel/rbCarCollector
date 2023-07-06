from django.contrib import admin
from .models import Make
from .models import CarModel
from .models import Collection
# Register your models here.
admin.site.register(Make)
admin.site.register(CarModel)
admin.site.register(Collection)