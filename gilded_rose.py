from registry import RuleRegistry
from item import Item

class GildedRose:
    def __init__(self, items):
        self.items = items
        self.registry = RuleRegistry()

    def update_quality(self):
        for item in self.items:
            rule = self.registry.get_rule(item)
            rule.apply(item)