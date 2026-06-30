import pytest


class Calc:
    # 이 곳에 코드를 작성

    def getDivide(self, a, b):
        return a / b

    def getSumSum(self, a, b, c):
        return a + b + c


# 테스트 케이스 작성
def test_getDivide():
    calc = Calc()
    assert calc.getDivide(10, 2) == 5
    assert calc.getDivide(7, 2) == 3.5
    assert calc.getDivide(-6, 3) == -2


def test_getDivide_by_zero():
    calc = Calc()
    with pytest.raises(ZeroDivisionError):
        calc.getDivide(5, 0)


def test_getSumSum():
    calc = Calc()
    assert calc.getSumSum(1, 2, 3) == 6
    assert calc.getSumSum(0, 0, 0) == 0
    assert calc.getSumSum(-1, 2, -3) == -2
