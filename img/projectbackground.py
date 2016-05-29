class ProjectPortfolio(object):
    """A Portfolio that contains a number of projects.
    Attributes:
        name: A string representing the Portfolio's name."""

    def __init__(self, name):
        """Return a ProjectPortfolio object whose name is *name* and projects list is empty."""
        self.name = name
        self.projects = []

    def addProject(self, project):
        """Adds *project* to project list"""
        self.projects.append(project) 

        