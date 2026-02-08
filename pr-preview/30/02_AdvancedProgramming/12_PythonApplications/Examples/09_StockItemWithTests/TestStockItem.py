# Example 12.9b Test Stock Item
#
# Uses the unittest package to test the tag based StockItem implementation


import unittest

import StockItem


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


unittest.main(verbosity=2)
