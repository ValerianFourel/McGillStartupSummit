from django.conf.urls import url
from registration import views
from django.urls import include, path


# SET THE NAMESPACE!
app_name = 'registration'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^registerTeamLeader/$',views.registerTeamLeader,name='registerTeamLeader'),
    url(r'^menu/$',views.menu,name='menu'),
    url(r'^change_password/$',views.change_password,name='change_password'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^event/$',views.event,name='event'),
    path(r'^registerTeamMember/<str:startupID>/$',views.registerTeamMember,name='registerTeamMember'),
    path(r'^editInfo/<int:startup>/$',views.editInfo,name='editInfo'),
    path(r'^viewTM/<str:uniqueID>/$',views.viewTM,name='viewTM'),


#    url(r'^registerTeamMember/(?P<startupID>\d+)/$',views.registerTeamMember,name='registerTeamMember'),




]
