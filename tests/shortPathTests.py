import unittest

from navigation.shortPath import astar

class TestAstar(unittest.TestCase):
    def test_valid_path(self):
        fire_station = (0, 0)
        destination = (3, 3)
        obstacles = {(2, 2)}
        path = astar(fire_station, destination, obstacles)
        expected_path = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3)]
        self.assertEqual(expected_path, path, "Valid path not found")

    def test_no_path(self):
        fire_station = (0, 0)
        destination = (3, 3)
        obstacles = {(0, 1), (1, 1), (2, 2), (3, 1)}
        path = astar(fire_station, destination, obstacles)
        self.assertIsNone(path, "Path should not exist")

    def same_start_and_end(self):
        fire_station = (0, 0)
        destination = (0, 0)
        obstacles = {(0, 1)}
        path = astar(fire_station, destination, obstacles)
        expected_path = [(0, 0)]
        self.assertEqual(expected_path, path, "Start and end are the same")

    def test_grid_out_of_bounds(self):
        fire_station = (0, 0)
        destination = (10, 10)
        obstacles = {(5, 5), (5, 6), (5, 7)}
        path = astar(fire_station, destination, obstacles)
        self.assertIsNone(path, "Path should exist on a larger grid")

    def test_grid_demo_path(self):
        fire_station = (0, 0)
        fire_1 = (2, 3)
        fire_2 = (3, 2)
        fire_3 = (1, 0)

        expected_path_1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)]
        path_station_to_fire_1 = astar(fire_station, fire_1)
        self.assertEquals(expected_path_1, path_station_to_fire_1)

        expected_path_2 = [(2, )]