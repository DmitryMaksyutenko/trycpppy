from django.contrib.auth.models import Group

from roles.models import Authors


class AuthorGroup:

    def __init__(self):
        self.group_id = Group.objects.get(name=Authors.__name__.lower())

    def add(self, user):
        user.groups.add(self.group_id)

    def remove(self, user):
        user.groups.remove(self.group_id)
