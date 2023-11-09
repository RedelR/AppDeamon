import pytest

from src.moving_average import MovingAverage

@pytest.fixture
def my_average():
    return MovingAverage()

def test_constructor(my_average):
    assert type(my_average._values) == list
    assert len(my_average._values) == 0
    assert type(my_average._filled) == int
    assert my_average._filled == 0
    assert my_average._max_items == 10


def test_add_value(my_average):
    my_average.add_value(10.0)
    assert len(my_average._values) == 1
    assert my_average._filled == 1
    assert my_average.calculate() == 10.0
    my_average.add_value(20.0)
    assert my_average._filled == 2
    assert my_average.calculate() == 15.0
    #-- now fill up  without shifting
    for i in range (1, 9):
        my_average.add_value(10.0 * float(i + 2))
    assert my_average._filled == 10
    assert my_average.calculate() == 55.0
    #- now shift for the first time
    my_average.add_value(10.0)
    assert my_average._filled == 10.0
    assert my_average.calculate() == 55.0


def test_calculate(my_average):
    assert my_average.calculate() == 0.0
    assert my_average.calculate(2,3) == 0.0
    assert my_average.calculate(0,0) == 0.0
    assert my_average.calculate(-1,-3) == 0.0
    assert my_average.calculate(3,2) == 0.0
    assert my_average.calculate(2,3) == 0.0
    my_average.add_value(10.0)
    assert my_average.calculate() == 10.0
    assert my_average.calculate(0) == 10.0
    assert my_average.calculate(0,9) == 10.0
    assert my_average.calculate(1) == 0.0

    my_average.add_value(20.0)
    assert my_average.calculate() == 15.0
    assert my_average.calculate(0,9) == 15.0
    assert my_average.calculate(2) == 0.0
    assert my_average.calculate(1) == 20.0
    assert my_average.calculate(1,0) == 0.0
    assert my_average.calculate(1,9) == 20.0

    my_average.add_value(30.0)
    assert my_average.calculate() == 20.0
    assert my_average.calculate(0,9) == 20.0
    assert my_average.calculate(2) == 30.0
    assert my_average.calculate(1) == 25.0


#    for i in range (1, 11):
#        my_average.add_value(10.0 * float(i + 2))
#    assert len(my_average._values) == 1
