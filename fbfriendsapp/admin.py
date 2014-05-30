from django.contrib import admin

from fbfriendsapp.models import Register,LinkedinProfileData,LinkedinUserFriendsData

admin.site.register(Register)
admin.site.register(LinkedinProfileData)
admin.site.register(LinkedinUserFriendsData)