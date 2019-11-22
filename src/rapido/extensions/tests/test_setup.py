# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from rapido.extensions.testing import RAPIDO_PLONE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that rapido.extensions is properly installed."""

    layer = RAPIDO_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rapido.extensions is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('rapido.extensions'))

    def test_uninstall(self):
        """Test if rapido.extensions is cleanly uninstalled."""
        self.installer.uninstallProducts(['rapido.extensions'])
        self.assertFalse(self.installer.isProductInstalled('rapido.extensions'))
