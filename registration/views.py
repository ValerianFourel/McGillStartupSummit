from django.shortcuts import render, redirect
from registration.forms import UserForm,IndividualProfileInfoForm, TeamLeaderProfileInfoForm, TeamMemberProfileInfoForm, StartupForm, EditProfileForm, EditStartupForm, ContactForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from registration.models import Startup
from django.views.generic import View
from django.core.mail import send_mail


import os
import logging
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import urllib
# import cv2
import requests
from django.contrib.auth.models import Group


from django.urls import reverse

from django.contrib import messages



s3_signature ={
'v4':'s3v4',
'v2':'s3'
}



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserChangeForm

from django.apps import apps
from registration.models import User


# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        startupID = request.user.startupID
    else:
        startupID = '0000'
    return render(request,'registration/index.html',{'startupID':startupID})

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(request.POST,request.FILES)
        profile_form = IndividualProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():


            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)
            user.is_Team_Leader = False
            user.is_Individual = True


            # Update with Hashed password

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and IndividualProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                user.profile_pic = request.FILES['profile_pic']

            # Now save model
            user.save()

            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = IndividualProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'registration/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'registration/login.html', {})
# Create your views here.

def registerTeamLeader(request,startupID='Default User'):


     registered = False


     if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
#        user_form = UserForm(data=request.POST)
        user_form = UserForm(request.POST,request.FILES)
#        user_form = UserForm(data=request.POST)
        profile_form = TeamLeaderProfileInfoForm(data=request.POST)
        startup_form = StartupForm(request.POST,request.FILES)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid() and startup_form.is_valid():

            # Save User Form to Database
            user = user_form.save(commit=False)
                        # Can't commit yet because we still need to manipulate
            startup = startup_form.save(commit=False)
            user.startupID = startup.uniqueID
            user.set_password(user.password)
            user.name_of_the_startup = startup.name_of_the_startup
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and IndividualProfileInfoForm
            profile.user = user
            user.save()



            # we create the startup
            group = Group.objects.create(name=user.name_of_the_startup)
            startup.group = group

            # we thenb add the user to to it

    #        group = user_form.save()

            # Hash the password
    #        group.password(group.password)

            # Update with Hashed password
    #        group.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate


            #startup =user.getID
            profile.startup = startup
    #        profile.user.name_of_the_startup = request.FILES['name_of_the_startup']


            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                user.profile_pic = request.FILES['profile_pic']

            if 'profile_logo' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                startup.profile_logo = request.FILES['profile_logo']

#            group.save()

            # Now save model
        #    user.save()
            profile.startupID = startup.uniqueID



            startup.save()

            profile.save()
            user.groups.add(startup.group)

            startupID = profile.startup.getuniqueID







            registered = True



            # Registration Successful!

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors,)

     else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = TeamLeaderProfileInfoForm()
        startup_form = StartupForm()

    #    user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
     return render(request,'registration/groupRegistration.html',{'user_form':user_form,'profile_form':profile_form,'startup_form':startup_form, 'startupID':startupID,  'registered':registered})
                         #  'user_form': user_form,
def registerTeamMember(request,startupID='Default User'):

     registered = False

     startup = Startup.objects.get(uniqueID=startupID)


     if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
#        user_form = UserForm(data=request.POST)
        user_form = UserForm(request.POST,request.FILES)
        profile_form = TeamMemberProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():



            # Save User Form to Database
            user = user_form.save(commit=False)

    #        group = user_form.save()

            # Hash the password
            user.set_password(user.password)
            user.is_Team_Leader = False
            user.is_Team_Member = True
            user.startupID = startup.uniqueID
            user.name_of_the_startup = startup.name_of_the_startup




    #        group.password(group.password)

            # Update with Hashed password

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and IndividualProfileInfoForm
            profile.user = user
            profile.startupID = startup.uniqueID
            user.save()


            # we are getting the group

            group = Group.objects.get(name=user.name_of_the_startup)
            startup.group = group


            # we are adding the user to the group
            user.groups.add(startup.group)




            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                user.profile_pic = request.FILES['profile_pic']




            profile.save()


            registered = True



            # Registration Successful!

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors,)

     else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = TeamMemberProfileInfoForm()
    #    user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
     return render(request,'registration/memberRegistration.html',{'user_form':user_form,'profile_form':profile_form,'startupID':startupID, 'registered':registered})
     #return HttpResponseRedirect(reverse('registerTeamMember',args=[startupID]))



