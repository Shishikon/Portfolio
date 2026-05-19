from django.contrib import admin
from .models import *

class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link')
    list_display_links = ('title', 'github_link')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    list_display_links = ('full_name',)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization')
    list_display_links = ('title', 'organization')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree')
    list_display_links = ('institution', 'degree')


admin.site.register(TechStack, TechStackAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
