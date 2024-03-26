from django.db import models
#Traer la tabla user de django por defecto
from django.contrib.auth.models import User
#Para poder crear y guardar correctamente
from django.db.models.signals import post_save


# PERFIL DE USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    telephone= models.CharField(max_length=150, null=True, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'
        ordering= ['-id'] #Muestra el registro mas reciente
    #Define un método __str__() que devuelve una representación de cadena del perfil.
    def __str__(self):
        return self.user.username
    
#Al momento de crear el usuario se tiene que crear el perfil
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#Cuando se graba un perfil termina impactando la base de datos de perfiles
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() #Se graba el perfil

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender= User)

'''Cada vez que se guarda un objeto User (es decir, cada vez que se crea un nuevo usuario), se activan esas funciones. 
La primera función, create_user_profile, crea un perfil asociado al usuario recién creado, y la segunda función, save_user_profile,
guarda ese perfil en la base de datos. De esta manera, aseguramos que cada usuario tenga automáticamente un perfil asociado en el sistema.'''