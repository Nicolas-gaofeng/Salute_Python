# coding:utf-8


def divide(num1, num2):
    """除法"""
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0

    print num1 / num2


divide(100, 50)
divide("a", 50)
