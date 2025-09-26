from bank import value


def main():
    test_hello()
    test_h()
    test_others()


def test_hello():
    assert value('hello') == 0
    assert value('HELLO THERE') == 0


def test_h():
    assert value('hihihi') == 20
    assert value('hehehe') == 20


def test_others():
    assert value('Phu') == 100
