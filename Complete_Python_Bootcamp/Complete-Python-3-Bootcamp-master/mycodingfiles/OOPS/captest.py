import unittest
import cap

class TestCap(unittest.TestCase):
    """docstring for TestCap."""

    def test_one_word(Self):
        text='python'
        result=cap.cap_text(text)
        Self.assertEqual(result,'Python')
if __name__ == '__main__':
    unittest.main()
