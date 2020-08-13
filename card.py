class Card:
    """
    カードの各属性値やヘルパー関数を保持する。

    Attirbutes
    ----------
    name_jp : str
        カードの日本語名。
    name_en : str
        カードの英語名。
    rarity : str
        カードのレアリティ。
    """
    def __init__(self, name_jp, name_en, rarity):
        """
        初期化関数
        """
        self.name_jp = name_jp
        self.name_en = name_en
        self.rarity = rarity

    def print(self):
        """
        カード情報を整形して出力する。
        """
        print(self.rarity, self.name_jp+"/"+sel.name_en)