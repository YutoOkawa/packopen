class Card:
    def __init__(self, name_jp, name_en, rarity):
        self.name_jp = name_jp
        self.name_en = name_en
        self.rarity = rarity

    def print(self):
        print(self.rarity, self.name_jp+"/"+self.name_en)