# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_contact_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        data = {'name': 'fulano', 'email': 'fulano@fulano.com', 'message': 'Ok'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(mail.outbox), 1)
        self.assertTrue('success' in response.context)

    def test_contact_error(self):
        data = {'name': 'fulano', 'email': 'fulano@fulano.com'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(mail.outbox), 0)
        self.assertTrue('success' not in response.context)
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')
