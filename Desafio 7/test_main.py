import os
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from django.test import TestCase
from api.models import User, Event, Group, Agent
from main import (
    get_active_users,
    get_amount_users,
    get_admin_users,
    get_all_debug_events,
    get_all_critical_events_by_user,
    get_all_agents_by_user,
    get_all_events_by_group
)


class TestChallenge10(TestCase):
    def setUp(self) -> None:
        admin = Group.objects.create(name="admin")
        operators = Group.objects.create(name="operators")

        alexandre = User.objects.create(name="alexandre", email="alexandre@gmail.com", password="gmmggtes12")
        jose = User.objects.create(name="jose", email="jose@gmail.com", password="gmmggtes12")
        aline = User.objects.create(name="aline", email="aline@gmail.com", password="gmmggtes12")
        kenny = User.objects.create(name="kenny", email="kenny@gmail.com", password="gmmggtes12", last_login=(datetime.today() - timedelta(days=12)))
        john = User.objects.create(name="john", email="john@gmail.com", password="gmmggtes12")
        mario = User.objects.create(name="mario", email="mario@gmail.com", password="gmmggtes12", last_login=(datetime.today() - timedelta(days=12)))
        maria = User.objects.create(name="maria", email="maria@gmail.com", password="gmmggtes12")
        roberto = User.objects.create(name="roberto", email="roberto@gmail.com", password="gmmggtes12", last_login=(datetime.today() - timedelta(days=12)))
        fabio = User.objects.create(name="fabio", email="fabio@gmail.com", password="gmmggtes12")
        denis = User.objects.create(name="denis", email="denis@gmail.com", password="gmmggtes12")

        alexandre.group.set([admin])
        jose.group.set([admin])
        aline.group.set([admin])
        kenny.group.set([admin])
        john.group.set([admin])
        mario.group.set([admin])
        maria.group.set([operators])
        roberto.group.set([operators])
        fabio.group.set([operators])
        denis.group.set([operators])

        agent_linux = Agent.objects.create(name='linux-server', address='10.0.34.15', status=True, env='production', version='1.1.1', user=alexandre)
        agent_mac = Agent.objects.create(name='mac-server', address='10.0.34.123', status=True, env='production', version='1.1.2', user=john)

        Event.objects.create(level='critical', data=datetime.today(), agent=agent_linux, arquivado=False)
        Event.objects.create(level='information', data=datetime.today(), agent=agent_mac, arquivado=False)

    def test_1(self):
        users = get_active_users()
        assert isinstance(users[0], User)

    def test_2(self):
        amount = get_amount_users()
        self.assertEqual(amount, 10)

    def test_3(self):
        admins = get_admin_users()
        self.assertEqual(admins.count(), 6)

    def test_4(self):
        users = get_all_debug_events()
        self.assertEqual(
            users.count(),
            0
        )

    def test_5(self):
        agent = Agent.objects.filter(name='linux-server').first()
        users = get_all_critical_events_by_user(agent)
        self.assertEqual(
            users.count(),
           1
        )

    def test_6(self):
        users = get_all_agents_by_user('alexandre')
        self.assertEqual(
            users.count(),
            1
        )

    def test_7(self):
        users = get_all_events_by_group()
        self.assertEqual(
            users.count(),
            1
        )
