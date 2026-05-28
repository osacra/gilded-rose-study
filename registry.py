from rules.default import DefaultRule
from rules.aged_brie import AgedBrieRule
from rules.backstage import BackstageRule
from rules.sulfuras import SulfurasRule

class RuleRegistry:
    def __init__(self):
        self.rules = {
            "Aged Brie": AgedBrieRule(),
            "Backstage passes to a TAFKAL80ETC concert": BackstageRule(),
            "Sulfuras, Hand of Ragnaros": SulfurasRule(),
        }

        self.default = DefaultRule()

    def get_rule(self, item):
        return self.rules.get(item.name, self.default)