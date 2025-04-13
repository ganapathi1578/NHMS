from django.contrib import admin
from homeremedies.models import BodyPart, Disease, Remedy

@admin.register(BodyPart)
class BodyPartAdmin(admin.ModelAdmin):
    display = ('name')  # Adjust fields as needed
    search_fields = ('name',)

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_part')
    search_fields = ('name',)
    list_filter = ('body_part',)

@admin.register(Remedy)
class RemedyAdmin(admin.ModelAdmin):
    list_display = ('disease', 'name','details')
    search_fields = ('name',)
    list_filter = ('disease',)