def menu(request):




    if(request.user.startupID):
        startupID = request.user.startupID
        startup = Startup.objects.get(uniqueID=startupID)
        allMembers = User.objects.filter(groups__name=startup.name_of_the_startup)
    else:
        startupID = '0000'
        allMembers = []







    return render(request,'registration/menu.html',{'startupID':startupID,'allMembers':allMembers})



def editInfo(request, startup= 0):

    startupID = request.user.startupID

    if startup == 0:
        if request.method == 'POST':
            profile_form = EditProfileForm(request.POST, instance = request.user)

            if profile_form.is_valid():
                profile_form.save()


                startup = Startup.objects.get(uniqueID=startupID)
                allMembers = User.objects.filter(groups__name=startup.name_of_the_startup)
                return render(request,'registration/menu.html',{'startupID':startupID,'allMembers':allMembers})

        else:
            profile_form = EditProfileForm(instance=request.user)
            args = {'profile_form':profile_form,'startup':startup,'startupID':startupID}


            return render(request,'registration/editInfo.html',args)
    else:
        startupID = request.user.startupID
        instance = Startup.objects.get(uniqueID=startupID)
        group = Group.objects.get(name=instance.name_of_the_startup)




        if request.method == 'POST':

            profile_form = EditStartupForm(request.POST, instance = instance)

            if profile_form.is_valid():
                profile = profile_form.save()
                group.name = profile.name_of_the_startup
                group.save()


                allMembers = User.objects.filter(groups__name=instance.name_of_the_startup)

                for user in allMembers:
                    user.name_of_the_startup = profile.name_of_the_startup
                    user.save()

        #        startupID = request.user.startupID


                return render(request,'registration/menu.html',{'startupID':startupID,'allMembers':allMembers})

        else:
            profile_form = EditStartupForm(instance=instance)
            args = {'profile_form':profile_form,'startup':startup,'startupID':startupID}



        return render(request,'registration/editInfo.html',args)



def viewTM(request,uniqueID='Default User'):

    if(request.user.is_authenticated):
        startupID = request.user.startupID

    startup = Startup.objects.get(uniqueID=startupID)
    allMembers = User.objects.filter(groups__name=startup.name_of_the_startup)


    member = User.objects.get(uniqueID=uniqueID)
#    profile_pic = Image.objects.get(filename=uniqueID)
    if member.profile_pic:
        AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')
        profile_pic_url = member.profile_pic.__str__()
    #    firstpart , profile_pic_name = profile_pic_url.split('/')

    #    seven_days_as_seconds = 600
        pic_url = create_presigned_url(AWS_STORAGE_BUCKET_NAME, profile_pic_url)


    else:
        pic_url = None

    args = {'uniqueID':uniqueID,'member':member, 'allMembers':allMembers,'pic_url':pic_url,'startupID':startupID} # 'profile_pic':profile_pic}





    return render(request,'registration/viewTM.html',args)

def change_password(request):
    startupID = request.user.startupID;


    startup = Startup.objects.get(uniqueID=startupID)
    allMembers = User.objects.filter(groups__name=startup.name_of_the_startup)



    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()

            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'registration/menu.html', {
             'startupID':startupID, 'allMembers':allMembers

            })
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form, 'allMembers':allMembers, 'startupID':startupID
    })



#

def contact(request):
    if(request.user.is_authenticated):
        startupID = request.user.startupID
    else:
        startupID = '000'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_first_name = form.cleaned_data['first_name']
            sender_last_name = form.cleaned_data['last_name']
            sender_name = sender_last_name +' '+ sender_first_name
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_email , form.cleaned_data['message'])
            send_mail('New Enquiry', message,sender_email, ['admin@startupsummit.ca'])
            return render(request,'registration/index.html',{'startupID':startupID})
    else:
        form = ContactForm()

    return render(request, 'registration/contact.html', {'form': form,'startupID':startupID })

def event(request):
    if(request.user.is_authenticated):
        startupID = request.user.startupID
    else:
        startupID = '0000'
    return render(request,'registration/event.html',{'startupID':startupID})

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration, HttpMethod="GET" )
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response




#def url_to_image(URL):
#    resp = urllib.request.urlopen(url)
#    image = np.asarray(bytearray(resp.read()), dtype="uint8")
#    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

#    return resp
