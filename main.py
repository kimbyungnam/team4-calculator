import pytest


class Calc:
    def getGop(self,a,b):
        return a*b


def test_getGop():
    # arrange
    sut = Calc()

    ret = sut.getGop(3,2)

    assert ret == 6