from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from elabodeal.models import (
	User, 
	File,
	Cart,
	Product,
	Category, 
	Publisher,
	SharedCart,
	ProductGroup,
	ProductLanguage,
	ProductPremiere,
	PurchasedProduct,
	VerificationCode
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	list_display = [
		'id', 
		'email',
		'username', 
		'is_staff',
		'is_publisher'
	]

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'publisher',
				'username',
				'email',
				'email_verified',
				'email_verified_at',
				'is_staff',
				'is_superuser',
				'newsletter',
				'created_at',
				'updated_at'
			]
		}]
	]

	add_fieldsets = [
		[None, {
			'fields': [
				'email',
				'username',
				'password1',
				'password2'
			]
		}]
	]

	readonly_fields = [
		'id',
		'publisher',
		'is_staff',
		'newsletter',
		'created_at',
		'updated_at',
		'is_superuser',
		'email_verified',
		'email_verified_at'
	]

	search_fields = ['id', 'username', 'email']

	list_filter = ['is_superuser', 'is_staff']
	
	filter_horizontal = []

	@admin.display(boolean=True)
	def is_publisher(self, obj):
		return obj.is_publisher

	def get_readonly_fields(self, request, obj=None):
		if not obj: return self.readonly_fields

		self.readonly_fields.append('email')
		self.readonly_fields.append('username')

		return self.readonly_fields


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	list_display = ['id', 'full_name']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'first_name',
				'last_name',
				'account_number',
				'swift',
				'created_at',
				'updated_at'
			]
		}]
	]

	add_fieldsets = [
		[None, {
			'fields': [
				'first_name',
				'last_name',
				'swift',
				'account_number'
			]
		}]
	]

	readonly_fields = [
		'id',
		'created_at',
		'updated_at'
	]

	search_fields = [
		'id',
		'user__id',
		'last_name',
		'first_name',
		'user__email',
		'account_number',
		'user__username'
	]

	def full_name(self, obj):
		return obj.full_name

	def get_readonly_fields(self, request, obj=None):
		if not obj: return self.readonly_fields

		self.readonly_fields.append('first_name')
		self.readonly_fields.append('last_name')
		self.readonly_fields.append('account_number')
		self.readonly_fields.append('swift')

		return self.readonly_fields


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
	list_display = ['id', 'publisher']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'publisher',
				'created_at',
				'updated_at'
			]
		}]
	]

	add_fieldsets = [
		[None, {
			'fields': ['publisher']
		}]
	]

	readonly_fields = [
		'id', 
		'created_at', 
		'updated_at'
	]

	search_fields = [
		'id',
		'publisher__id',
		'publisher__first_name',
		'publisher__last_name'
	]

	def get_readonly_fields(self, request, obj=None):
		if not obj: return self.readonly_fields

		self.readonly_fields.append('publisher')

		return self.readonly_fields


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

	fieldsets = [
		[None, {
			'fields': ['id', 'name']
		}]
	]

	add_fieldsets = [
		[None, {
			'fields': ['name']
		}]
	]

	readonly_fields = ['id']

	search_fields = ['id', 'name']


@admin.register(ProductLanguage)
class ProductLanguageAdmin(admin.ModelAdmin):
	list_display = ['id', 'code', 'name']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'code',
				'name'
			]
		}]
	]

	add_fieldsets = [
		[None, {
			'fields': [
				'code',
				'name'
			]
		}]
	]

	readonly_fields = ['id']

	search_fields = ['id', 'code', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'price']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'publisher',
				'group',
				'category',
				'language',
				'title',
				'description',
				'contents',
				'author',
				'isbn',
				'price',
				'copies',
				'published_year',
				'page_count',
				'cover_img',
				'premiere',
				'other_images',
				'files',
				'age_category',
				'average_rating',
				'rating_count'
			]
		}]
	]

	readonly_fields = [
		'id',
		'average_rating',
		'rating_count',
		'created_at',
		'updated_at'
	]

	search_fields = [
		'id',
		'isbn',
		'title',
		'author',
		'description'
	]

	def get_readonly_fields(self, request, obj=None):
		if not obj: return self.readonly_fields

		self.readonly_fields.append('isbn')
		self.readonly_fields.append('group')
		self.readonly_fields.append('title')
		self.readonly_fields.append('files')
		self.readonly_fields.append('price')
		self.readonly_fields.append('author')
		self.readonly_fields.append('copies')
		self.readonly_fields.append('category')
		self.readonly_fields.append('language')
		self.readonly_fields.append('premiere')
		self.readonly_fields.append('contents')
		self.readonly_fields.append('publisher')
		self.readonly_fields.append('cover_img')
		self.readonly_fields.append('page_count')
		self.readonly_fields.append('description')
		self.readonly_fields.append('other_images')
		self.readonly_fields.append('age_category')
		self.readonly_fields.append('published_year')

		return self.readonly_fields


@admin.register(ProductPremiere)
class ProductPremiereAdmin(admin.ModelAdmin):
	list_display = ['id', 'datetime']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'datetime',
				'created_at',
				'updated_at'
			]
		}]
	]

	add_fieldsets = [
		[None, {
			'fields': ['datetime']
		}]
	]

	readonly_fields = [
		'id',
		'created_at',
		'updated_at'
	]

	def get_readonly_fields(self, request, obj=None):
		if not obj: return self.readonly_fields

		self.readonly_fields.append('datetime')

		return self.readonly_fields


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
	list_display = ['id', 'size', 'path', 'extension']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'size',
				'path',
				'type',
				'hash',
				'extension',
				'uploaded_at'
			]
		}]
	]

	readonly_fields = [
		'id',
		'size',
		'path',
		'type',
		'hash',
		'extension',
		'uploaded_at'
	]

	search_fields = ['id']


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
	list_display = ['id', 'email', 'code']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'code',
				'email',
				'expiration_at',
				'created_at'
			]
		}]
	]

	readonly_fields = [
		'id',
		'code',
		'email',
		'created_at',
		'expiration_at'
	]

	search_fields = ['id']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'products_count']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'user',
				'title',
				'description',
				'products',
				'created_at',
				'updated_at'
			]
		}]
	]

	readonly_fields = [
		'id',
		'user',
		'title',
		'products',
		'created_at',
		'updated_at',
		'description'
	]

	search_fields = ['id']


@admin.register(PurchasedProduct)
class PurchasedProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'product', 'has_rating']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'user',
				'rating',
				'product',
				'has_rating',
				'purchased_at'
			]
		}]
	]

	readonly_fields = [
		'id',
		'user',
		'rating',
		'product',
		'has_rating',
		'purchased_at'
	]

	search_fields = ['id']


@admin.register(SharedCart)
class SharedCartAdmin(admin.ModelAdmin):
	list_display = ['id', 'cart', 'code']

	fieldsets = [
		[None, {
			'fields': [
				'id',
				'cart',
				'code',
				'created_at'
			]
		}]
	]

	readonly_fields = [
		'id',
		'cart',
		'code',
		'created_at'
	]

	search_fields = ['id']


# The group model is not used to.
admin.site.unregister(Group)

# Site settings
admin.site.site_header = _('Elabodeal - Panel administracyjny')