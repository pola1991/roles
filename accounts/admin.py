from django.contrib import admin
from .models import Profile

# Cuando cualquier usuario se registre vaya a estar en el perfil de estudiante

#Para que se vea profile detallado en administrador django
class ProfileAdmin(admin.ModelAdmin):
    list_display= ('user', 'address', 'telephone', 'user_group')
    search_fields= ('user__username', 'user__groups__name')
    list_filter= ['user__groups']

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

admin.site.register(Profile, ProfileAdmin)