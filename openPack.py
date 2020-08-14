import openpyxl
import random
from tqdm import tqdm

from card import Card

def loadCardList(filename):
    """
    カードリストが記述されたxlsxファイルを読み込む。
    基本土地枠に基本土地でないカードが入る場合、その内容が記述されたファイルを読み込む。
    レアリティごとのリスト、全カードリストを作成する。

    Parameters
    ----------
    filename : str
        読み込む対象のxlsxファイル名

    Returns
    -------
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
    """
    cList, uList, rList, mList, lList = [], [], [], [], []
    print("\n----- Start Loading CardList -----")
    with open("notBasicLands.txt") as f:
        l = [s.strip() for s in f.readlines()]
        print(l)
    # TODO:FileNotFoundErrorへの対処
    wb = openpyxl.load_workbook(filename)
    sheet = wb["シート1"]
    for i in tqdm(range(2, sheet.max_row+1)):
        name_jp = sheet.cell(row=i,column=1).value
        name_en = sheet.cell(row=i,column=2).value
        rarity = sheet.cell(row=i,column=3).value
        card = Card(name_jp, name_en, rarity)
        if card.rarity == "C":
            if card.name_en in l:
                lList.append(card)
            else:
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

    return cList, uList, rList, mList, lList

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

    print("\nOpen a Pack!")
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
    commonCardList, uncommonCardList, rareCardList, mythicCardList, landCardList = loadCardList("M21.xlsx")

    print("\nWelcome to Open Pack Simulator!")
    while True:
        print("\nMenu List-----------------------------------------------------------------------------")
        print("1:open a pack")
        print("2:show all common cards")
        print("3:show all uncommon cards")
        print("4:show all rare cards")
        print("5:show all mythic cards")
        print("6:show all land cards")
        print("0:exit this program")
        print("--------------------------------------------------------------------------------------")
        print("input number>", end="")
        try:
            check = int(input())
        except ValueError as e:
            print("\nError: ", end="")
            print(e)
            print("Retry input number.")
            continue
        if check == 1:
            pack = openPack(commonCardList, uncommonCardList, rareCardList, mythicCardList, landCardList)
            print("--------------------------------------------------------------------------------------")
            for card in pack:
                card.print()
            print("--------------------------------------------------------------------------------------")
            print("You get a nice pack! continue?")
        elif check == 2:
            for card in commonCardList:
                card.print()
        elif check == 3:
            for card in uncommonCardList:
                card.print()
        elif check == 4:
            for card in rareCardList:
                card.print()
        elif check == 5:
            for card in mythicCardList:
                card.print()
        elif check == 6:
            for card in landCardList:
                card.print()
        elif check == 0:
            print("\nThank you for playing!")
            quit()
        else:
            print("\nError: Unknown Code! Retry input number.")

if __name__ == "__main__":
    main()
