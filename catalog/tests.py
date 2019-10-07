from django.test import TestCase
from account import models as amod
from django.contrib.auth import logout
from django.contrib.auth import models as pmod
# Create your tests here.

class SiteTests(TestCase):
    fixtures = ['account.yaml']

    def test_user_get(self):
        u1 = amod.User.objects.get(id=2)
        self.assertEqual(u1.first_name, 'Homer', msg="Name should be 'Homer'")
      

    def test_user_create(self):
        u = amod.User()
        u.first_name = 'Harry'
        u.last_name = 'Potter'
        u.username = 'harry'
        u.set_password('muggles')
        u.birthdate = '1990-02-01'
        u.email = 'harry@potter.com'
        u.save()
        u2 = amod.User.objects.get(username=u.username)
        self.assertEqual(u.first_name, u2.first_name, msg='Names do not match')

    def test_user_login(self):
        credentials = {
            'username': 'caleb',
            'password': 'password' 
        }
        response = self.client.post('/account/login/', credentials)
        request = response.wsgi_request
        self.assertTrue(request.user.is_authenticated, msg='User should have authenticated')
        self.assertEqual(request.user.id, amod.User.objects.get(username='caleb').id, msg='User should have been caleb')
        self.assertEqual(response.status_code, 302, msg='User not redirected')


    def test_user_logout(self):
        credentials = {
            'username': 'caleb',
            'password': 'password' 
        }
        response = self.client.post('/account/login/', credentials)
        request = response.wsgi_request
        self.assertTrue(request.user.is_authenticated, msg='User should have authenticated')
        logout(request)
        self.assertFalse(request.user.is_authenticated, msg='User was not logged out')

    def test_group_permissions(self):
        g = pmod.Group()
        g.name = 'Testers'
        g.save()
        g2 = pmod.Group.objects.get(name=g.name)
        self.assertEqual(g.name, g2.name, msg='Group names do not match')
        p = pmod.Permission()
        p.codename = 'test_stuff'
        p.name = 'Test all the stuff'
        p.content_type = pmod.Permission.objects.get(codename='add_user').content_type
        p.save()
        p2 = pmod.Permission.objects.get(codename=p.codename)
        self.assertEqual(p.name, p2.name, msg='Permission codenames do not match')
        # g.permissions.add(pmod.Permission.objects.get(codename=p.codename))
        # g.save()
        # g = pmod.Group.objects.get(name=g.name)
        # self.assertEqual

    def test_user_group(self):
        u = amod.User.objects.get(username='mctester')
        u.groups.add(pmod.Group.objects.get(name='Tellers'))
        morgan = amod.User.objects.get(username='morgan')
        self.assertEqual(u.get_all_permissions(), morgan.get_all_permissions(), msg='Wrong permissions')

    def test_user_changePW(self):
        u = amod.User()
        u.first_name = 'Harry'
        u.last_name = 'Potter'
        u.username = 'harry'
        u.password = amod.User.objects.get(username='mctester').password
        u.birthdate = '1990-02-01'
        u.email = 'harry@potter.com'
        u.save()
        new = amod.User.objects.get(username='mctester')
        new.set_password('newPassword')
        new.save()
        self.assertNotEqual(new.password, u.password, msg='Password was unchanged')