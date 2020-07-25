from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from elabodeal.models import User, Category, Product


class UserAdmin(BaseUserAdmin):
	list_display = ('email', 'username', 'is_staff')
	list_filter = ('is_superuser', 'email', 'last_login')
	fieldsets = (
		(None, {'fields': (
			'email', 'username', 'password', 'email_verified', 'email_verified_at',
			'is_superuser', 'is_staff', 'is_active', 'is_seller', 'last_login',
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


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	fieldsets = (
		(None, {'fields': ('name',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('name',)}
		),
	)
	search_fields = ('name',)
	ordering = ('name',)
	filter_horizontal = ()

class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'author', 'user')
	list_filter = ('category', 'author')
	fieldsets = (
		(None, {'fields': ('title', 'description', 'price', 'category', 'cover_img', 'pdf', 'epub', 'mobi', 'author', 'user', 'page_count', 'isbn')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('title', 'description', 'price', 'page_count', 'isbn', 'category', 'cover_img_url', 'author')}
		),
	)
	search_fields = ('category', 'author')
	ordering = ('category', 'author')
	filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.unregister(Group)