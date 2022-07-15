# -*- coding: utf-8 -*-
import copy
AGED_BRIED = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"
MAX_QUALITY = 50
MIN_QUALITY = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __eq__(self, __o: object) -> bool:
        is_same_name = self.name == __o.name
        is_same_sell_in = self.sell_in == __o.sell_in
        is_same_quality = self.quality == __o.quality
        return is_same_name and is_same_sell_in and is_same_quality


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    # TODO: seperate update_quality & update_sell_in method
    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                item.sell_in = self._update_sell_in(item)
                continue

            if item.name != AGED_BRIED and item.name != BACKSTAGE_PASSES:
                if item.name == CONJURED:
                    item.quality = max(item.quality - 2, MIN_QUALITY)
                else:
                    item.quality = max(item.quality - 1, MIN_QUALITY)
            elif item.name == BACKSTAGE_PASSES and item.quality < MAX_QUALITY:
                if item.sell_in < 6:
                    item.quality = min(item.quality + 3, MAX_QUALITY)
                elif item.sell_in < 11:
                    item.quality = min(item.quality + 2, MAX_QUALITY)
                else:
                    item.quality = item.quality + 1
            elif item.name == AGED_BRIED and item.quality < MAX_QUALITY:
                item.quality = item.quality + 1

            item.sell_in = self._update_sell_in(item)

            if item.sell_in < 0:
                if item.name != AGED_BRIED:
                    if item.name != BACKSTAGE_PASSES:
                        if item.name == CONJURED:
                            item.quality = max(item.quality - 2, MIN_QUALITY)
                        else:
                            item.quality = max(item.quality - 1, MIN_QUALITY)
                    else:
                        item.quality = 0

    def _update_sell_in(self, item: Item) -> int:
        _item = copy.deepcopy(item)
        return _item.sell_in - 1
