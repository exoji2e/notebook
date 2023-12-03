import unittest
from . import primes

class TestPrimes(unittest.TestCase):
    def testIsPrime(self):
        self.assertEqual(False, primes.isPrime(1))
        self.assertEqual(True, primes.isPrime(2))
        self.assertEqual(True, primes.isPrime(3))
        self.assertEqual(False, primes.isPrime(4))
        self.assertEqual(True, primes.isPrime(10**9 + 7))
        self.assertEqual(True, primes.isPrime(10**9 + 9))

    def testPrimesBelow(self):
        prms = primes.getPrimesBelow(20)
        self.assertEqual(prms, [2, 3, 5, 7, 11, 13, 17, 19])
        prms = set(primes.getPrimesBelow(1000))
        for i in range(1000):
            self.assertEqual(i in prms, primes.isPrime(i))

    def testPrimesFrom(self):
        self.assertEqual(primes.getPrimesFrom(10**9, 2), [10**9 + 7, 10**9 + 9])

if __name__ == '__main__':
    unittest.main()