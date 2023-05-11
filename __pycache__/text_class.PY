import unittest
#from class import Person

class TextClass(unittest.TestCase):
    def setUp(self) -> None:
        personn = person('Maru Koch', '26-08-1985', 45000)

    def test_capitalize(self):
        self.assertEqual(self.person.capitaliize(), 'Maru Koch')


    def tearDown(self) -> None:
        return super().tearDown()