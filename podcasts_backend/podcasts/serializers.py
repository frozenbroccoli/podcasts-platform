from rest_framework import serializers


class PodcastSearchSerializer(serializers.Serializer):
    """
    Serializer for the PodcastSearch API view.
    """
    collectionId = serializers.IntegerField()
    collectionName = serializers.CharField()
    artistName = serializers.CharField()
    trackTimeMillis = serializers.IntegerField(required=False)
    trackCount = serializers.IntegerField()
    thumbnailSmall = serializers.URLField(source='artworkUrl100')
    thumbnailLarge = serializers.URLField(source='artworkUrl600')
    genres = serializers.ListField()
    primaryGenreName = serializers.CharField()
    collectionViewUrl = serializers.URLField()
    releaseDate = serializers.DateTimeField()


class PodcastsSearchQueriesSerializer(serializers.Serializer):
    """
    Serializer for podcasts
    """
    query = serializers.CharField()
    ordering = serializers.ChoiceField(
        choices=['newest', 'oldest', 'mostTracks', 'leastTracks'],
        required=False
    )
    attr = serializers.ChoiceField(
        choices=[
            'titleTerm',
            'languageTerm',
            'authorTerm',
            'genreIndex',
            'artistTerm',
            'ratingIndex',
            'keywordsTerm',
            'descriptionTerm'
        ],
        required=False
    )
    limit = serializers.IntegerField(
        min_value=1,
        max_value=200,
        default=50
    )


class PodcastEpisodesQueriesSerializer(serializers.Serializer):
    collectionId = serializers.IntegerField()
    limit = serializers.IntegerField(
        min_value=1,
        max_value=200,
        default=50
    )


class PodcastInfoSerializer(serializers.Serializer):
    artistName = serializers.CharField()
    collectionName = serializers.CharField()
    thumbnail = serializers.URLField(source='artworkUrl600')
    collectionId = serializers.IntegerField()
    kind = serializers.CharField()
    trackCount = serializers.IntegerField()


class EpisodesSerializer(serializers.Serializer):
    trackId = serializers.IntegerField()
    trackName = serializers.CharField()
    trackTimeMillis = serializers.IntegerField()
    episodeUrl = serializers.URLField()
    releaseDate = serializers.DateTimeField()
    description = serializers.CharField()
    thumbnail = serializers.URLField(source='artworkUrl600')
