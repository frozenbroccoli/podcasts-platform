import datetime
import operator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
import requests
from . import serializers


base_url = 'https://itunes.apple.com'


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

    Query parameters:
    query: The query term.
    ordering: The ordering key. Possible values are
        newest, oldest, mostTracks, leastTracks. Orders
        by popular by default.
    attr: The attribute to search for. Possible values
        are titleTerm, languageTerm, authorTerm, genreIndex,
        artistTerm, ratingIndex, keywordsTerm, descriptionTerm.
    limit: The number of search results. 50 by default. Max 200.
    """

    def get(self, request, *args, **kwargs):
        query_serializer = serializers.PodcastsSearchQueriesSerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        query, ordering, attr = [query_serializer.validated_data.get(key, '') for key in ('query', 'ordering', 'attr',)]
        limit = query_serializer.validated_data.get('limit', 50)

        def get_release_date(result: dict) -> datetime.date:
            """
            Get the date object of the release date.

            :param result: One search result dict with a "releaseDate" key.
            :return: Python date object of value of the "releaseDate" key.
            """
            return datetime.datetime.fromisoformat(result['releaseDate'])

        if query:
            url = f'{base_url}/search?term={query}&media=podcast&attribute={attr}&limit={limit}'
            results = requests.get(url, timeout=10).json()['results']
            match ordering:
                case 'newest':
                    response = sorted(results, reverse=True, key=get_release_date)
                case 'oldest':
                    response = sorted(results, reverse=False, key=get_release_date)
                case 'mostTracks':
                    response = sorted(results, reverse=True, key=operator.itemgetter('trackCount'))
                case 'leastTracks':
                    response = sorted(results, reverse=False, key=operator.itemgetter('trackCount'))
                case _:
                    response = results
            serializer = serializers.PodcastSearchSerializer(response, many=True)
            paginator = PageNumberPagination()
            paginated_response = paginator.paginate_queryset(serializer.data, request)
            return paginator.get_paginated_response(paginated_response)

        return Response(status=status.HTTP_200_OK)


class PodcastEpisodesView(APIView):
    """
    Episode lookup view.
    """
    def get(self, request, *args, **kwargs):
        query_serializer = serializers.PodcastLookupQueriesSerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        collection_id = query_serializer.validated_data.get('collectionId', '')
        limit = query_serializer.validated_data.get('limit', 50)

        if collection_id:
            url = f'{base_url}/lookup?id={collection_id}&media=podcast&entity=podcastEpisode&limit={limit}'
            results = requests.get(url, timeout=10).json()['results']
            paginator = PageNumberPagination()
            paginated_response = paginator.paginate_queryset(results, request)
            return paginator.get_paginated_response(paginated_response)

        return Response(status=status.HTTP_200_OK)
