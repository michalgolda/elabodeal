import unittest

from django.test import TestCase

from rest_framework.test import APITestCase as BaseAPITestCase


class BaseTestCase(unittest.TestCase):
	pass


class WebTestCase(BaseTestCase, TestCase):
	pass


class APITestCase(BaseTestCase, BaseAPITestCase):
	pass