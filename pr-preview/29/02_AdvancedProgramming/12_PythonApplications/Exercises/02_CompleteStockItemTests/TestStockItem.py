# Exercise 12.2b Test Stock Item
#
# Uses the unittest package to provide a complete set of tests for StockItem


import unittest

import StockItem


class TestStockItem(unittest.TestCase):
    def test_init(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        self.assertEqual(item.stock_ref, "Test")
        self.assertEqual(item.price, 10)
        self.assertEqual(item.stock_level, 0)
        self.assertEqual(item.tags, "test:tag")

    def test_str(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        expected_str = """Stock Reference: Test
Price: 10
Stock level: 0
Tags: test:tag"""
        self.assertEqual(str(item), expected_str)

    def test_add_stock(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        item.add_stock(10)
        self.assertEqual(item.stock_level, 10)

    def test_add_stock_greater_than_maximum_raises_exception(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        with self.assertRaises(Exception):
            item.add_stock(StockItem.StockItem.max_stock_add + 1)

    def test_add_negative_stock_raises_exception(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        with self.assertRaises(Exception):
            item.add_stock(-1)

    def test_sell_stock(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        item.add_stock(10)
        item.sell_stock(2)
        self.assertEqual(item.stock_level, 8)

    def test_sell_zero_stock_raises_exception(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        item.add_stock(10)
        with self.assertRaises(Exception):
            item.sell_stock(0)

    def test_sell_negative_stock_raises_exception(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        item.add_stock(10)
        with self.assertRaises(Exception):
            item.sell_stock(-1)

    def test_sell_stock_greater_than_stock_level_raises_exception(self):
        item = StockItem.StockItem(stock_ref="Test", price=10, tags="test:tag")
        with self.assertRaises(Exception):
            item.sell_stock(1)


unittest.main(verbosity=2)
