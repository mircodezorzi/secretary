from typing import Dict, List


class shard(object):
    def __init__(self, path, content):
        self.path = path
        self.content = content


class component(object):
    def __init__(self, name: str, shards: List[shard]):
        self.name = name
        self.shards: List[shard] = shards


class registry(object):
    def __init__(self):
        self.components: Dict[component] = {}

    def register(self, component: component):
        self.components[component.name] = component
