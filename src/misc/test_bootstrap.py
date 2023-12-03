import unittest
from .bootstrap import bootstrap

class BootstrapTest(unittest.TestCase):
    def test_bootstrap_sum(self):
        @bootstrap
        def SUM(n):
            if n == 0: yield 0
            yield n + (yield SUM(n-1))
        self.assertEqual(SUM(100000), 5000050000)
    def test_fib(self):
        DP = {}
        @bootstrap
        def fib(n):
            if n <= 2:
                yield 1
            if n in DP:
                yield DP[n]
            res = (yield fib(n-1)) + (yield fib(n-2))
            DP[n] = res
            yield res

        self.assertEqual(fib(1000), 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)

if __name__ == '__main__':
    unittest.main()