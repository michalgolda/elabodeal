from rest_framework import serializers
from elabodeal.models import SharedCart


class SharedCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = SharedCart
        fields = '__all__'