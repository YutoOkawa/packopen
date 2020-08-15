import unittest
import openPack
from card import Card

class OpenPackTest(unittest.TestCase):
    def setUp(self):
        """
        setup function
        """
        pass

    def tearDown(self):
        """
        tearDown function
        """
        pass

    def test_loadCardList(self):
        """
        loadCardListの単体テスト
        """
        testAllList, testCList, testUList, testRList, testMList, testLList = openPack.loadCardList("test_M21.xlsx")
        self.assertEqual([Card("レインジャーの悪知恵", "Ranger's Guile", "C")], testCList)
        self.assertEqual([Card("大殺漢", "Goremand", "U")], testUList)
        self.assertEqual([Card("栄光の頌歌", "Glorious Anthem", "R")], testRList)
        self.assertEqual([Card("長老ガーガロス", "Elder Gargaroth", "M")], testMList)
        self.assertEqual([Card("山", "Mountain", "L"), Card("血溜まりの洞窟", "Bloodfell Caves", "C")], testLList)

    def test_pickCard(self):
        """
        pickCardの単体テスト
        """
        testCard = Card("山", "Mountain", "L")
        testCardList = [Card("山", "Mountain", "L")]
        self.assertEqual(testCard, openPack.pickCard(testCardList))

    def test_openPack(self):
        """
        openPackの単体テスト
        """
        testAllList = [
            Card("素早い反応", "Swift Response", "C"),
            Card("村の儀式", "Village Rites", "C"),
            Card("冥府の傷跡", "Infernal Scarring", "C"),
            Card("胸躍る可能性", "Thrill of Possibility", "C"),
            Card("抵抗の妙技", "Feat of Resistance", "C"),
            Card("人生は続く", "Life Goes On", "C"),
            Card("レインジャーの悪知恵", "Ranger's Guile", "C"),
            Card("うろつく光霊", "Roaming Ghostlight", "C"),
            Card("噛み傷への興奮", "Furor of the Bitten", "C"),
            Card("霧のブレス", "Frost Breath", "C"),
            Card("悪い取引", "Bad Deal", "U"),
            Card("難破船の探知者", "Shipwreck Dowser", "U"),
            Card("豊かな実りの聖域", "Sanctum of Fruitful Harvest", "U"),
            Card("万物の聖域", "Sanctum of All", "R"),
            Card("島", "Island", "L")
        ]
        testCList = [
            Card("素早い反応", "Swift Response", "C"),
            Card("村の儀式", "Village Rites", "C"),
            Card("冥府の傷跡", "Infernal Scarring", "C"),
            Card("胸躍る可能性", "Thrill of Possibility", "C"),
            Card("抵抗の妙技", "Feat of Resistance", "C"),
            Card("人生は続く", "Life Goes On", "C"),
            Card("レインジャーの悪知恵", "Ranger's Guile", "C"),
            Card("うろつく光霊", "Roaming Ghostlight", "C"),
            Card("噛み傷への興奮", "Furor of the Bitten", "C"),
            Card("霧のブレス", "Frost Breath", "C")
        ]
        testUList = [
            Card("悪い取引", "Bad Deal", "U"),
            Card("難破船の探知者", "Shipwreck Dowser", "U"),
            Card("豊かな実りの聖域", "Sanctum of Fruitful Harvest", "U")
        ]
        testRList = [
            Card("万物の聖域", "Sanctum of All", "R")
        ]
        testMList = [
            Card("万物の聖域", "Sanctum of All", "R")
        ]
        testLList = [
            Card("島", "Island", "L")
        ]
        testpack = [
            Card("素早い反応", "Swift Response", "C"),
            Card("村の儀式", "Village Rites", "C"),
            Card("冥府の傷跡", "Infernal Scarring", "C"),
            Card("胸躍る可能性", "Thrill of Possibility", "C"),
            Card("抵抗の妙技", "Feat of Resistance", "C"),
            Card("人生は続く", "Life Goes On", "C"),
            Card("レインジャーの悪知恵", "Ranger's Guile", "C"),
            Card("うろつく光霊", "Roaming Ghostlight", "C"),
            Card("噛み傷への興奮", "Furor of the Bitten", "C"),
            Card("霧のブレス", "Frost Breath", "C"),
            Card("悪い取引", "Bad Deal", "U"),
            Card("難破船の探知者", "Shipwreck Dowser", "U"),
            Card("豊かな実りの聖域", "Sanctum of Fruitful Harvest", "U"),
            Card("万物の聖域", "Sanctum of All", "R"),
            Card("島", "Island", "L")
        ]

        self.assertEqual(set(testpack), set(openPack.openPack(testAllList, testCList, testUList, testRList, testMList, testLList)))

if __name__ == "__main__":
    unittest.main()