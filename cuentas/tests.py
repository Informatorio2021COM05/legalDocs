from .models import Escribano
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import EscribanoSignUpView, SignUpView


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
        username='will',
        email='will@email.com',
        password='testpass123',
        nombre='elnombre',
        apellido='elapellido',
        dni=1234,
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertEqual(user.nombre, 'elnombre')
        self.assertEqual(user.apellido, 'elapellido')
        self.assertEqual(user.dni, 1234)
        self.assertFalse(user.is_escribano)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
        username='superadmin',
        email='superadmin@email.com',
        password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)



class SignupTests(TestCase):
    def setUp(self):
        url = reverse('cuentas:signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/cuentas/signup/')
        self.assertEqual(
        view.func.__name__,
        SignUpView.as_view().__name__
        )