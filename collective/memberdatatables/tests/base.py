import unittest2 as unittest
from collective.memberdatatables import testing


class UnitTestCase(unittest.TestCase):
    pass


class IntegrationTestCase(unittest.TestCase):

    layer = testing.INTEGRATION


class FunctionalTestCase(unittest.TestCase):

    layer = testing.FUNCTIONAL
