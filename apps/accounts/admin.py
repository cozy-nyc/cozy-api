from django.contrib import admin
from apps.accounts.models import Profile, Clan, ProfileImg

class ProfileAdmin(admin.ModelAdmin):
    """
        Nothing Yet.

        Notes:
            "Add sorts for users by username, location, age(date of creation to
                now), and last Active." - Rantahu
    """

admin.site.register(Profile, ProfileAdmin)


class ClanAdmin(admin.ModelAdmin):
    """
        Nothing Yet.

        Notes:
            "Add sorts for clans by name and popularity" - Rantahu
    """

admin.site.register(Clan, ClanAdmin)
