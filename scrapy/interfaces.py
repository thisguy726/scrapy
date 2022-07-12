from zope.interface import Interface


class ISpiderLoader(Interface):

    def from_settings(self):
        """Return an instance of the class for the given settings"""

    def load(self):
        """Return the Spider class for the given spider name. If the spider
        name is not found, it must raise a KeyError."""

    def list():
        """Return a list with the names of all spiders available in the
        project"""

    def find_by_request(self):
        """Return the list of spiders names that can handle the given request"""
