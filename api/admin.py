from django.contrib import admin
from .models import User_details
from import_export.admin import ImportExportModelAdmin

@admin.register(User_details)
class ImageAdmin(ImportExportModelAdmin):
    list_display = ['id','token','user_name','user_email','google_id','facebook_id','apple_id','profile_preview','user_phone_no','is_guest','is_deleted','datetime']
    readonly_fields = ['datetime']
    search_fields=['token','user_name','user_email']

