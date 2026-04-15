from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=30)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_workout(self):
        self.assertEqual(self.activity.workout, self.workout)

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)
