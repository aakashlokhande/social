from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import ugettext_lazy as _

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name,last_name, mobile_number,  password=None, ):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not mobile_number:
            raise ValueError('User must have a mobile Number')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,first_name, last_name, mobile_number):
        user =self.create_user(
			email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
			password=password,
		)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username=None
    mobile_number = models.CharField(max_length=30, unique=True, null=True)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country_iso= models.CharField(max_length=10,null=True)
    profile_pic = models.ImageField(default='default2.jpg', upload_to='profile_pics')
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)

    REQUIRED_FIELDS = ['first_name','last_name','mobile_number']
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    objects = MyAccountManager()

    def __str__(self):
	    return self.email
