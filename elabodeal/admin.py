from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from elabodeal.models import (User, Category, Product, File, 
							  SharedCart, ProductLabel)


class UserAdmin(BaseUserAdmin):
	list_display = (
		'email', 'username', 
		'is_active', 'is_superuser',
		'is_online')

	list_filter = (
		'is_active', 'is_online',
		'is_superuser')

	fieldsets = (
		(None, {
			'fields': (
				'username', 'email', 
				'email_verified', 'email_verified_at',
				'is_active', 'is_online',
				'is_staff', 'publisher')
		}),
	)

	readonly_fields=(
		'publisher', 
		'is_online', 
		'email')

	add_fieldsets = (
		(None, {
			'classes': ('wide', ),
			'fields': (
				'email', 'username',
				'password1', 'password2')
		}),
	)

	search_fields = ('email', 'username')

	ordering = ('is_active', 'is_online', 'email_verified')

	filter_horizontal = ()


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', )

	list_filter = ('name', )
	
	fieldsets = ((None, {'fields': ('name', )}), )
	
	add_fieldsets = (
		(None, {
			'classes': ('wide', ),
			'fields': ('name', )}
		),
	)
	
	search_fields = ('name', )
	
	ordering = ('name', )	


class ProductAdmin(admin.ModelAdmin):
	list_display = (
		'title', 'category',
		'publisher', 'price')
	
	list_filter = ('category', 'author', 'title')
	
	fieldsets = (
		(None, {
			'fields': (
				'publisher', 'category',
				'labels', 'opinions',
				'title', 'description',
				'price', 'author',
				'page_count', 'isbn',
				'contents', 'age_category',
				'url_name', 'average_rating',
				'rating_count', 'cover_img',
				'pdf_file', 'epub_file', 
				'mobi_file', 'published_at',
				'updated_at', 'demo_file')
		}),
	)

	readonly_fields = (
		'published_at', 'updated_at',
		'pdf_file', 'mobi_file',
		'epub_file', 'age_category',
		'price', 'rating_count',
		'average_rating', 'cover_img',
		'isbn', 'contents', 'page_count',
		'url_name', 'author',
		'publisher', 'demo_file')

	add_fieldsets = (
		(None, {
			'fields': (
				'publisher', 'category',
				'labels', 'opinions',
				'title', 'description',
				'price', 'author',
				'page_count', 'isbn',
				'contents', 'age_category',
				'url_name', 'epub_file', 
				'pdf_file', 'mobi_file')
		})
	)

	search_fields = (
		'category', 'author',
		'title', 'price',
		'author', 'publisher')
	
	ordering = (
		'category', 'author',
		'price', 'published_at')


class FileAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (
				'uuid', 'uploaded_at',
				'size', 'path',
				'extension')
		}),
	)

	readonly_fields = (
		'uploaded_at', 'size', 
		'extension', 'uuid',
		'path')


class SharedCartAdmin(admin.ModelAdmin):
	list_display = ('code', 'shared_at')

	fieldsets = (
		(None, {
			'fields': ('code', 'shared_at',
					   'cart')
		}),
	)
	
	readonly_fields = ('code', 'shared_at', 'cart')


class ProductLabelAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('name', 'color')
		}),
	)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(SharedCart, SharedCartAdmin)
admin.site.register(ProductLabel, ProductLabelAdmin)

admin.site.unregister(Group)