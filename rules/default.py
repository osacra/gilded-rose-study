from rules.base import UpdateRule

class DefaultRule(UpdateRule):
    def apply(self, item):
        item.sell_in -= 1

        if item.quality > 0:
            item.quality -= 1

        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1