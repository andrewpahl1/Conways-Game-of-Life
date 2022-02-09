import life
import unittest

class TestGetNeighbors(unittest.TestCase):
    
    def test_get_neighbors1(self):
        field = life.GameOfLife(5, 5)
        expected_result = ((0,1), (1,0), (1,1))
        actual_result = field.get_neighbors((0, 0))
        self.assertEqual(sorted(actual_result), sorted(expected_result))
        
    def test_get_neighbors2(self):
        field = life.GameOfLife(5, 5)
        expected_result = ((3,2), (3,4), (2,3), (2,4), (2,2), (4,3), (4,4), (4,2))
        actual_result = field.get_neighbors((3, 3))
        self.assertEqual(sorted(actual_result), sorted(expected_result))
    
    def test_get_neighbors3(self):
        field = life.GameOfLife(98, 98)
        expected_result = ((97, 96), (96, 97), (96, 96))
        actual_result = field.get_neighbors((97, 97))
        self.assertEqual(sorted(actual_result), sorted(expected_result))

if __name__ == "__main__":
    unittest.main()