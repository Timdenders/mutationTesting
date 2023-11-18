import pytest
from polynomial import Polynomial  # Import the Polynomial class from your module


def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]


def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""

    # Additional test cases
    poly4 = Polynomial([])
    assert str(poly4) == "0" or str(poly4) == ""
    
    poly5 = Polynomial([1, 3, 5])
    assert str(poly5) == "1x^2 + 3x + 5"

    poly6 = Polynomial([2, 4, 6])  # 2x^2 + 4x + 6
    assert str(poly6) == "2x^2 + 4x + 6"

    poly7 = Polynomial([-1, 2, 0, 4])  # -1x^3 + 2x^2 + 4
    assert str(poly7) == "-1x^3 + 2x^2 + 4"

    poly = Polynomial([5])  # 5
    assert str(poly) == "5"

    poly = Polynomial([-1, 3])  # -1x + 3
    assert str(poly) == "-1x + 3"

    poly = Polynomial([4])  # 4
    assert str(poly) == "4"

    poly = Polynomial([-1, 3, 0])  # -1x^2 + 3x
    assert str(poly) == "-1x^2 + 3x"

    poly = Polynomial([-1, 0, 4])  # -1x^2 + 4
    assert str(poly) == "-1x^2 + 4"

    poly = Polynomial([2, 3, 0])  # 2x^2 + 3x
    assert str(poly) == "2x^2 + 3x"


def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

    # Additional test cases
    poly1 = Polynomial([3])  # 3
    poly2 = Polynomial([2, 0, 0, 4])  # 2x^3 + 4
    result = poly1 + poly2
    assert result.coefficients == [2, 0, 0, 7]  # 2x^3 + 7

    poly1 = Polynomial([-2, 1])  # -2x + 1
    poly2 = Polynomial([5, 0, 6])  # 5x^2 + 6
    result = poly1 + poly2
    assert result.coefficients == [5, -2, 7]  # 5x^2 - 2x + 7

    poly1 = Polynomial([4, 2])  # 4x + 2
    poly2 = Polynomial([-1, 3])  # -1x + 3
    result = poly1 + poly2
    assert result.coefficients == [3, 5]  # 3x + 5


def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3, -1, 3]

    # Additional cases
    poly1 = Polynomial([2, 5])  # 2x + 5
    poly2 = Polynomial([3, 0, 1])  # 3x^2 + 1
    result = poly1 - poly2
    assert result.coefficients == [-3, 2, 4]  # -3x^2 + 2x + 4

    poly1 = Polynomial([1, 3])  # 1x + 3
    poly2 = Polynomial([0, 0])  # 0
    result = poly1 - poly2
    assert result.coefficients == [1, 3]  # 1x + 3

    poly1 = Polynomial([1, 3])  # 1x + 3
    poly2 = Polynomial([0, 0])  # 0
    result = poly1 - poly2
    assert result.coefficients == [1, 3]  # 1x + 3

    poly1 = Polynomial([-2, 5])  # -2x + 5
    poly2 = Polynomial([1, 4])  # 1x + 4
    result = poly1 - poly2
    assert result.coefficients == [-3, 1]  # -3x + 1



def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]


def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6


def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0 ** 0.5) < 1e-6


def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6


def test_evaluate():
    poly = Polynomial([1, -2, 3])  # x^2 - 2x + 3

    result_1 = poly.evaluate(1)
    assert result_1 == 2  # 1^2 - 2*1 + 3 = 2

    result_0 = poly.evaluate(0)
    assert result_0 == 3  # 0^2 - 2*0 + 3 = 3

    result_minus_1 = poly.evaluate(-1)
    assert result_minus_1 == 6  # (-1)^2 - 2*(-1) + 3 = 6


def test_find_root_bisection():
    poly = Polynomial([-1, 0, 0, 1])  # -x^3 + 1
    root = poly.find_root_bisection(0, 2)
    assert abs(root - 1) < 1e-6  # Expected root is 1 within the interval [0, 2]
