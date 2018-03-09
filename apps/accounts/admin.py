from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    """
        Nothing Yet.

        Notes:
            "Add sorts for users by username, location, age(date of creation to
                now), and last Active." - Rantahu
    """

admin.site.register(Profile, ProfileAdmin)


class Clan(admin.ModelAdmin):
    """
        Nothing Yet.

        Notes:
            "Add sorts for clans by name and popularity" - Rantahu
    """

admin.site.register(Clan, ProfileImg)
