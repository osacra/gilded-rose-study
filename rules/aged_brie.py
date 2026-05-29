from rules.base import UpdateRule
from rules.helpers import decrease_sell_in, increase_quality


class AgedBrieRule(UpdateRule):

    def apply(self, item):

        # sempre diminui o tempo
        decrease_sell_in(item)

        # aged brie sempre melhora
        increase_quality(item)

        # depois que passa da validade melhora mais ainda
        if item.sell_in < 0:
            increase_quality(item)