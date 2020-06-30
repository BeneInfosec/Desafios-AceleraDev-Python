import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from django.test import TestCase
from api.models import User, Agent, Group, Event, GroupUser


class TestChallenge9(TestCase):

    def setUp(self):
        user = User.objects.create(name="Jose", email="jose@gmail.com", password="xxxxxxxxxxxxxxxxxxxxxxx")
        agent = Agent.objects.create(name="Machine1", address="192.168.1.1", status=True, env="prod", version="1.1.1")
        group = Group.objects.create(name="Admin")
        GroupUser.objects.create(user=user, group=group)
        Event.objects.create(level="CRITICAL", data="django.core.exceptions.ValidationError", user=user, agent=agent, arquivado=False)

    def test_1(self):
        user = User.objects.get(name="Jose")
        self.assertEqual(user.email, "jose@gmail.com")

    def test_2(self):
        agent = Agent.objects.get(name="Machine1")
        self.assertEqual(agent.name, "Machine1")

    def test_3(self):
        group = Group.objects.get(name="Admin")
        self.assertEqual(group.name, "Admin")

    def test_4(self):
        event = Event.objects.get(level="CRITICAL")
        self.assertEqual(event.level, "CRITICAL")
