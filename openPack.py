import openpyxl
import random
from tqdm import tqdm

from card import Card

allCardList = []
commonCardList = []
uncommonCardList = []
rareCardList = []
mythicCardList = []
landCardList = []

def loadCardList():
    """
    xlsxファイルの読み込む。
    レアリティごとのリスト、全カードリストを作成する。
    """
    print("\n----- Start Loading CardList -----")
    wb = openpyxl.load_workbook("M21.xlsx")
    sheet = wb["シート1"]
    for i in tqdm(range(2, sheet.max_row+1)):
        name_jp = sheet.cell(row=i,column=1).value
        name_en = sheet.cell(row=i,column=2).value
        rarity = sheet.cell(row=i,column=3).value
        card = Card(name_jp, name_en, rarity)
        allCardList.append(card)
        if card.rarity == "C":
            commonCardList.append(card)
        elif card.rarity == "U":
            uncommonCardList.append(card)
        elif card.rarity == "R":
            rareCardList.append(card)
        elif card.rarity == "M":
            mythicCardList.append(card)
        elif card.rarity == "L":
            landCardList.append(card)
    print("----- Finish Loading CardList -----")

def pickCard(cardList):
    """
    カードリストからランダムなカードを取得する。

    Parameters
    ----------
    cardList : list(Card)
        対象のカードリスト。

    Returns
    -------
    card : Card
        ランダムに選ばれたカード。
    """
    number = random.randrange(len(cardList))
    card = cardList[number]
    return card

# pack開封モード
def openPack():
    """
    1パック開封するゲームモードを開始する。
    """
    pack = []

    # Mythicの抽選
    # 1/8の確率でMythic, そうでなければRare
    rare = random.randrange(8)
    if rare == 0:
        rareCard = pickCard(mythicCardList)
    else:
        rareCard = pickCard(rareCardList)
    pack.append(rareCard)

    # Uncommonの抽選
    # 1パックに3枚
    while len(pack) != 4:
        ucCard = pickCard(uncommonCardList)
        if ucCard in pack:
            continue
        pack.append(ucCard)

    # Commonの抽選
    # レア枠、UC枠、Foil枠、土地枠以外全て
    while len(pack) != 14:
        cCard = pickCard(commonCardList)
        if cCard in pack:
            continue
        pack.append(cCard)

    # Landの抽選
    landCard = pickCard(landCardList)
    pack.append(landCard)

    # カード情報の出力
    # packの内容を全て出力
    for card in pack:
        card.print()

def main():
    loadCardList()

    print("\nWelcome to Open Pack Simulator!")
    while True:
        print("\nMenu:")
        print("1:one pack open")
        print("0:exit this program")
        print("input number>", end="")
        check = int(input())
        if check == 1:
            openPack()
        elif check == 0:
            print("Thank you for playing!")
            quit()

if __name__ == "__main__":
    main()
