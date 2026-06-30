import pytest

class Calc:
    # 이 곳에 코드를 작성
    def getSum(self, a, b):
        return a + b

    def getZegop(self, a):
        return a * a

    def getMinus(self, a,b):
        return a -b
      
    def getGop(self,a,b):
        return a*b

    def getDivide(self, a, b):
        return a / b

    def getSumSum(self, a, b, c):
        return a + b + c

# 테스트 케이스 작성
def test_getGop():
    # arrange
    sut = Calc()

    ret = sut.getGop(3,2)

    assert ret == 6

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


def test_getMinus():
    sut = Calc()
    
    ret = sut.getMinus(1,2)
    
    assert ret == -1


def test_getZegop():
    sut = Calc()

    ret = sut.getZegop(2)

    assert ret == 4
    

def test_getSum():
    sut = Calc()

    ret = sut.getSum(4, 8)

    assert ret == 12

