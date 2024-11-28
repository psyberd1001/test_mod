from unittest import TestCase
import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('<NAME>')
        for i in range(10):
            runner.walk()
            runner_distance = runner.distance
        self.assertEqual(runner_distance, 50)

    def test_run(self):
        runner1 = Runner('<NAME1>')
        for i in range(10):
            runner1.run()
            runner1_distance = runner1.distance
        self.assertEqual(runner1_distance, 100)

    def test_challenge(self):
        runner2 = Runner('<NAME2>')
        runner3 = Runner('<NAME3>')
        for i in range(10):
            runner2.run()
            runner2_distance = runner2.distance
        for i in range(10):
            runner3.walk()
            runner3_distance = runner3.distance
        self.assertNotEqual(runner2_distance, runner3_distance)

if __name__ == '__main__':
    unittest.main()