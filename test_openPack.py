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
        TODO:loadCardListのテストの実装
        """
        pass

    def test_pickCard(self):
        """
        pickCardの単体テスト
        """
        testCard = Card("山", "Mountain", "L")
        testCardList = [testCard]
        self.assertEqual(testCard, openPack.pickCard(testCardList))

    def test_openPack(self):
        """
        openPackの単体テスト
        """
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
        testpack = []

        for card in testRList:
            testpack.append(card)

        for card in testUList:
            testpack.append(card)

        for card in testCList:
            testpack.append(card)

        for card in testLList:
            testpack.append(card)

        self.assertEqual(set(testpack), set(openPack.openPack(testCList, testUList, testRList, testMList, testLList)))

if __name__ == "__main__":
    unittest.main()