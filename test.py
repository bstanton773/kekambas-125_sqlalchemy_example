from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase(TestCase):
    def test_example_one(self):
      self.assertEqual(solution(1,5),2)
    def test_fun_lil_zero(self):
       self.assertEqual(solution(3,3),0)
    def test_one(self):
       self.assertEqual(solution(1,2),1)
    def test_no_caps_no_sec_arg(self):
       self.assertEqual(solution(10,77),23)

if __name__ == "__main__":
   main()