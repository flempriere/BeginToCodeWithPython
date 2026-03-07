"""
Example 12.10b RunTests

Runs `unittest` based unit tests on the Fashion Shop Classes
"""

import unittest

from Data import StockItem


class TestStockItem(unittest.TestCase):
    def test_init(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        self.assertEqual(item.stock_ref, "Test")
        self.assertEqual(item.price, 10)
        self.assertEqual(item.stock_level, 0)
        self.assertEqual(item.tags, "test:tag")

    def test_always_fails(self):
        self.assertEqual(1, 0)

    def test_add_negative_stock_raises_exception(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        with self.assertRaises(Exception):
            item.add_stock(-1)

    def test_add_and_sell_stock(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        item.add_stock(10)
        self.assertEqual(item.stock_level, 10)
        item.sell_stock(2)
        self.assertEqual(item.stock_level, 8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
