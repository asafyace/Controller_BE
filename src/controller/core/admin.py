from django.contrib import admin
from .models import Server, Lab, User, Complain, Command
from import_export.admin import ImportExportModelAdmin


admin.site.register(User)
admin.site.register(Lab)
admin.site.register(Complain)


@admin.register(Command)
class CommandAdmin(ImportExportModelAdmin):
    pass


@admin.register(Server)
class ServerAdmin(ImportExportModelAdmin):
    pass
