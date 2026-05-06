from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Run', user='test@example.com', team='Test Team')
        self.assertIn('Run', str(activity))

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='test@example.com', team='Test Team', points=10)
        self.assertIn('test@example.com', str(lb))

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', user='test@example.com')
        self.assertIn('Pushups', str(workout))
