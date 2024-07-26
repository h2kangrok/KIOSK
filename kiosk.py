import os
import csv

# 기본 메뉴판을 출력하는 함수


def print_regular_menu():
    menu_print = """
    🛸　　　 　🌎　°　　🌓　•　　.°•　　　🚀 ✯
    　　　★　*　　　　　°　　　　🛰 　°·　　                           🪐
    .　　　•　° ★　•  ☄
    ▁▂▃▄▅▆▇▇▆▅▄▃▁▂
    ****************************** MENU ***********************************
          Coffee/Tea              Bread                  Side Menu
    -----------------------------------------------------------------------
       Americano   2500    LoafBread       3000   SalmonSkinSalad    6000
       CafeLatte   3500    Croissant       3000   FriedChickenSalad  6000
       Espresso    3000    ApplePie        4000
       GreenTea    3300    StrawberryCake  4500
    -----------------------------------------------------------------------
    """
    print(menu_print)

# 여름 메뉴판을 출력하는 함수


def print_summer_menu():
    summer_menu_print = """
    ☀️　　　 　🌊　°　　🏖️　•　　.°•　　　🍹 🌴
    　　　★　*　　　　　°　　　　🍦 　°·　　                           🌺
    .　　　•　° ★　•  ☀️
    ▁▂▃▄▅▆▇▇▆▅▄▃▁▂
    ****************************** SUMMER MENU ***********************************
          Cold Drinks              Summer Desserts           Summer Side Menu
    -----------------------------------------------------------------------
       IcedCoffee   3500    MangoSorbet    4000   ColdNoodleSalad    5000
       Lemonade     3000    PineappleCake  4500   FruitSalad         4000
       IcedTea      3300    StrawberrySmoothie  4500
    -----------------------------------------------------------------------
    """
    print(summer_menu_print)

# CSV 파일에서 메뉴를 읽어오는 함수


def load_menu_from_csv(file_path):
    menu = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # CSV 파일의 첫 번째 행(헤더)를 건너뜀
        for row in csv_reader:
            category, item, price = row
            price = int(price)  # 가격을 정수로 변환
            if category not in menu:
                menu[category] = {}  # 카테고리가 없으면 새로 생성
            menu[category][item] = price
    return menu

# 기본 메뉴 CSV 파일을 생성하는 함수


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
        writer.writerow(["Category", "Item", "Price"])  # CSV 파일의 헤더
        for data in menu_data:
            writer.writerow(data)  # 메뉴 데이터를 CSV에 기록

    print(f"메뉴가 '{file_path}' 파일에 저장되었습니다.")

# 여름 메뉴 CSV 파일을 생성하는 함수


def create_summer_menu_csv(file_path):
    summer_menu_data = [
        ("Cold Drinks", "IcedCoffee", 3500),
        ("Cold Drinks", "Lemonade", 3000),
        ("Cold Drinks", "IcedTea", 3300),
        ("Summer Desserts", "MangoSorbet", 4000),
        ("Summer Desserts", "PineappleCake", 4500),
        ("Summer Desserts", "StrawberrySmoothie", 4500),
        ("Summer Side Menu", "ColdNoodleSalad", 5000),
        ("Summer Side Menu", "FruitSalad", 4000)
    ]

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Item", "Price"])  # CSV 파일의 헤더
        for data in summer_menu_data:
            writer.writerow(data)  # 여름 메뉴 데이터를 CSV에 기록

    print(f"여름 메뉴가 '{file_path}' 파일에 저장되었습니다.")

# 기본 메뉴 CSV 파일 경로를 반환하며, 파일이 없으면 생성


def get_csv_path():
    default_path = 'menu.csv'
    if not os.path.exists(default_path):  # 파일이 존재하지 않으면 생성
        create_menu_csv(default_path)
    return default_path

# 여름 메뉴 CSV 파일 경로를 반환하며, 파일이 없으면 생성


def get_summer_csv_path():
    summer_path = 'summer_menu.csv'
    if not os.path.exists(summer_path):  # 파일이 존재하지 않으면 생성
        create_summer_menu_csv(summer_path)
    return summer_path

# 메뉴를 선택하는 함수


def select_menu():
    print("\n당신은 손님인가요, 주인인가요? (손님/주인): ", end="")
    role = input().strip().lower()
    if role == "손님":
        print("메뉴판을 보여드립니다.")
        return get_csv_path(), print_regular_menu
    elif role == "주인":
        print("\n메뉴판을 선택하세요:")
        print("1. 평소 메뉴판")
        print("2. 여름 메뉴판")
        while True:
            choice = input("선택 (1/2): ").strip()
            if choice == "1":
                print_regular_menu()
                return get_csv_path(), print_regular_menu
            elif choice == "2":
                print_summer_menu()
                return get_summer_csv_path(), print_summer_menu
            else:
                print("잘못된 입력입니다. 1 또는 2를 선택해주세요.")
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        exit()

# 주문 내역을 출력하는 함수


def display_order_summary(order_dict, total_amount, total_count):
    print("\n**********주문 내역**********")
    for item, details in order_dict.items():
        print(f"{item}: {details['count']}개 - {details['amount']}원")
    print(f"\n총 주문 금액은 {total_amount}원입니다.")
    print(f"총 주문 수량은 {total_count}개입니다.")

# 주문을 처리하는 함수


def process_order(order, order_dict):
    total_amount = 0
    total_count = 0
    i = 0

    while i < len(order):
        try:
            item = order[i]
            count = int(order[i + 1])

            if item.lower() == "종료":
                print("주문이 종료되었습니다. 프로그램을 종료합니다.")
                exit()

            # 메뉴에서 아이템 가격 확인
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

# 주문을 받는 함수


def take_order():
    total_amount = 0
    total_count = 0
    order_dict = {}

    while True:
        order_input = input(
            "메뉴와 주문수량을 입력해주세요. 예시처럼 메뉴와 수량으로 입력해주세요!! ex) Americano 2 Espresso 3 SalmonSkinSalad 1\n종료하시려면 '종료'라고 입력해주세요: ")
        if order_input.lower() == "종료":
            print("주문이 종료되었습니다. 프로그램을 종료합니다.")
            exit()

        order = order_input.split()  # 입력된 주문을 분리하여 리스트로 변환
        valid_order, order_amount, order_count = process_order(
            order, order_dict)  # 주문 처리

        if valid_order:
            total_amount += order_amount
            total_count += order_count
            while True:
                add_more = input("더 추가할 메뉴가 없으신가요? (y/n): ").lower()
                if add_more == "y":
                    display_order_summary(
                        order_dict, total_amount, total_count)
                    return
                elif add_more == "n":
                    break
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요! y 또는 n 로만 답해주세요.")

# 메인 함수


def main():
    global menu
    csv_path, menu_print_func = select_menu()  # 메뉴 선택
    menu = load_menu_from_csv(csv_path)  # 선택된 메뉴 CSV 파일에서 데이터 로드

    if menu_print_func:
        menu_print_func()  # 선택된 메뉴판 출력

    take_order()  # 주문 받기


# 프로그램이 실행될 때 메인 함수 호출
if __name__ == "__main__":
    main()
