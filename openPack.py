import openpyxl
import random
from tqdm import tqdm

from card import Card

def loadCardList(all, cList, uList, rList, mList, lList):
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
        all.append(card)
        if card.rarity == "C":
            cList.append(card)
        elif card.rarity == "U":
            uList.append(card)
        elif card.rarity == "R":
            rList.append(card)
        elif card.rarity == "M":
            mList.append(card)
        elif card.rarity == "L":
            lList.append(card)
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
def openPack(cList, uList, rList, mList, lList):
    """
    1パック開封するゲームモードを開始する

    Parameters
    ----------
    cList : list(Card)
        コモンのカードリスト
    uList : list(Card)
        アンコモンのカードリスト
    rList : list(Card)
        レアのカードリスト
    mList : list(Card)
        神話のカードリスト
    lList : list(Card)
        土地のカードリスト

    Returns
    -------
    pack : list(Card)
        作成されたパックの内容
    """
    pack = []

    # Mythicの抽選
    # 1/8の確率でMythic, そうでなければRare
    rare = random.randrange(8)
    if rare == 0:
        rareCard = pickCard(mList)
    else:
        rareCard = pickCard(rList)
    pack.append(rareCard)

    # Uncommonの抽選
    # 1パックに3枚
    while len(pack) != 4:
        ucCard = pickCard(uList)
        if ucCard in pack:
            continue
        pack.append(ucCard)

    # Commonの抽選
    # レア枠、UC枠、Foil枠、土地枠以外全て
    while len(pack) != 14:
        cCard = pickCard(cList)
        if cCard in pack:
            continue
        pack.append(cCard)

    # Landの抽選
    landCard = pickCard(lList)
    pack.append(landCard)

    return pack

def main():
    allCardList = []
    commonCardList = []
    uncommonCardList = []
    rareCardList = []
    mythicCardList = []
    landCardList = []

    loadCardList(allCardList, commonCardList, uncommonCardList, rareCardList, mythicCardList, landCardList)

    print("\nWelcome to Open Pack Simulator!")
    while True:
        print("\nMenu:")
        print("1:one pack open")
        print("0:exit this program")
        print("input number>", end="")
        check = int(input())
        if check == 1:
            pack = openPack(commonCardList, uncommonCardList, rareCardList, mythicCardList, landCardList)
            for card in pack:
                card.print()
        elif check == 0:
            print("Thank you for playing!")
            quit()

if __name__ == "__main__":
    main()
