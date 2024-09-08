from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
import requests


class EchoView(APIView):
    """
    Echo back the request body.
    """

    def get(self, request, *args, **kwargs):
        return Response(
            data={
                "headers": request.headers,
                "args": request.query_params,
                "url": request.build_absolute_uri()
            },
            content_type='application/json; charset=utf-8',
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        return Response(
            data={
                "headers": request.headers,
                "form": request.data,
                "args": request.query_params,
            },
            content_type='application/json; charset=utf-8',
            status=status.HTTP_200_OK
        )


class PodcastSearchView(APIView):
    """
    List view for Apple podcasts search results.
    """
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        if query:
            url = f'https://itunes.apple.com/search?term={query}&media=podcast&limit=200'
            response = requests.get(url).json()['results']
            paginator = PageNumberPagination()
            paginated_response = paginator.paginate_queryset(response, request)
            return paginator.get_paginated_response(paginated_response)
        return Response(status=status.HTTP_200_OK)
