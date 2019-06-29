# A RouteTrie will store our routes and their associated handlers
class RouteTrieNode:
    def __init__(self):
        self.nodes = {}
        self.handler = None

    def insert(self, route):
        node = self.nodes.get(route)
        if node:
            return node

        node = RouteTrieNode()
        self.nodes[route] = node
        return node


class RouteTrie:
    def __init__(self, split_fn):
        self.root = RouteTrieNode()
        self.split_fn = split_fn

    def insert(self, path, handler):
        current = self.root
        for route in self.split_fn(path):
            current = current.insert(route)
        current.handler = handler

    def find(self, path):
        current = self.root
        for route in self.split_fn(path):
            current = current.nodes.get(route)
            if not current:
                return None
        return current


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.trie = RouteTrie(self.split_path)
        self.trie.insert("/", root_handler)
        self.trie.insert("404", not_found_handler)

    def add_handler(self, route, handler):
        self.trie.insert(route, handler)

    def lookup(self, path):
        current = self.trie.root
        for ch in self.split_path(path):
            current = current.nodes.get(ch)
            if not current:
                return self.trie.root.nodes["404"].handler
        return current.handler

    def split_path(self, path):
        return path.strip("/").split("/")


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")


# Tests
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
