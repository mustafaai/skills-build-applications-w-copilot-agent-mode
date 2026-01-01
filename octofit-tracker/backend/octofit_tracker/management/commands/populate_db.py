from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        # Delete in order: Leaderboard, Activity, Workout, Team, then User (excluding superuser)
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        # Workaround for djongo SQLDecodeError: delete users one by one
        for user in User.objects.all():
            if not user.is_superuser and user.id is not None:
                user.delete()

        # Create users (superheroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
        ]
        marvel_users = [User.objects.create_user(**hero, password='password') for hero in marvel_heroes]
        dc_users = [User.objects.create_user(**hero, password='password') for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Team Marvel')
        for user in marvel_users:
            marvel_team.members.add(user)
        dc_team = Team.objects.create(name='Team DC')
        for user in dc_users:
            dc_team.members.add(user)

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard', duration=60)
        workout2 = Workout.objects.create(name='Agility Boost', description='Agility and speed drills', difficulty='Medium', duration=45)
        workout3 = Workout.objects.create(name='Endurance Run', description='Long distance running', difficulty='Easy', duration=30)

        # Create activities
        activities = [
            Activity.objects.create(user=marvel_users[0], activity_type='Strength', duration=60, calories_burned=500, date=timezone.now()),
            Activity.objects.create(user=marvel_users[1], activity_type='Agility', duration=45, calories_burned=350, date=timezone.now()),
            Activity.objects.create(user=dc_users[0], activity_type='Endurance', duration=30, calories_burned=200, date=timezone.now()),
            Activity.objects.create(user=dc_users[1], activity_type='Strength', duration=60, calories_burned=550, date=timezone.now()),
        ]

        # Create leaderboard entries
        Leaderboard.objects.create(user=marvel_users[0], score=1000, rank=1)
        Leaderboard.objects.create(user=marvel_users[1], score=900, rank=2)
        Leaderboard.objects.create(user=dc_users[0], score=850, rank=3)
        Leaderboard.objects.create(user=dc_users[1], score=800, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
