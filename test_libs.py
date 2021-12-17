from unittest import TestCase
from libs import Bones, Square, GameField


class TestLibs(TestCase):
    def test_throw(self):
        b = Bones()
        self.assertIn(b.throw(), [(i, x) for i in range(1, 7) for x in range(1, 7)])

    def test_has_interception_single(self):
        field = GameField(50, 50)
        self.assertEqual(field.hasInterceptionSingle(Square(0, 0, 2, 2, 0), Square(3, 3, 4, 4, 0)), False)

    def test_has_interception_single_2(self):
        field = GameField(50, 50)
        self.assertEqual(field.hasInterceptionSingle(Square(0, 0, 3, 3, 0), Square(2, 2, 4, 4, 0)), True)

    def test_getState_inField(self):
        field = GameField(50, 50)
        self.assertEqual(field.getState(49,49), 0)

    def test_getState_outOfField(self):
        field = GameField(50, 50)
        self.assertEqual(field.getState(50,50), None)

    def test_has_interception_any(self):
        field = GameField(50, 50)
        field.addSquare(0, 0, 2, 2, 0)
        self.assertEqual(field.hasInterceptionAny(Square(3, 3, 4, 4, 0)), False)

    def test_has_interception_any_2(self):
        field = GameField(50, 50)
        field.addSquare(0, 0, 3, 3, 0)
        self.assertEqual(field.hasInterceptionAny(Square(2, 2, 4, 4, 0)), True)

