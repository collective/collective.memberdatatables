from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

from plone.testing import z2


class Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.memberdatatables
        import collective.js.datatables
        self.loadZCML(package=collective.js.datatables)
        self.loadZCML(package=collective.memberdatatables)

#        z2.installProduct(app, 'collective.memberdatatables')

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'collective.memberdatatables:default')

#    def tearDownZope(self, app):
#        z2.uninstallProduct(app, 'collective.memberdatatables')


FIXTURE = Layer()
INTEGRATION = IntegrationTesting(
    bases=(FIXTURE,), name="collective.memberdatatables:Integration"
)
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                               name="collective.memberdatatables:Functional")

ROBOT = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, FIXTURE, z2.ZSERVER),
    name="collective.memberdatatables:Robot"
)
