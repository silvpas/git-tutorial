#!/usr/bin/env python
"""Test cattery.py file."""

import unittest

from . import cattery


class TestCattery(unittest.TestCase):
    """Test Cattery class."""

    def setUp(self):
        self.cattery = cattery.Cattery()

    # add_cats

    def test__add_cats__succeeds(self):
        """It should successfully add cats."""
        self.cattery.add_cats(["Fluffy", "Snookums"])
        assert self.cattery.cats == ["Fluffy", "Snookums"]
        assert self.cattery.num_cats == 2

    # remove_cat

    def test__remove_cat__succeeds(self):
        """It should remove a cat."""
        self.cattery.add_cats(["Fluffy", "Junior"])
        self.cattery.remove_cat("Fluffy")
        assert self.cattery.cats == ["Junior"]
        assert self.cattery.num_cats == 1

    def test__remove_cat__no_cats__fails(self):
        """It should fail to remove non-existent cats."""
        with self.assertRaises(cattery.CatNotFound):
            self.cattery.remove_cat("Fluffles")

    def test__remove_cat__cat_not_in_cattery__fails(self):
        """It should fail to remove cats not in the cattery."""
        self.cattery.add_cats(["Fluffy"])
        with self.assertRaises(cattery.CatNotFound):
            self.cattery.remove_cat("Snookums")

if __name__ == '__main__':
    unittest.main()
