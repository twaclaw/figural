import numpy as np

import figural.pentagonal as pn
import figural.triangular as tr


class TestTriangular:
    def test_triangular(self):
        assert tr.ith(1) == 1
        assert tr.ith(5) == 15
        assert tr.ith(10) == 55

    def test_is_triangular(self):
        assert tr.is_triangular(6)
        assert not tr.is_triangular(11)
        assert np.all(tr.is_triangular(tr.arange(1000000)))

    # TODO add tests for drawing functions


class TestPentagonal:
    def test_pentagonal(self):
        assert pn.ith(1) == 1
        assert pn.ith(5) == 35
        assert pn.ith(10) == 145

    def test_is_triangular(self):
        assert pn.is_pentagonal(1)
        assert not pn.is_pentagonal(11)
        assert np.all(pn.is_pentagonal(pn.arange(1000000)))

    # TODO add tests for drawing functions
