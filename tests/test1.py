import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator


    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_adding_success_multiply(self):
        assert self.calculator.multiply(self, 2, 3) == 6

    def test_adding_success_subtraction(self):
        assert self.calculator.subtraction(self, 4, 1) == 3

    def test_adding_success_division(self):
        assert self.calculator.division(self, 4, 2) == 2


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 1, 0)


    def teardown(self):
        print('выполнение метода TearDown')