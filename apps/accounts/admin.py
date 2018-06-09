from django.contrib import admin
from apps.accounts.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    """
        Nothing Yet.

        Notes:
            "Add sorts for users by username, location, age(date of creation to
                now), and last Active." - Rantahu
    """

admin.site.register(Profile, ProfileAdmin)


