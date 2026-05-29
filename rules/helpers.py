# helpers pra não repetir lógica em todas as rules

def decrease_sell_in(item):
    item.sell_in -= 1


def increase_quality(item, amount=1):
    # aumenta quality mas nunca passa de 50
    if item.quality < 50:
        item.quality += amount

        if item.quality > 50:
            item.quality = 50


def decrease_quality(item, amount=1):
    # diminui quality mas nunca fica negativo
    if item.quality > 0:
        item.quality -= amount

        if item.quality < 0:
            item.quality = 0