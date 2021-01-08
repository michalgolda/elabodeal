import unittest

from django.test import TestCase


class BaseTestCase(unittest.TestCase):
	pass


class WebTestCase(BaseTestCase, TestCase):
	pass
