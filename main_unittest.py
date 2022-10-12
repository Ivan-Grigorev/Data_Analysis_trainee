import unittest
from unittest.mock import MagicMock, patch


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__name__':
    unittest.main()


class TestApp(unittest.TestCase):

    def setUp(self):
        print("Setup code. Let's create a new db mock if there is no")
        if not hasattr(self, 'db'):
            self.db = {}

    def tearDown(self):
        print("Clear after test")
        self.db.clear()

    def test_db_update(self):
        new_row = {'a': 1}
        self.db.update(new_row)
        self.assertEqual(self.db, new_row)

    def test_db_pop(self):
        new_row = {'a': 1}
        self.db.update(new_row)
        popped_row = self.db.pop('a')
        self.assertEqual(popped_row, new_row['a'])


if __name__ == '__main__':
    unittest.main()

# thing = ProductionClass()
# thing.method = MagicMock(return_value=3)
# thing.method(3, 4, 5, key='value')
#
# thing.method.assert_called_with(3, 4, 5, key='value')
#
# with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
#     thing = ProductionClass()
#     thing.method(1, 2, 3)
#
# mock_method.assert_called_once_with(1, 2, 3)
#
#
# @patch('module.ClassName2')
# @patch('module.ClassName1')
# def test(MockClass1, MockClass2):
#     module.ClassName1()
#     module.ClassName2()
#     assert MockClass1 is module.ClassName1
#     assert MockClass2 is module.ClassName2
#     assert MockClass1.called
#     assert MockClass2.called
#
#
# test()
