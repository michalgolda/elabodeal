from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from elabodeal.models import (
	User, Publisher, ProductGroup,
	Category, ProductLanguage
)


class UserAdmin(BaseUserAdmin):
	list_display = ['id', 'username', 'email']

	fieldsets = [
		[
			None,
			{
				'fields': [
					'id', 'publisher', 'username',
					'email', 'email_verified', 'email_verified_at',
					'is_staff', 'is_online', 'is_superuser',
					'created_at', 'updated_at'
				]
			}
		]
	]

	add_fieldsets = [
		[
			None,
			{
				'fields': [
					'email', 'username', 
					'password1', 'password2'
				]
			}
		]
	]

	readonly_fields = [
		'id', 'created_at', 
		'updated_at', 'is_online'
	]

	search_fields = ['id', 'username', 'email']

	list_filter = ['is_online', 'is_superuser', 'is_staff']
	
	filter_horizontal = []


class PublisherAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name']

	fieldsets = [
		[
			None,
			{
				'fields': [
					'id', 'first_name', 
					'last_name', 'account_number', 
					'swift', 'created_at',
					'updated_at'
				]
			}
		]
	]

	add_fieldsets = [
		[
			None,
			{
				'fields': [
					'first_name', 'last_name', 
					'account_number', 'swift'
				]
			}
		]
	]

	readonly_fields = ['id', 'created_at', 'updated_at']

	search_fields = [
		'id', 'first_name', 'last_name',
		'account_number'
	]


class ProductGroupAdmin(admin.ModelAdmin):
	list_display = ['id', 'publisher']

	fieldsets = [
		[
			None,
			{
				'fields': [
					'id', 'publisher',
					'created_at', 'updated_at'
				]
			}
		]
	]

	add_fieldsets = [
		[
			None,
			{
				'fields': ['publisher']
			}
		]
	]

	readonly_fields = ['id', 'created_at', 'updated_at']

	search_fields = ['id']


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

	fieldsets = [
		[
			None,
			{
				'fields': ['id', 'name']
			}
		]
	]

	add_fieldsets = [
		[
			None,
			{
				'fields': ['name']
			}
		]
	]

	readonly_fields = ['id']

	search_fields = ['id', 'name']


class ProductLanguageAdmin(admin.ModelAdmin):
	list_display = ['id', 'code', 'name']

	fieldsets = [
		[
			None,
			{
				'fields': ['id', 'name', 'code']
			}
		]
	]

	add_fieldsets = [
		[
			None,
			{
				'fields': ['name', 'code']
			}
		]
	]

	readonly_fields = ['id']

	search_fields = ['name', 'code']


admin.site.register(User, UserAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductLanguage, ProductLanguageAdmin)

# The group model is not used to.
admin.site.unregister(Group)

# Site settings
admin.site.site_header = _('Elabodeal - Panel administracyjny')