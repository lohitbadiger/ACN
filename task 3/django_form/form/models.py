from django.db import models
from phone_field import PhoneField
# Create your models here.
 # NAME, PHONENUMBER, EMAILID
 
#  Now we need to create our Model for our Forms. So to do that just open the models.py file in the editor and type these following commands.

class InfoStore(models.Model):
    
    # InfoStore form has these name, phone  and email in the database
    name=models.CharField(max_length=200)
    phone =PhoneField(max_length=11, help_text='Contact phone number')

    email=models.EmailField()
    
    # function to show the content in admin page, by 'name' 
    def __str__(self):
        return self.name
    
    
    
    
    
   