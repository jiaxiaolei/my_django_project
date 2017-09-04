# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

from django.test import TestCase
from django.test.client import Client


class SendviewsTestCase(TestCase):

    def test_http(self):
        c = Client()
        ret = c.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(ret.status_code, 200)

    def test_http2(self):
        c = Client()
        ret = c.get('/customer/details/')
        self.assertEqual(ret.status_code, 200)
