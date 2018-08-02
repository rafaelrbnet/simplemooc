from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test.client import Client

from simplemooc.courses.models import Course

class IndexCourseTestCase(TestCase):

    def test_index_status_code(self):
        client = Client()
        response = client.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self):
        client = Client()
        response = client.get(reverse('courses:index'))
        self.assertTemplateUsed(response, 'courses/index.html')
        self.assertTemplateUsed(response, 'base.html')


class ContactCourseTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_details_status_code(self):
        client = Client()
        response = client.get(reverse('courses:details', args=[self.course.slug]))
        self.assertEqual(response.status_code, 200)

    def test_details_template_used(self):
        client = Client()
        response = client.get(reverse('courses:details', args=[self.course.slug]))
        self.assertTemplateUsed(response, 'courses/details.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_contact_form_error(self):
        data = {'name': 'Fulado de tal', 'email': '', 'mensagem': ''}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'mensagem', 'Este campo é obrigatório.')

    def test_contact_form_sucess(self):
        data = {'name': 'Fulado de tal', 'email': 'admin@admin.com', 'mensagem': 'Teste'}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].to, [settings.CONTACT_EMAIL])

class EnrollmentCourseTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_enrollment_status_code_login(self):
        User = get_user_model()
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.client.login(username='test_user', password='test_user')

        
        response = self.client.get(reverse('courses:enrollment', args=[self.course.slug]))
        self.assertEqual(response.status_code, 200)

    def test_enrollment_status_code_logout(self):
        client = Client()
        response = client.get(reverse('courses:enrollment', args=[self.course.slug]))
        self.assertEqual(response.status_code, 302)