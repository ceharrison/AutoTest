import unittest
from Package1.Logintests import LoginScenarios

# Get all tests from LoginScenarios
tc = unittest.TestLoader().loadTestsFromTestCase(LoginScenarios)

# Creating test suite
currentTestSuite=unittest.TestSuite([tc])

unittest.TextTestRunner(verbosity=2).run(currentTestSuite)