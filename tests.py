import life
import unittest

class TestGetNeighbors(unittest.TestCase):
    
    def test_get_neighbors1(self):
        field = life.GameOfLife(5, 5)
        expected_result = (field.grid[0][1], field.grid[1][0], field.grid[1][1])
        actual_result = field.grid[0][0].neighbors
        self.assertEqual(sorted(actual_result), sorted(expected_result))
        
    def test_get_neighbors2(self):
        field = life.GameOfLife(5, 5)
        expected_result = (
            field.grid[3][2], field.grid[3][4], field.grid[2][3],
            field.grid[2][4], field.grid[2][2], field.grid[4][3],
            field.grid[4][4], field.grid[4][2]
        )
        actual_result = field.grid[3][3].neighbors
        self.assertEqual(sorted(actual_result), sorted(expected_result))
    
    def test_get_neighbors3(self):
        field = life.GameOfLife(98, 98)
        expected_result = (field.grid[97][96], field.grid[96][97], field.grid[96][96])
        actual_result = field.grid[97][97].neighbors
        self.assertEqual(sorted(actual_result), sorted(expected_result))

if __name__ == "__main__":
    unittest.main()