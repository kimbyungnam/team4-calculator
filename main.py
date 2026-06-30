import pytest

class Calc:
    # 이 곳에 코드를 작성
    def getSum(self, a, b):
        return a + b

    def getZegop(self, a):
        return a * a

    def getMinus(self, a,b):
        return a -b


# 테스트 케이스 작성
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

    assert ret == 1
