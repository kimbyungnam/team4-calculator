import pytest


class Calc:
    # 이 곳에 코드를 작성
    def getZegop(self, a):
        return a * a

    def getMinus(self, a,b):
        return a -b


# 테스트 케이스 작성
def test_sample():
    assert 1 == 1
    assert Calc().getMinus(1,2) ==-1
    

def test_getZegop():
    sut = Calc()

    ret = sut.getZegop(2)

    assert ret == 4
