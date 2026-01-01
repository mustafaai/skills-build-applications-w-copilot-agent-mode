from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


# Team Serializer
class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'created_at']


# Activity Serializer
class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'calories_burned', 'date']


# Workout Serializer
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration']


# Leaderboard Serializer
class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score', 'rank']
