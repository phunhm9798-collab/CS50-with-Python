from twttr import shorten


def main():
    test_shorten()


def test_shorten():
    assert shorten('phu') == 'ph'
    assert shorten('PHu') == 'PH'
    assert shorten('3205Abcde') == '3205bcd'
    assert shorten(',NGUYEN.') == ',NGYN.'
