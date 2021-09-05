from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from elabodeal.web.views import BaseView
from elabodeal.models import (
    User,
    Product,
    Publisher
)


class ProfileView(BaseView):
    @staticmethod
    def _check_publisher_existing(username):
        existing_user = User.objects.filter(username=username).first()

        if not existing_user or not existing_user.is_publisher: 
            return False

        existing_publisher = existing_user.publisher

        return existing_publisher

    @staticmethod
    def _check_whether_current_user_already_following(current_user, publisher_id):
        following = False

        if current_user.is_authenticated:
            following = current_user.already_following(publisher_id)

        return following

    @staticmethod
    def _check_whether_current_user_is_profile_owner(current_user, username):
        current_user_is_profile_owner = False

        if current_user.is_authenticated:
            if current_user.username == username:
                current_user_is_profile_owner = True

        return current_user_is_profile_owner

    @staticmethod
    def _aggregate_product_categories(products):
        aggregations = {}

        for product in products:
            label = product.category.name

            if not label in aggregations:
                background_color = '#000'
                count = products.filter(category__name=label).count()

                aggregations[label] = {
                    'count': count,
                    'background_color': background_color
                }

        return aggregations

    @staticmethod
    def _aggregate_product_languages(products):
        aggregations = {}

        for product in products:
            label = product.language.name
            
            if not label in aggregations:
                background_color = '#ff0011'
                count = products.filter(language__name=label).count()

                aggregations[label] = {
                    'count': count,
                    'background_color': background_color
                }

        return aggregations

    def _generate_chart_data(self, chart_name, queryset):
        aggregation_functions = {
            'languages': self._aggregate_product_languages,
            'categories': self._aggregate_product_categories
        }

        aggregations = aggregation_functions[chart_name](queryset)

        data = []
        labels = []
        background_colors = []

        for label in aggregations.keys():
            count, background_color = aggregations[label].values()

            data.append(count)
            labels.append(label)
            background_colors.append(background_color)

        data = {
            'labels': labels,
            'datasets': [{
                'data': data,
                'backgroundColor': background_colors
            }]
        }

        return data

    def _serialize_profile(self, existing_publisher):
        bio = existing_publisher.bio
        avatar_img = existing_publisher.avatar_img
        banner_img = existing_publisher.banner_img
        banner_text = existing_publisher.banner_text
        who_you_are = existing_publisher.who_you_are
        banner_product = existing_publisher.banner_product

        if avatar_img:
            avatar_img = { 'path': avatar_img.path }

        if banner_img:
            banner_img = { 'path': banner_img.path }

        if banner_product:
            banner_product = {
                'id': banner_product.id,
                'cover_img': { 
                    'path': banner_product.cover_img.path
                }
            }

        return {
            'bio': bio,
            'avatar_img': avatar_img,
            'banner_img': banner_img,
            'banner_text': banner_text,
            'who_you_are': who_you_are,
            'banner_product': banner_product
        }

    def _serialize_products(self, products):
        return list(
            map(
                lambda product: {
                    'id': product.id,
                    'title': product.title
                },
                products
            )
        )

    def get(self, request, username):
        existing_publisher = self._check_publisher_existing(username)

        if not existing_publisher: return redirect('web:index')

        current_user = request.user

        current_user_already_following = self._check_whether_current_user_already_following(
            current_user,
            existing_publisher.id
        )

        current_user_is_profile_owner = self._check_whether_current_user_is_profile_owner(
            current_user,
            username
        )

        products = Product.objects.all()
        products_count = len(products)

        followers_count = existing_publisher.followers.count()

        charts = {
            'languages': self._generate_chart_data('languages', products),
            'categories': self._generate_chart_data('categories', products)
        }

        application_data = {}

        application_data['charts'] = charts
        application_data['products'] = self._serialize_products(products)
        application_data['profile'] = self._serialize_profile(existing_publisher) 
        application_data['current_user_already_following'] = current_user_already_following

        context = {}
        
        context['application_data'] = application_data

        context['existing_publisher'] = existing_publisher

        context['followers_count'] = followers_count

        context['products'] = products
        context['products_count'] = products_count
       
        context['current_user_is_profile_owner'] = current_user_is_profile_owner
        context['current_user_already_following'] = current_user_already_following

        return self.respond('profile.html', request, context)