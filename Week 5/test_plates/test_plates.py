from plates import is_valid


def test_length():
    assert is_valid('OUTATIME') == False
    assert is_valid('OUTTIME') == False
    assert is_valid('CS50') == True


def test_center():
    assert is_valid('PN35') == True
    assert is_valid('CS50P') == False
    assert is_valid('CS50') == True


def test_alphabet():
    assert is_valid('50CS') == False
    assert is_valid('32PH') == False
    assert is_valid('PN35') == True


def test_start():
    assert is_valid('PN05') == False
    assert is_valid('PN35') == True
    assert is_valid('pn35') == True


def test_symbols():
    assert is_valid('HELLO, WORLD') == False
    assert is_valid('Hello!') == False
    assert is_valid('GOODBYE, WORLD') == False
