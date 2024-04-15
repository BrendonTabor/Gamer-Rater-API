from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from raterapi.models import Game


class GameView(ViewSet):
    """Game view set"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        user = request.auth.user

        game = Game()
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.year_released = request.data["yearReleased"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.estimated_time_to_play = request.data["estimatedTimeToPlay"]
        game.age_recommendation = request.data["ageRecommendation"]
        game.user = user
        game.image_url = request.data["imageUrl"]

        try:
            game.save()
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class UserGameSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "user_name",
        )


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = Game
        fields = (
            "id",
            "title",
            "description",
            "designer",
            "year_released",
            "number_of_players",
            "estimated_time_to_play",
            "age_recommendation",
            "user",
            "image_url",
        )
