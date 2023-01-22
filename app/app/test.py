from django.test import SimpleTestCase
from . import calculator

class testCalculator(SimpleTestCase):
    def test_dicreaseNumbers(self):
        self.assertEqual(calculator.dicreaseTwoNumbers(10,5),5)


