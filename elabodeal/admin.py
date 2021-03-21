from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from elabodeal.models import User, Publisher, ProductGroup


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
	list_display = ['id', 'name', 'publisher']

	fieldsets = [
		[
			None,
			{
				'fields': [
					'id', 'publisher', 
					'name', 'created_at',
					'updated_at'
				]
			}
		]
	]

	add_fieldsets = [
		[
			None,
			{
				'fields': ['publisher', 'name']
			}
		]
	]

	readonly_fields = ['id', 'created_at', 'updated_at']

	search_fields = ['id', 'name']

admin.site.register(User, UserAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)

# The group model is not used to.
admin.site.unregister(Group)

# Site settings
admin.site.site_header = _('Elabodeal - Panel administracyjny')


# class CategoryAdmin(admin.ModelAdmin):
# 	list_display = ('name', )

# 	list_filter = ('name', )
	
# 	fieldsets = ((None, {'fields': ('name', )}), )
	
# 	add_fieldsets = (
# 		(None, {
# 			'classes': ('wide', ),
# 			'fields': ('name', )}
# 		),
# 	)
	
# 	search_fields = ('name', )
	
# 	ordering = ('name', )	


# class ProductAdmin(admin.ModelAdmin):
# 	list_display = (
# 		'title', 'category',
# 		'publisher', 'price')
	
# 	list_filter = ('category', 'author', 'title')
	
# 	fieldsets = (
# 		(None, {
# 			'fields': (
# 				'publisher', 'category',
# 				'labels', 'opinions',
# 				'title', 'description',
# 				'price', 'author',
# 				'page_count', 'isbn',
# 				'contents', 'age_category',
# 				'url_name', 'average_rating',
# 				'rating_count', 'cover_img',
# 				'pdf_file', 'epub_file', 
# 				'mobi_file', 'published_at',
# 				'updated_at', 'demo_file')
# 		}),
# 	)

# 	readonly_fields = (
# 		'published_at', 'updated_at',
# 		'pdf_file', 'mobi_file',
# 		'epub_file', 'age_category',
# 		'price', 'rating_count',
# 		'average_rating', 'cover_img',
# 		'isbn', 'contents', 'page_count',
# 		'url_name', 'author',
# 		'publisher', 'demo_file')

# 	add_fieldsets = (
# 		(None, {
# 			'fields': (
# 				'publisher', 'category',
# 				'labels', 'opinions',
# 				'title', 'description',
# 				'price', 'author',
# 				'page_count', 'isbn',
# 				'contents', 'age_category',
# 				'url_name', 'epub_file', 
# 				'pdf_file', 'mobi_file')
# 		})
# 	)

# 	search_fields = (
# 		'category', 'author',
# 		'title', 'price',
# 		'author', 'publisher')
	
# 	ordering = (
# 		'category', 'author',
# 		'price', 'published_at')


# class FileAdmin(admin.ModelAdmin):
# 	fieldsets = (
# 		(None, {
# 			'fields': (
# 				'uuid', 'uploaded_at',
# 				'size', 'path',
# 				'extension')
# 		}),
# 	)

# 	readonly_fields = (
# 		'uploaded_at', 'size', 
# 		'extension', 'uuid',
# 		'path')


# class SharedCartAdmin(admin.ModelAdmin):
# 	list_display = ('code', 'shared_at')

# 	fieldsets = (
# 		(None, {
# 			'fields': ('code', 'shared_at',
# 					   'cart')
# 		}),
# 	)
	
# 	readonly_fields = ('code', 'shared_at', 'cart')


# class ProductLabelAdmin(admin.ModelAdmin):
# 	fieldsets = (
# 		(None, {
# 			'fields': ('name', 'color')
# 		}),
# 	)