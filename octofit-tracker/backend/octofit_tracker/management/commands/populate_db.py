from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# MODELS (temporários para popular o banco, substitua por models.py depois)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user_email = models.EmailField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Limpa dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Usuários
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='123'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='123'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='123'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='123'),
        ]

        # Atividades
        Activity.objects.create(name='Corrida', user_email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(name='Natação', user_email='spiderman@marvel.com', team='Marvel')
        Activity.objects.create(name='Ciclismo', user_email='batman@dc.com', team='DC')
        Activity.objects.create(name='Yoga', user_email='wonderwoman@dc.com', team='DC')

        # Leaderboard
        Leaderboard.objects.create(user_email='ironman@marvel.com', team='Marvel', points=100)
        Leaderboard.objects.create(user_email='spiderman@marvel.com', team='Marvel', points=80)
        Leaderboard.objects.create(user_email='batman@dc.com', team='DC', points=90)
        Leaderboard.objects.create(user_email='wonderwoman@dc.com', team='DC', points=95)

        # Workouts
        Workout.objects.create(name='Treino de Força', description='Supino, Agachamento, Remada', user_email='ironman@marvel.com')
        Workout.objects.create(name='Treino de Resistência', description='Corrida longa distância', user_email='spiderman@marvel.com')
        Workout.objects.create(name='Treino de Velocidade', description='Sprints', user_email='batman@dc.com')
        Workout.objects.create(name='Treino de Flexibilidade', description='Alongamento e Yoga', user_email='wonderwoman@dc.com')

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
