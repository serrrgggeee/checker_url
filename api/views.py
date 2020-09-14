from users_urls.models import Urls
from users_urls.serializers import UrlsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import action

import datetime

from django.contrib.auth.models import User


class UrlCheckerDetail(APIView):

    def get_object(self, pk):
      try:
        return Urls.objects.get(pk=pk)
      except Urls.DoesNotExist:
        raise Http404

    def list(self, request):
      queryset = Urls.objects.all()
      serializer = UserSerializer(queryset, many=True)
      return Response(serializer.data)

    def get(self, request, pk, format=None):
      url = self.get_object(pk)
      serializer = UrlsSerializer(url)
      return Response(serializer.data)

    def post(self, request, format=None):
      # curl -X POST -S -H 'Accept: application/json; indent=4 Content-TyContent-Type: application/json' -d "user=1&url=http://test.ru" http://127.0.0.1:8000/api/url_checker/add/
      now = datetime.datetime.now().time()
      request.data._mutable = True
      request.data.update({'active_time': now})
      serializer = UrlsSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UrlsSerializer

  # @action(detail=False)
  def list(self, request):
    print(111)
    time = datetime.datetime.now() - datetime.timedelta(minutes=15)
    # active_users = Urls.objects.filter(active_time__gte=time).distinct('user').order_by('-active_time')
    active_users = Urls.objects.filter(active_time__gte=time).order_by('-active_time')
    serializer = self.get_serializer(active_users, many=True)
    return Response(serializer.data)