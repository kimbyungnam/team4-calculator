import pytest

class Calc:
    # 이 곳에 코드를 작성
    def getSum(self, a, b):
        return a + b
    pass


# 테스트 케이스 작성
def test_sample():
    c = Calc()

    assert c.getSum(4, 8) == 1