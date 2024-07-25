# MARK: 매뉴판 출력
import os
import csv
menu_print = """
🛸　　　 　🌎　°　　🌓　•　　.°•　　　🚀 ✯
　　　★　*　　　　　°　　　　🛰 　°·　　                           🪐
.　　　•　° ★　•  ☄
▁▂▃▄▅▆▇▇▆▅▄▃▁▂
****************************** MENU ***********************************
      Coffee/Tea              Bread                  Side Menu
---------------------------------------------------------
   Americano   2500    LoafBread       3000   SalmonSkinSalad    6000
   CafeLatte   3500    Croissant       3000   FriedChickenSalad  6000
   Espresso    3000    ApplePie        4000
   GreenTea    3300    StrawberryCake  4500
-----------------------------------------------------------------------
"""
print(menu_print)

# MARK:손님한테 주문받아 금액출력하는 시스템


def load_menu_from_csv(file_path):
    menu = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # 헤더 건너뛰기
        for row in csv_reader:
            category, item, price = row
            price = int(price)
            if category not in menu:
                menu[category] = {}
            menu[category][item] = price
    return menu


def create_menu_csv(file_path):
    menu_data = [
        ("Coffee/Tea", "Americano", 2500),
        ("Coffee/Tea", "CafeLatte", 3500),
        ("Coffee/Tea", "Espresso", 3000),
        ("Coffee/Tea", "Green Tea", 3300),
        ("Bread", "Loaf_Bread", 3000),
        ("Bread", "Croissant", 3000),
        ("Bread", "ApplePie", 4000),
        ("Bread", "StrawberryCake", 4500),
        ("Side Menu", "SalmonSkinSalad", 6000),
        ("Side Menu", "FriedChickenSalad", 6000)
    ]

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Item", "Price"])
        for data in menu_data:
            writer.writerow(data)

    print(f"메뉴가 '{file_path}' 파일에 저장되었습니다.")


def get_csv_path():
    default_path = 'menu.csv'
    if not os.path.exists(default_path):
        create_menu_csv(default_path)
    return default_path


csv_path = get_csv_path()
menu = load_menu_from_csv(csv_path)


def display_order_summary(order_dict, total_amount, total_count):
    print("\n**********주문 내역**********")
    for item, details in order_dict.items():
        print(f"{item}: {details['count']}개 - {details['amount']}원")
    print(f"\n총 주문 금액은 {total_amount}원입니다.")
    print(f"총 주문 수량은 {total_count}개입니다.")


def process_order(order, order_dict):
    total_amount = 0
    total_count = 0
    i = 0

    while i < len(order):
        try:
            item = order[i]
            count = int(order[i + 1])

            # 메뉴 확인 및 가격 합산
            item_found = False
            for category, items in menu.items():
                if item in items:
                    item_price = items[item]
                    if item in order_dict:
                        order_dict[item]['count'] += count
                        order_dict[item]['amount'] += item_price * count
                    else:
                        order_dict[item] = {'count': count,
                                            'amount': item_price * count}
                    total_amount += item_price * count
                    total_count += count
                    item_found = True
                    break

            if not item_found:
                print(f"메뉴에 '{item}'가 없습니다.")
                return False, total_amount, total_count
            i += 2
        except (ValueError, IndexError):
            print(
                f"잘못된 입력: {order[i:]}. 올바른 형식으로 입력해주세요. ex) Americano 2 Espresso 3")
            return False, total_amount, total_count

    return True, total_amount, total_count


def take_order():
    total_amount = 0
    total_count = 0
    order_dict = {}

    while True:
        order = input(
            "메뉴와 주문수량을 입력해주세요.\n예시처럼 메뉴와 수량으로 입력해주세요!! ex) Americano 2 Espresso 3 SalmonSkinSalad 1 : ").split()
        valid_order, order_amount, order_count = process_order(
            order, order_dict)

        if valid_order:
            total_amount += order_amount
            total_count += order_count
            while True:
                add_more = input("더 추가할 메뉴가 없으신가요? ex) y or n ").lower()
                if add_more == "y":
                    display_order_summary(
                        order_dict, total_amount, total_count)
                    return
                elif add_more == "n":
                    break
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요! y 또는 n 로만 답해주세요.")


take_order()
