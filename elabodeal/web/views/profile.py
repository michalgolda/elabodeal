from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from elabodeal.web.views import BaseView
from elabodeal.models import (
    User,
    Product,
    Publisher
)


def check_publisher_existing(method):
    def wrapper(request, username, *args, **kwargs):
        existing_user = User.objects.filter(username=username).first()

        if not existing_user: 
            return redirect('web:index')

        if not existing_user.is_publisher: 
            return redirect('web:index')

        existing_publisher = existing_user.publisher

        return method(request, existing_publisher, *args, **kwargs)
    return wrapper


def check_whether_user_already_following(method):
    def wrapper(request, existing_publisher, *args, **kwargs):
        user_already_following = False
        
        if request.user.is_authenticated:
            user_already_following = request.user.already_following(
                existing_publisher.id
            )

        return method(request, existing_publisher, user_already_following)
    return wrapper


def aggregate_product_categories(products):
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


def aggregate_product_languages(products):
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


def generate_chart_data(chart_name, queryset):
    aggregation_functions = {
        'languages': aggregate_product_languages,
        'categories': aggregate_product_categories
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


class ProfileView(BaseView):

    @method_decorator([
        check_publisher_existing,
        check_whether_user_already_following
    ])
    def get(self, request, existing_publisher, user_already_following):
        products = Product.objects.all()
        followers = existing_publisher.followers.count()

        charts = {
            'languages': generate_chart_data(
                'languages',
                products
            ),
            'categories': generate_chart_data(
                'categories',
                products
            )
        }

        context = {
            'banner': {
                'text': None,
                'product': None
            },
            'application_data': {
                'charts': charts,
                'userAlreadyFollowing': user_already_following
            },
            'followers': followers,
            'products': products,
            'publisher': existing_publisher,
            'products_count': len(products),
            'user_already_following': user_already_following
        }

        return self.respond('profile.html', request, context)