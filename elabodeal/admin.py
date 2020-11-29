from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from elabodeal.models import User, Category, Product


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
				'is_staff')
		}),
	)

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
		'publisher', 'category',
		'title', 'price')
	
	list_filter = ('category', 'author','title')
	
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
				'updated_at')
		}),
	)

	exclude = ('published_at', 'updated_at')

	search_fields = (
		'category', 'author',
		'title', 'price',
		'author', 'publisher')
	
	ordering = (
		'category', 'author',
		'price', 'published_at')


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.unregister(Group)