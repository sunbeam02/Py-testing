import unittest
from func import avg
class FUnctionTest(unittest.TestCase):
    def test_avg(self):
        self.assertTrue(avg(1,2,3,4),2)

    def test_avg_2(self):
        with self.assertRaises(TypeError):
            self.assertTrue(avg(1,2,3,'4'),2)

    def test_avg_3(self):
        with self.assertRaises(TypeError):
            self.assertTrue(avg(1,2,3,float),2)

    def test_avg_4(self):
        self.assertTrue(isinstance(avg(1, 2, 3), int))

    

if __name__ =='__main__':
    unittest.main()

    
    