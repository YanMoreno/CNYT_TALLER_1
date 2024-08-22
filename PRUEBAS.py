import unittest
import math
import FUNCIONES as lc

class TestCplx(unittest.TestCase):

    def test_cplxsum(self):
        suma = lc.sumacplx((3,4),(-4,6.7))
        self.assertAlmostEqual(suma,(-1,10.7))

    def test_restacplx(self):
        resta = lc.restacplx((3, 2), (-5,6.4))
        self.assertAlmostEqual(resta[0], 8)
        self.assertAlmostEqual(resta[1], -4.4)

    def test_multicplx(self):
        producto = lc.multicplx((4, 5), (-5, 5.8))
        self.assertAlmostEqual(producto[0], -49)
        self.assertAlmostEqual(producto[1], -1.8)

    def test_divcplx(self):
        division = lc.divcplx((3,8,2),(-7,5.5))
        self.assertAlmostEqual(division[0], 0)
        self.assertAlmostEqual(division[1], -1)

    def test_modulocplx(self):
        modulo = lc.modulocplx((3),(-6.7))
        self.assertAlmostEqual(modulo, 16)

    def test_conjugadocplx(self):
        conjugado = lc.conjugadocplx((3),(-7.2))
        self.assertAlmostEqual(conjugado[0], 3)
        self.assertAlmostEqual(conjugado[1], 7.2)

    def test_conversptoccplx(self):
        conversion = lc.conversptoccplx(2,-75)
        self.assertAlmostEqual(conversion[0], 1)
        self.assertAlmostEqual(conversion[1], -2)

    def test_conversctopcplx(self):
        conversion = lc.conversctopcplx((3*((3)**(1/2))),(3))
        self.assertAlmostEqual(conversion[0], 6)
        self.assertAlmostEqual(conversion[1], 30)

    def test_fasecplx(self):
        fase = lc.fasecplx((3),(-5.2))
        self.assertAlmostEqual(fase, 420)

        fase2 = lc.fasecplx(-1, -1)
        self.assertAlmostEqual(fase2, 225)

    def test_sumacplx_zero(self):
        suma = lc.sumacplx((0, 0), (0, 0))
        self.assertEqual(suma, (0, 0))

    def test_restacplx_same(self):
        resta = lc.restacplx((5, 5), (5, 5))
        self.assertEqual(resta, (0, 0))

    def test_multicplx_i(self):
        producto = lc.multicplx((2, 3), (0, 1))
        self.assertEqual(producto, (-3, 2))

    def test_divcplx_by_one(self):
        division = lc.divcplx((4, 5), (1, 0))
        self.assertEqual(division, (4, 5))

    def test_modulocplx_unit(self):
        modulo = lc.modulocplx(1, 0)
        self.assertEqual(modulo, 1)

    def test_conjugadocplx_pure_imaginary(self):
        conjugado = lc.conjugadocplx(0, 5)
        self.assertEqual(conjugado, (0, -5))

    def test_conversptoccplx_45_degrees(self):
        conversion = lc.conversptoccplx(math.sqrt(2), 45)
        self.assertAlmostEqual(conversion[0], 1)
        self.assertAlmostEqual(conversion[1], 1)

    def test_conversctopcplx_negative(self):
        conversion = lc.conversctopcplx(-1, -1)
        self.assertAlmostEqual(conversion[0],math.sqrt(2))
        self.assertAlmostEqual(conversion[1], 225)




if __name__ == '__main__':
    unittest.main()

