import datetime
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
        ordering = request.query_params.get('ordering', '')
        limit = request.query_params.get('limit', 50)

        def get_release_date(result: dict) -> datetime.date:
            """
            Get the date object of the release date.

            :param result: One search result dict with a "releaseDate" key.
            :return: Python date object of value of the "releaseDate" key.
            """
            return datetime.datetime.fromisoformat(result['releaseDate'])

        if query:
            url = f'https://itunes.apple.com/search?term={query}&media=podcast&limit={limit}'
            results = requests.get(url).json()['results']
            match ordering:
                case 'newest':
                    response = sorted(results, reverse=True, key=get_release_date)
                case 'oldest':
                    response = sorted(results, reverse=False, key=get_release_date)
                case _:
                    response = results
            paginator = PageNumberPagination()
            paginated_response = paginator.paginate_queryset(response, request)
            return paginator.get_paginated_response(paginated_response)
        return Response(status=status.HTTP_200_OK)
