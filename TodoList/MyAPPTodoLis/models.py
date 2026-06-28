from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    num=models.AutoField(primary_key=True)
    nomC=models.CharField(max_length=100)
    email=models.EmailField()
    pwd=models.CharField(max_length=100)
    metier=models.CharField(max_length=50, choices=[
        ('jardinier', 'Jardinier'),
        ('bawab', 'Bawab/Gardien'),
        ('cuisinier', 'Cuisinier/Cuisinière'),
        ('femme_menage', 'Femme de ménage'),
        ('chauffeur', 'Chauffeur'),
        ('nounou', 'Nounou/Garde d\'enfants'),
    ], default='femme_menage')  
    
    
    def __str__(self):
        return f" {self.nomC}({self.metier})"
    
@receiver(post_save, sender=Client)
def create_user_for_client(sender, instance, created, **kwargs):
     if created:  
        
        username = instance.nomC.lower().replace(' ', '')
        if User.objects.filter(username=username).exists():
            username = f"{username}{instance.num}"
        
        
        User.objects.create_user(
            username=username,
            email=instance.email,
            password=instance.pwd,
            first_name=instance.nomC
        )
    
class List(models.Model):
    num=models.AutoField(primary_key=True)
    date=models.DateTimeField(auto_now_add=True)
    element=models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        
        if self.client:
            return f"Tâche pour {self.client.nomC} - {self.client.get_metier_display()}"
      
