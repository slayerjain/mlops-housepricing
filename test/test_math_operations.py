import pytest
from src.utils.math_operations import *  # Importing all from the source module, add_numbers, divide_numbers, multiply_numbers, subtract_numbers
def test_dummy():
	assert True
# Test generated using Keploy
def test_add_numbers_positive_integers():
    result = add_numbers(3, 5)
    assert result == 8, "Expected 3 + 5 to equal 8"
# Test generated using Keploy
def test_subtract_numbers_negative_result():
    result = subtract_numbers(3, 5)
    assert result == -2, "Expected 3 - 5 to equal -2"
# Test generated using Keploy
def test_multiply_numbers_with_zero():
    result = multiply_numbers(7, 0)
    assert result == 0, "Expected 7 * 0 to equal 0"
# Test generated using Keploy
def test_divide_numbers_zero_division():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide_numbers(10, 0)
# Test generated using Keploy
def test_divide_numbers_positive_integers():
    result = divide_numbers(10, 2)
    assert result == 5, "Expected 10 / 2 to equal 5"