from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from elabodeal.models import User


class UserAdmin(BaseUserAdmin):
	list_display = ('email', 'username', 'is_staff')
	list_filter = ('is_superuser', 'email', 'last_login')
	fieldsets = (
		(None, {'fields': (
			'email', 'username', 'password', 'email_verified', 'email_verified_at',
			'is_superuser', 'is_staff', 'is_active', 'last_login',
		)}),

	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'username', 'password1', 'password2')}
		),
	)
	search_fields = ('email', 'username')
	ordering = ('email', 'username')
	filter_horizontal = ()

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)