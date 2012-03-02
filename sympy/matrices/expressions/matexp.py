from matexpr import MatrixExpr, ShapeError, Identity
from sympy import Pow, S, Basic
from sympy.core.sympify import _sympify

class MatExp(MatrixExpr, Pow):

    def __new__(cls, b, e):
        assert e.is_Matrix
        e = _sympify(e)
        if e.is_Identity or b is S.Zero:
            return b
        elif not e.is_square:
            raise ShapeError("Exp of non-square matrix %s"%b)
        elif e.is_ZeroMatrix:
            return b
        else:
            return MatrixExpr.__new__(cls, b, e)

    @property
    def shape(self):
        return self.args[1].shape

    def _entry(self, i, j):
        if self.exp.is_Integer:
            # Make an explicity MatMul out of the MatPow
            return Basic.__new__(MatMul,
                    *[self.base for k in range(self.exp)])._entry(i, j)

from matmul import MatMul
