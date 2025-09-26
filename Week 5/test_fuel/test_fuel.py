from fuel import convert, gauge
import pytest


def test_convert():
    assert convert('1/4') == 25
    assert convert('3/4') == 75
    assert convert('1/2') == 50
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('1.5/10')
    with pytest.raises(ValueError):
        convert('-1/10')


def test_gauge():
    assert gauge(25) == '25%'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
