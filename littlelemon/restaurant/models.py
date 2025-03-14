from django.db import models

# Modèle Booking
class Booking(models.Model):
   Name = models.CharField(max_length=255)    
   No_of_guests = models.IntegerField(default=6)
   BookingDate = models.DateTimeField()

   def __str__(self):
      return self.Name  # Correction ici

# Modèle Menu
class Menu(models.Model):
   Title = models.CharField(max_length=255) 
   Price = models.DecimalField(max_digits=10, decimal_places=2) 
   Inventory = models.IntegerField(default=5) 

   def get_item(self):
      return f'{self.Title} : {str(self.Price)}'
