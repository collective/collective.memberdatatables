import unittest2 as unittest
from collective.memberdatatables.tests import base
from plone.app import testing


class TestIntegration(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """
    def setUp(self):
        base.IntegrationTestCase.setUp(self)
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        testing.login(self.portal, testing.TEST_USER_NAME)
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
