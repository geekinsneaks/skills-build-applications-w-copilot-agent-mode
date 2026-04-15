from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', team=marvel)
        steve = User.objects.create_user(username='captain', email='steve@marvel.com', password='password', team=marvel)
        bruce = User.objects.create_user(username='hulk', email='bruce@marvel.com', password='password', team=marvel)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', team=dc)
        bruce_dc = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', team=dc)
        diana = User.objects.create_user(username='wonderwoman', email='diana@dc.com', password='password', team=dc)

        # Create Workouts
        run = Workout.objects.create(name='Running', description='Run 5km')
        swim = Workout.objects.create(name='Swimming', description='Swim 1km')
        lift = Workout.objects.create(name='Weight Lifting', description='Lift 100kg')

        # Create Activities
        Activity.objects.create(user=tony, workout=run, duration=30)
        Activity.objects.create(user=steve, workout=swim, duration=45)
        Activity.objects.create(user=bruce, workout=lift, duration=60)
        Activity.objects.create(user=clark, workout=run, duration=25)
        Activity.objects.create(user=bruce_dc, workout=swim, duration=40)
        Activity.objects.create(user=diana, workout=lift, duration=55)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=300)
        Leaderboard.objects.create(team=dc, points=280)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
