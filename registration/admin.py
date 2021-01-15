from django.contrib import admin
from registration.models import TeamLeaderProfileInfo, User, IndividualProfileInfo, TeamMemberProfileInfo, Startup
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(TeamLeaderProfileInfo)
admin.site.register(User)
admin.site.register(IndividualProfileInfo)
admin.site.register(Startup)
admin.site.register(TeamMemberProfileInfo)
