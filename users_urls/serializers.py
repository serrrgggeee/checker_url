from users_urls.models import Urls
from rest_framework import serializers


class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = ['id', 'user', 'url', 'active_time']