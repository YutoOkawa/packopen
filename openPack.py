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
# 対象のカードリストを入力としランダムなカードを出力する
def pickCard(cardList):
    number = random.randrange(len(cardList))
    card = cardList[number]
    print(card.rarity, card.name_jp+"/"+card.name_en)

# pack開封モード
def openPack():
    # Mythicの抽選
    # 1/8の確率でMythic, そうでなければRare
    mythic = random.randrange(8)
    if mythic == 0:
        pickCard(mythicCardList)
    else:
        pickCard(rareCardList)

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
