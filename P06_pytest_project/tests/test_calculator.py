
from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected


class TestCal:
    def test(self):
        # arrange
        a = 4
        b = 1
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3
        assert result == expected

class TestCalcul:
    def test_fsd(self):
        # arrange
        a = 4
        b = 1
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 4
        assert result == expected

class TestCalcuwgwefl:
    def test_fsd(self):
        # arrange
        a = 4
        b = 1
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4
        assert result == expected


class TestCalculbg:
    def test_fsd(self):
        # arrange
        a = 4
        b = 0
        cal = Calculator()

        # act
        with pytest.raises(ZeroDivisionError, match = "Division by zero error"):
            cal.divide(a, b)
        
       
    
        

       
        

