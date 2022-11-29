from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    model = Account
    list_display = ['email','phone','usr_key','name',]
    search_fields = ('email','phone',)
    ordering = ('date_joined',)
    readonly_fields = ['name','phone','usr_key','date_joined','last_login']
    
    def has_add_permission(self, request,obj=None):
        return True
    def has_edit_permission(self,request,obj=None):
        return True
    def has_delete_permission(self, request,obj=None):
        return True

##admin.site.register(Group)
admin.site.register(Account,CustomUserAdmin)
admin.site.unregister(Group)
admin.site.site_header = "Starke"
admin.site.index_title = "Área destinada a manuntenção do site"