from rest_framework.views import APIView
from rest_framework.response import Response


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
            content_type='application/json; charset=utf-8'
        )

    def post(self, request, *args, **kwargs):
        return Response(
            data={
                "headers": request.headers,
                "form": request.data,
                "args": request.query_params,
            },
            content_type='application/json; charset=utf-8'
        )
