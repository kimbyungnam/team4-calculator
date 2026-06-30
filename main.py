import pytest


class Calc:
    def get_Minus(self, a,b):
        return a -b


# 테스트 케이스 작성
def test_sample():
    assert 1 == 1
    pytest.fail()
