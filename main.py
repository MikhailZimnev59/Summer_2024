import pytest, unittest
def should_skip():
    return True
class Test(unittest.TestCase):
    def a(self):
        self.assertEqual(1+1, 2)
    def test_b(self):
        self.assertEqual(1+2, 3)

@pytest.mark.skip
def test_c(self):
    self.assertEqual(1+3, 4)
@pytest.mark.skipif('should_skip')
def test_d(self):
    self.assertEqual(1+4, 5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
