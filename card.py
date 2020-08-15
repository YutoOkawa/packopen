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
    foiled : bool
        Foilであるかどうか。
    """
    def __init__(self, name_jp, name_en, rarity):
        """
        初期化関数
        """
        self.name_jp = name_jp
        self.name_en = name_en
        self.rarity = rarity
        self.foiled = False

    def __eq__(self, other):
        """
        比較演算子==の定義
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.name_jp == other.name_jp and self.name_en == other.name_en and self.rarity == other.rarity

    def __hash__(self):
        """
        ハッシュ化可能識別子
        """
        return hash(self.name_jp) ^ hash(self.name_en) ^ hash(self.rarity)

    def print(self):
        """
        カード情報を整形して出力する。
        """
        print(self.rarity, self.name_jp+"/"+self.name_en, end="")
        if self.foiled:
            print(" [Foil]")
            self.foiled = False
        else:
            print()

    def setFoiled(self, foiled):
        """
        Foiledのsetter
        """
        self.foiled = foiled