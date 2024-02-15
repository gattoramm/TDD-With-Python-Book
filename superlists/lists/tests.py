from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class SmokeTest(TestCase):
    """Тест на токсичность"""

    def test_bad_maths(self):
        """Тест: неправильные математические расчеты"""
        self.assertEquals(1 + 1, 3)
