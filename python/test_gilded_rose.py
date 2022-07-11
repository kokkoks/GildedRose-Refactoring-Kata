from gilded_rose import GildedRose, Item, AGED_BRIED, BACKSTAGE_PASSES, SULFURAS
from nose.tools import assert_equal


class TestGildedRose:
    def test_normal_item_with_sell_in_more_than_zero(self):
        list_item = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        expected_result = Item(name="+5 Dexterity Vest", sell_in=9, quality=19)
        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_normal_item_with_sell_in_less_than_zero(self):
        list_item = [Item(name="+5 Dexterity Vest", sell_in=0, quality=20)]
        expected_result = Item(name="+5 Dexterity Vest", sell_in=-1, quality=18)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_aged_brie_with_sell_in_more_than_zero(self):
        list_item = [
            Item(name=AGED_BRIED, sell_in=10, quality=1),
        ]
        expected_result = Item(name=AGED_BRIED, sell_in=9, quality=2)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_aged_brie_with_sell_in_less_than_zero(self):
        list_item = [
            Item(name=AGED_BRIED, sell_in=0, quality=1),
        ]
        expected_result = Item(name=AGED_BRIED, sell_in=-1, quality=2)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_backstage_passes_with_sell_in_more_than_ten(self):
        list_item = [Item(name=BACKSTAGE_PASSES, sell_in=15, quality=21)]
        expected_result = Item(name=BACKSTAGE_PASSES, sell_in=14, quality=22)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_backstage_passes_with_sell_in_more_than_three_less_than_ten(self):
        list_item = [Item(name=BACKSTAGE_PASSES, sell_in=6, quality=21)]
        expected_result = Item(name=BACKSTAGE_PASSES, sell_in=5, quality=23)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_backstage_passes_with_sell_in_less_than_three(self):
        list_item = [Item(name=BACKSTAGE_PASSES, sell_in=2, quality=21)]
        expected_result = Item(name=BACKSTAGE_PASSES, sell_in=1, quality=24)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_backstage_passes_with_sell_in_less_than_zero(self):
        list_item = [Item(name=BACKSTAGE_PASSES, sell_in=0, quality=21)]
        expected_result = Item(name=BACKSTAGE_PASSES, sell_in=-1, quality=0)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_sulfuras_with_sell_in_more_than_zero(self):
        list_item = [Item(name=SULFURAS, sell_in=2, quality=80)]
        expected_result = Item(name=SULFURAS, sell_in=1, quality=80)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_sulfuras_with_sell_in_less_than_zero(self):
        list_item = [Item(name=SULFURAS, sell_in=0, quality=80)]
        expected_result = Item(name=SULFURAS, sell_in=-1, quality=80)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_conjured_with_sell_in_more_than_zero(self):
        list_item = [Item(name="Conjured Mana Cake", sell_in=2, quality=20)]
        expected_result = Item(name="Conjured Mana Cake", sell_in=1, quality=18)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_conjured_with_sell_in_less_than_zero(self):
        list_item = [Item(name="Conjured Mana Cake", sell_in=0, quality=20)]
        expected_result = Item(name="Conjured Mana Cake", sell_in=-1, quality=16)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()

        assert_equal(expected_result, gilded_rose.items[0])

    def test_conjured_quality_is_one_with_sell_in_less_than_zero(self):
        list_item = [Item(name="Conjured Mana Cake", sell_in=0, quality=1)]
        expected_result = Item(name="Conjured Mana Cake", sell_in=-1, quality=0)

        gilded_rose = GildedRose(list_item)
        gilded_rose.update_quality()
        assert_equal(expected_result, gilded_rose.items[0])
