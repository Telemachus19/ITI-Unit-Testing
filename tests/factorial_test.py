import random
from src.factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_five():
    assert factorial(5) == 120

def test_factorial_random_int():
    n = random.randint(3,20);
    assert factorial(n) == factorial(n-1)*n

def test_factorial_negative():
    assert factorial(-3) == None

def test_factorial_fraction():
    assert factorial(1.5) == None

def test_factorial_boolean():
    assert factorial(False) == None

def test_factorial_string():
    assert factorial("abc") == None

