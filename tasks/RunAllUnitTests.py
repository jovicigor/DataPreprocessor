import unittest

if __name__ == "__main__":
    testsuite = unittest.TestLoader().discover('../tests', pattern="Test*.py")
    unittest.TextTestRunner(verbosity=1).run(testsuite)
