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

class TestUpdateAll(unittest.TestCase):

    def test_block(self):
        """A cluster of three living cells in an L-shaped pattern should produce a forth living cell (creating a block), then remain stable."""
        field = life.GameOfLife(10, 10)
        field.update_state((2,2), True)
        field.update_state((2,3), True)
        field.update_state((3,3), True)
        expected_result = (True, True, True, True)
        for i in range(10):
            field.update_all()
            actual_result = (field.grid[2][2], field.grid[2][3], field.grid[3][2], field.grid[3][3])
            self.assertEqual(actual_result, expected_result)
    
    def test_loaf(self):
        """The loaf structure should be stable."""
        field = life.GameOfLife(10, 10)
        field.update_state((2,1), True)
        field.update_state((3,2), True)
        field.update_state((4,3), True)
        field.update_state((1,2), True)
        field.update_state((1,3), True)
        field.update_state((2,4), True)
        field.update_state((3,4), True)
        expected_result = field.living_cells.copy()
        for i in range(10):
            field.update_all()
            self.assertEqual(sorted(field.living_cells), sorted(expected_result))
    
    def test_glider(self):
        """The glider structure should move across the field."""
        field = life.GameOfLife(20, 40)
        field.update_state((3,3), True)
        field.update_state((4,3), True)
        field.update_state((5,3), True)
        field.update_state((5,2), True)
        field.update_state((4,1), True)
        expected_results = (
            ((4,4), (4,3), (3,3), (5,3), (3,2), (4,1), (5,2)),
            ((4,4), (4,3), (5,4), (3,3), (5,3), (3,2), (4,1), (5,2)),
            ((4,4), (4,3), (5,4), (4,2), (3,3), (5,3), (3,2), (6,3), (4,1), (5,2)),
            ((4,4), (4,3), (5,4), (6,4), (4,2), (3,3), (5,3), (3,2), (6,3), (4,1), (5,2))
        )
        for i in range(4):
            field.update_all()
            self.assertEqual(sorted(field.living_cells), sorted(expected_results[i]))

if __name__ == "__main__":
    unittest.main()
