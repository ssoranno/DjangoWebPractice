from django.contrib import admin
from .models import Meeting
from .models import Contact
from .models import Room
from .models import CyberSkill
from .models import DevSkill
from .models import CloudPlatform


# Register your models here.
admin.site.register(Meeting)
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(CyberSkill)
admin.site.register(DevSkill)
admin.site.register(CloudPlatform)