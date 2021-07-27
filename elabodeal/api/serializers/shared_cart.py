from rest_framework import serializers
from elabodeal.models import SharedCart


class SharedCartSerializer(serializers.ModelSerializer):
    share_url_path = serializers.ReadOnlyField()

    class Meta:
        model = SharedCart
        fields = '__all__'