from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='member', password='pass')
        team = Team.objects.create(name='Team A')
        team.members.add(user)
        self.assertEqual(team.name, 'Team A')
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='active', password='pass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, calories_burned=200, date=timezone.now().date())
        self.assertEqual(activity.activity_type, 'Run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy', duration=10)
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username='leader', password='pass')
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
