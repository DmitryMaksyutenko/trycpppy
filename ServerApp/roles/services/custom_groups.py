from django.contrib.auth.models import Group

from roles.models import Authors


class AuthorGroup:
    """The wrapper class for addition, and deletion of the user
        from the Authors group.
    """

    def __init__(self):
        self.group_id = Group.objects.get(name=Authors.__name__.lower())

    def add(self, user):
        """Add user to group."""
        user.groups.add(self.group_id)

    def remove(self, user):
        """Remove user from group."""
        user.groups.remove(self.group_id)
