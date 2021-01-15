from django.db import models
import hashlib



# Create your models here.
from django.contrib.auth.models import AbstractUser, Group



import random, string


def pkgen():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return x


class User(AbstractUser):

    uniqueID = models.CharField(max_length=16, primary_key=True, default=pkgen)
    startupID = models.CharField(max_length=16, blank=True)
    name_of_the_startup = models.CharField(max_length=128, blank=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    university = models.CharField(max_length=128)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    portfolio_link = models.URLField(blank=True)


    is_Team_Leader = models.BooleanField('Team leader status', default=True)
    is_Individual = models.BooleanField('Individual status', default=False)
    is_Team_Member = models.BooleanField('Team Member status', default=False)

    def getID(self):
        return self.uniqueID

class Startup(models.Model):

    name_of_the_startup = models.CharField(max_length=128)
#    members = models.ManyToManyField(User, through='TeamMemberProfileInfo')
#    teamLeaderID = models.ForeignKey(TeamLeaderProfileInfo, on_delete=models.PROTECT)
    uniqueID = models.CharField(max_length=16, primary_key=True, default=pkgen, editable=False)
#    members = []
    group = models.OneToOneField(Group,on_delete=models.CASCADE,blank=True)

    portfolio_link_of_the_Startup = models.URLField(blank=True)

    profile_logo = models.ImageField(upload_to='profile_pics',blank=True)

    def getuniqueID(self):
        return self.uniqueID


    def __str__(self):
        return self.name_of_the_startup

# Create your models here.
class IndividualProfileInfo(models.Model):



    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE,)

    # Add any additional attributes you want
#    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


# Create your models here.
class TeamLeaderProfileInfo(models.Model):
#    ID = models.UUIDField(max_length=128, default = uuid.uuid4, primary_key=True)
#    uniqueID = models.UUIDField(max_length=128, default = uuid.uuid4, primary_key=True)


    user = models.OneToOneField(User,on_delete=models.PROTECT,)
#    name_of_the_startup = models.CharField(max_length=128)
    startup = models.OneToOneField(Startup,on_delete=models.PROTECT,blank=True)
    # Create relationship (don't inherit from User!)

    # Add any additional attributes you want
#portfolio_site
#    portfolio_site = models.URLField(blank=True)

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
#    profile_logo = models.ImageField(upload_to='profile_logo',blank=True)
    startupID = models.CharField(max_length=16, blank=True)




    def __str__(self):
        return self.user.username
        # Built-in attribute of django.contrib.auth.models.User !



class TeamMemberProfileInfo(models.Model):
    uniqueID = models.CharField(max_length=16, primary_key=True, default=pkgen)

    user = models.OneToOneField(User,on_delete=models.PROTECT,)
    startupID = models.CharField(max_length=16, blank=True)
#    date_joined = models.DateField(blank=True)

        # pip install pillow to use this!
        # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
#    invite_reason = models.CharField(max_length=64)
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
