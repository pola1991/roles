#Importar el modelo de grupos de django
from django.contrib.auth.models import Group
#Herramienta para manejar signals(eventos que se emiten cuando ocurren ciertos eventos)
from django.db.models.signals import post_save
from.models import Profile
from django.dispatch import receiver #decorar funciones

#Se le deben pasar 2 argumentos
# Debo elegir a que signal estamos conectados (post_save)
# Debo elegir quien enviará la signal
@receiver(post_save , sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            grupo = Group.objects.get(name='estudiante')
            
        except Group.DoesNotExist:
            grupo = Group.objects.create(name='estudiante')
            grupo = Group.objects.create(name='profesor')
            grupo = Group.objects.create(name='administrativo')
        instance.user.groups.add(grupo)
        

'''
Cuando viene una señal de grabar registro, toma el receiver y toma evento.
Cuando yo creo un perfil se inicia esta funcion que dice que si esta creado el grupo 
estudiantes agrego ese perfil al grupo estudiantes y si no está creado el grupo lo creo
'''

'''
Ahora debo agregar este archivo en apps.py
'''