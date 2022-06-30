from gilded_rose import GildedRose, Item
from nose.tools import assert_equal


class TestGildedRose:
    def __init__(self) -> None:
        self.items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49
            ),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

    def test_one_day_passed(self):
        expected_result = [
            Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
            Item(name="Aged Brie", sell_in=1, quality=1),
            Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=78),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-2, quality=78),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=21
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50
            ),
            Item(name="Conjured Mana Cake", sell_in=2, quality=5),  # <-- :O
        ]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        assert_equal(expected_result, self.items)
