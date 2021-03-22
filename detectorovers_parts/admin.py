from django.contrib import admin
from detectorovers_parts.models import Part

class PartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Part, PartAdmin)
