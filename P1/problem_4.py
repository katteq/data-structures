class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


import time


cache = None

class Cache:
    def __init__(self, group):
        self.group = group
        self.itenternal_cache = {}
        if group is not None:
            self.cache_groups(group)

    def cache_groups(self, group, parents = set()):
        users = group.get_users()
        for user in users:
            cached_user = self.itenternal_cache.get(user)
            if cached_user == None:
                cached_user = set()
            cached_user.add(group.name)
            cached_user.update(parents)
            self.itenternal_cache[user] = cached_user

        parents.add(group.name)
        for gr in group.get_groups():
            self.cache_groups(gr, parents)

    def instance(self):
        return self.itenternal_cache


# Without a cache
def is_user_in_group2(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not user or not group:
        return False
    sub_groups = group.get_groups()
    users = group.get_users()
    if user in users:
        return True
    else:
        for gr in sub_groups:
            if is_user_in_group(user, gr):
                return True

    return False

cache = None

# With precached users and their groups
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    global cache

    # During the first function excecution we build the users cache with the following structure:
    #  {
    #   user_id1: ( "group_id1", "group_id2", "group_id3"),
    #   user_id2: ( "group_id1", "group_id3"),
    #   user_id3: ( "group_id3")
    #  }
    #  For this data structure we use a dictionary and set, which garantee a constant lookup time on the subsequent
    #  funtion calls.

    if not user or not group:
        return False

    if cache is None:
        cache = Cache(group).instance()

    user_groups = cache.get(user)
    if user_groups == None:
        return False

    return True if group.name in user_groups else False


def test1():
    parent = Group("parent")
    childA1 = Group("childA1")
    childA2 = Group("childA2")
    childA3 = Group("childA3")

    childB1 = Group("childB1")
    childB2 = Group("childB2")

    childA1.add_group(childB1)
    childA2.add_group(childB2)
    childA3.add_group(childB2)

    childB2.add_user("CHILD_USER1")
    childA2.add_user("CHILD_USER2")
    childA1.add_user("CHILD_USER3")
    childB1.add_user("CHILD_USER4")

    parent.add_group(childA1)
    parent.add_group(childA2)
    parent.add_group(childA3)

    start = time.process_time()
    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER1', parent) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER2', parent) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER3', parent) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER4', parent) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if not is_user_in_group('CHILD_USER5', parent) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER1', childB2) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER1', childA2) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER2', childA2) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER4', childB1) else "Fail")
    start = time.process_time()

    print("Pass| "+ "%.2gs" % ( time.process_time() - start) if is_user_in_group('CHILD_USER1', childA3) else "Fail")
    start = time.process_time()

def test2():
    parent = Group("parent")
    childA1 = Group("childA1")
    childA1.add_user("user")
    parent.add_group(childA1)

    print("Pass" if not is_user_in_group(None, parent) else "Fail")
    print("Pass" if not is_user_in_group("user", None) else "Fail")
    print("Pass" if not is_user_in_group(None, None) else "Fail")


test1()
test2()
