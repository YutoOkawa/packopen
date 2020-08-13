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

# xlsxファイルの読み込み
# レアリティごとのリスト、全カードリストの作成
def loadCardList():
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

# カード情報の出力
# 対象のカードリストを入力とし、その中からランダムなカードを出力する
def pickCard(cardList):
    number = random.randrange(len(cardList))
    card = cardList[number]
    return card

# pack開封モード
def openPack():
    pack = []

    # Mythicの抽選
    # 1/8の確率でMythic, そうでなければRare
    rare = random.randrange(8)
    if rare == 0:
        rareCard = pickCard(mythicCardList)
    else:
        rareCard = pickCard(rareCardList)
    pack.append(rareCard)

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

    # for card in allCardList:
    #     print(card.rarity, card.name_jp+"/"+card.name_en)

if __name__ == "__main__":
    main()
