import unittest
import flatten

class TestFlatten(unittest.TestCase):

    def test_flatten_simple(self):
        self.assertEqual(flatten.flatten([1, 2, [3]]), [1, 2, 3], "Should be [1, 2, 3]")

    def test_flatten_empty(self):
        self.assertEqual(flatten.flatten([]), [], "Should be []")
    
    def test_flatten_single(self):
        self.assertEqual(flatten.flatten([1]), [1], "Should be [1]")
    
    def test_flatten_complicated(self):
        self.assertEqual(flatten.flatten([[1,2,[3]],4]), [1,2,3,4], "Should be [1,2,3,4]")

    def test_flatten_empty_list(self):
        self.assertEqual(flatten.flatten([[1,2,[3,[]]],4]), [1,2,3,4], "Should be [1,2,3,4]")



if __name__ == '__main__':
    unittest.main()