from django.test import TestCase
from django.contrib.gis.geos import Point
from django.urls import reverse
from .models import Place
from django.contrib.auth.models import User


class PlaceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Place.objects.create(author=user, title='Home', location=Point(5, 23))

    def test_title_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_location_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_location_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        place = Place.objects.get(id=1)
        max_length = place._meta.get_field('title').max_length 
        self.assertEquals(max_length, 100)


class ListPlaceViewTest(TestCase):
    @classmethod
    def setUpData(cls):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        number_of_places = 5
        for i in range(number_of_places):
            Place.objects.create(author=user, title='john %s' % i, location=Point(i,i*2))

    def test_url_exists(self):
        first_resp = self.client.get('/')
        second_resp = self.client.get('/home/')
        self.assertEqual(first_resp.status_code, 302)
        self.assertEqual(second_resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 302)


class LoginTest(TestCase):
    @classmethod
    def setUp(self):
        test_user1 = User.objects.create_user('john', 'john@mail.com', 'johnpass').save()
        test_user1 = User.objects.create_user('mark', 'mark@mail.com', 'markpass').save()
        test_user1 = User.objects.create_user('sandy', 'sandy@mail.com', 'sandypass').save()

        test_place1 = Place.objects.create(author=test_user1, title='user1title',location=Point(10,2))
        test_place2 = Place.objects.create(author=test_user1, title='user1title',location=Point(10,2))
        test_place3 = Place.objects.create(author=test_user1, title='user1title',location=Point(10,2))
    
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='john', password='johnpass')
        resp = self.client.get(reverse('home'))

        self.assertEqual(str(resp.context['user']), 'john')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
