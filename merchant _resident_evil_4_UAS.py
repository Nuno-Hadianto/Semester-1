from prettytable import PrettyTable
import matplotlib.pyplot as mberr
print("++++++++++++++++++++++++++")
print("Resident Evil 4 HD Edition")
print("*****Professional Mode****")
print("*****Pc Steam Versions****")
print("++++++++++++++++++++++++++")

player = {
    "name" : ["Leon", "Ada"],
    "pin"  : ['333', '666']
}

money = {
    "pesetas" : 100000,
    "e-money" : 0
}

weapons = {
    "Code" : [1,2,3],
    "Weapons Name" : ["Red9", "Riot Gun", "Broken Butterfly"],
    "Weapons Price First" : [14000, 12000, 38000],
    "Weapons Price Two" : [28000, 24000, 76000]
}

voucher_card = {
    "Voucher Card Name" : ["Verdugo", "Salazar", "Plagas"],
    "Discount" : [0.4, 0.3, 0.5],
    "Status" : ["Active"]
}

purchase_history = {
    "vip"   : {"items": [], "total_spent": 0},
    "non_vip": {"items": [], "total_spent": 0}
}

vip_player_tables = PrettyTable()
vip_player_tables.field_names = ["Code", "Weapons Name", "Weapons Price First"]

non_vip_player_tables = PrettyTable()
non_vip_player_tables.field_names = ["Code", "Weapons Name", "Weapons Price Two"]

def chart_buat_weapons_vip(weapons):
    weapons_names = weapons["Weapons Name"]
    prices_first = weapons["Weapons Price First"]

    mberr.figure(figsize=(10, 6))
    mberr.bar(weapons_names, prices_first, color='blue', label='VIP Price')
    mberr.xlabel('Weapons Name')
    mberr.ylabel('Price')
    mberr.title('VIP WEAPONS PRICE')
    mberr.legend()
    mberr.show()

def chart_buat_weapons_non_vip(weapons):
    weapons_names = weapons["Weapons Name"]
    prices_first = weapons["Weapons Price Two"]

    mberr.figure(figsize=(10, 6))
    mberr.bar(weapons_names, prices_first, color='red', label='NON VIP Price')
    mberr.xlabel("Weapons Name")
    mberr.ylabel("Price")
    mberr.title("NON VIP WEAPONS PRICE")
    mberr.legend()
    mberr.show()

def chart_buat_liat_cash(money):
    mata_uang = ["Pesetas", "E-Money"]
    duit = [money["pesetas"], money["e-money"]]

    mberr.figure(figsize=(10, 6))
    mberr.bar(mata_uang, duit, color=["orange", "green"])
    mberr.xlabel("Mata uang")
    mberr.ylabel("Jumlah")
    mberr.title("Your pocket right now")
    mberr.show()

def chart_buat_liat_voucher(voucher_card):
    voucher_names = voucher_card["Voucher Card Name"]
    discounts = voucher_card["Discount"]

    mberr.figure(figsize=(10, 6))
    mberr.bar(voucher_names, discounts, color=["blue", "green", "red"])
    mberr.xlabel("Voucher Card Name")
    mberr.ylabel("Discount")
    mberr.title("Voucher Discounts")
    mberr.show()

def chart_buat_liat_history_beli(purchase_history):
    vip_history = purchase_history["vip"]
    non_vip_history = purchase_history["non_vip"]

    mberr.figure(figsize=(10, 6))
    mberr.bar("VIP", vip_history["total_spent"], color="brown", label="VIP Player")
    mberr.bar("Non-VIP", non_vip_history["total_spent"], color="purple", label="Non-VIP Player")
    mberr.xlabel("Player Type")
    mberr.ylabel("Total Spent")
    mberr.title("Purchase History")
    mberr.legend()
    mberr.show()

def vip_player_weapons():
    vip_player_tables.clear_rows()
    for inventory in range(len(weapons.get("Weapons Name"))):
        vip_player_tables.add_row([weapons.get("Code")[inventory],
                                   weapons.get("Weapons Name")[inventory],
                                   weapons.get("Weapons Price First")[inventory]])
        print(vip_player_tables)

def non_vip_player_weapons():
    non_vip_player_tables.clear_rows()
    for inventory in range(len(weapons.get("Weapons Name"))):
        non_vip_player_tables.add_row([weapons.get("Code")[inventory],
                                       weapons.get("Weapons Name")[inventory],
                                       weapons.get("Weapons Price Two")[inventory]])
        print(non_vip_player_tables)

def merchant_menu_vip():
    print("=================================================")
    print("===========+Automatic get 30 % Discount+=========")
    print("================Half Price Too!==================")
    print("=================================================")
    print("Got a selection of good things on sale, stranger!")
    print("=================================================")
    print("\n1. Buy Weapons\n2. Inspect Weapons\n3. Inspect Cash Balance\n4. Convert Cash Balance\n5. Purchase History\n6. Leave")
    print("=================================================")

def merchant_menu_non_vip():
    print("=================================================")
    print("Got a selection of good things on sale, stranger!")
    print("=================================================")
    print("\n1. Buy Weapons\n2. Inspect Weapons\n3. Inspect Vouchers\n4. Inspect Cash Balance\n5. Purchase history\n6. Leave")
    print("=================================================")

def buat_kembali():
    while True:
        try:
            leave = input("Press o button for back mate : ")
            if leave == "o":
                print("================")
                print(" Leaving Menu...")
                print("================")
                break
            else:
                print("======================")
                print(" Wrong input stranger!")
                print("======================")
        except EOFError:
            print("Type wisely stranger!")
        except KeyboardInterrupt:
            print("Type wisely stranger!")

def buat_convert_pesetas():
    while True:
        try:
            chart_buat_liat_cash(money)
            buat_input_nominal_e_money = int(input("Enter pesetas you want convert to e-money stranger! : "))
            if buat_input_nominal_e_money > money["pesetas"]:
                print("You dont have enough pesetas!")
                continue
            money["e-money"] += buat_input_nominal_e_money
            money["pesetas"] -= buat_input_nominal_e_money
            print(f" Pesetas Total : pts. {money["pesetas"]} ")
            print(f" E-Money Total :   e. {money["e-money"]} ")
            break
        except ValueError:
            print(" Wrong input!")

def buat_liat_cash():
    chart_buat_liat_cash(money)
    print("==========================================")
    print(f" Pesetas Total : pts. {money["pesetas"]} ")
    print(f" E-Money Total :   e. {money["e-money"]} ")
    print("==========================================")

def buat_liat_voucher():
    chart_buat_liat_voucher(voucher_card)
    print(" Limited Vouchers Avaiable for you stranger ")
    voucher_table = PrettyTable(["Code", "Voucher Card Name", "Discount", "Status"])
    voucher_code = 1
    voucher_table.clear_rows()
    for inventory in range(len(voucher_card["Voucher Card Name"])):
        voucher_table.add_row([voucher_code, 
                               voucher_card["Voucher Card Name"][inventory],
                               voucher_card["Discount"][inventory],
                               voucher_card["Status"]])
        voucher_code += 1
        print(voucher_table)

def update_purchase_history(player_type, item, price):
    purchase_history[player_type]["items"].append({"items": item, "price": price})
    purchase_history[player_type]["total_spent"] += price

def vip_weapons_buy():
    global input_weapons
    vip_player_weapons()
    while True:
        try:
            chart_buat_weapons_vip(weapons)
            input_weapons = input("Enter the name of the weapons you want to buy stranger : ")
            if input_weapons not in weapons["Weapons Name"]:
                raise ValueError("Weapon not found.")
            else:
                find_weapons = weapons["Weapons Name"].index(input_weapons)
                find_price_index = find_weapons
                price = weapons["Weapons Price First"][find_price_index]
                print(f" | Weapons Name you choose: {input_weapons} |")
                print(f" | Weapons Price you buy: {price} |")
                update_purchase_history("vip", input_weapons, price)
                break
        except ValueError:
            print("Mberr")

    while True:
        try:
            print("======================")
            print("====Payment method====")
            print("===Only use E-Money===")
            print("======================")
            player_choice = input(" Press x button to get discount! :")
            if player_choice == "x":
                vip_player_voucher()
                break
            else:
                print("===============================================")
                print(" Sorry mate, wrong selections pr is unavaiable ")
                print("===============================================")
        except EOFError:
            print("Type wisely Stranger!")
        except KeyboardInterrupt:
            print("Type Wisely Stranger!")

def non_vip_weapons_buy():
    global input_weapons
    non_vip_player_weapons()
    while True:
        try:
            chart_buat_weapons_non_vip(weapons)
            input_weapons = input("Enter the name of the weapons you want to buy stranger :")
            if input_weapons not in weapons["Weapons Name"]:
                raise ValueError("Weapon not found.")
            find_weapons = weapons.get("Weapons Name").index(input_weapons)
            find_price_weapons = weapons.get("Weapons Name").index(input_weapons)
            price = weapons.get("Weapons Price Two")[find_price_weapons]
            player_choice = weapons.get("Weapons Name")[find_weapons]
            print(f" | Weapons Name you choose: {player_choice} |")
            print(f" | Weapons Price you buy: {price} |")
            break
        except ValueError:
            print("mberr")

    while True:
        try:
            print("======================")
            print("====Payment method====")
            print("===Only use pesetas===")
            print("======================")
            player_choice = input(" Do you have voucher card stranger? (press x button for yes or press o button for no) : ")
            if player_choice == "x":
                non_vip_player_voucher()
                break
            elif player_choice == "o":
                non_vip_player_pay()
                break
            else:
                print("===============================================")
                print(" Sorry mate, wrong selections or is unavaiable ")
                print("===============================================")
        except EOFError:
            print("Type Wisely STranger!")
        except KeyboardInterrupt:
            print("Type wisely stranger!")

def non_vip_player_pay():
    try:
        price_index = weapons.get("Weapons Name").index(input_weapons)
        price = weapons.get("Weapons Price Two")[price_index]
        pesetas = money["pesetas"]
        print(" Payment method : Pesetas ")
        print(f" [ Weapons Price : pts. {price} ]")
        print(f" [ your pesetas before payment : pts. {money["pesetas"]} ] ")
        money["pesetas"] = pesetas - price
        if pesetas > price :
            print(f" [ your pesetas after payment : pts. {money["pesetas"]} ]")
            update_purchase_history("non_vip", input_weapons, price)
        else:
            pesetas < price
            print(" Not enough cash stranger! ")
            player_choice = input(" Find some treasure and kill zombies (press o button for continue journey)")
            if player_choice == "o":
                print("=====================")
                print(" *laughs* Thank you! ")
                print("=====================")
                raise SystemExit
            else:
                print("========================")
                print(" Wrong choice stranger! ")
                print("========================")
    except EOFError:
        print("Type wisely stranger!")
    except KeyboardInterrupt:
        print("Type wisely stranger!")

def print_purchase_history():
    print("==============================")
    print("       PURCHASE HISTORY       ")
    print("==============================")
    for player_type, history in purchase_history.items():
        print(f"{player_type.upper()} PLAYER:")
        print(f"Total Spent: {history["total_spent"]}")
        print("Item Purchased:")
        for item in history["items"]:
            print(f" {item["items"]}: {item["price"]}")
            print("=================================")

def vip_player_voucher():
    try:
        while True:
            price_index = weapons["Weapons Name"].index(input_weapons)
            price = weapons["Weapons Price First"][price_index]
            total = price * 0.7
            cash = money["e-money"] - total
            if cash >= 0:
                money["e-money"] = cash
                print(" | Payment method : E-Money   | ")
                print(f"| Weapons Price : e. {price} | ")
                print(f"| VIP Discount : 30%         | ")
                print(f"| Price after getting discounts : e. {total} | ")
                print(f"| Your E-Money is now worth : e. {money["e-money"]} | ")
                break
            elif cash < total:
                print("===========================================================")
                print("Not enough cash stranger! Convert your pesetas into E-money")
                print("===========================================================")
                player_choice = input("Do you want to convert? (press x button for yes or press o button for no) ")
                if player_choice == "x":
                    buat_convert_pesetas()
                    vip_weapons_buy()
                    break
                elif player_choice == "o":
                    print("===================================")
                    print("*laughs* Don't troll me stranger...")
                    print("===================================")
                    break
    except EOFError:
        print("Type Wisely Stranger!")
    except KeyboardInterrupt:
        print("Type Wisely Stranger!")

def non_vip_player_voucher():
    try:
        while True:
            chart_buat_liat_voucher(voucher_card)
            nama_voucher = input("Enter Voucher Card Name : ")
            if nama_voucher in voucher_card.get("Voucher Card Name"):
                cari_nama_voucher = voucher_card.get("Voucher Card Name").index(nama_voucher)
                cari_discount_voucher = voucher_card.get("Discount")[cari_nama_voucher]
                input_weapons = input("Enter Weapons Name Again : ")
                if input_weapons in weapons.get("Weapons Name"):
                    price_index = weapons.get("Weapons Name").index(input_weapons)
                    price = weapons.get("Weapons Price Two")[price_index]
                    pesetas = money["pesetas"]
                    total = price * (1 - cari_discount_voucher)
                    if pesetas > total:
                        money["pesetas"] = pesetas - total
                        print(f" Payment method: | Pesetas")
                        print(f" Weapons Price:  | pts. {price}")
                        print(f" Discount Price: | {cari_discount_voucher}")
                        print(f" Price after get discount: | pts. {total}")
                        print(f" Pesetas balance now:   | pts. {money["pesetas"]}")
                        break
                    else:
                        print("=========================")
                        print("Not enough cash stranger!")
                        print("=========================")
                        player_choice = input("Find some treasure and kill zombies! (press o button for continue journey)")
                        if player_choice == "o":
                            print("=================")
                            print("Comeback any time")
                            print("=================")
                            raise SystemExit
                        else:
                            print("=======================")
                            print(" Wrong choice stranger!")
                            print("=======================")
                else:
                    print("=================")
                    print("Weapons not found")
                    print("=================")
            else:
                print("======================")
                print("Voucher card not found")
                print("======================")
    except EOFError:
        print("Type Wisely Stranger!")
    except KeyboardInterrupt:
        print("Type Wisely Stranger!")

def vip_menu_player():
    while True:
        try:
            merchant_menu_vip()
            player_choice = (input(" Select your choice stranger! : "))
            if player_choice == "1":
                vip_weapons_buy()
                buat_kembali()
            elif player_choice == "2":
                vip_player_weapons()
                buat_kembali()
            elif player_choice == "3":
                buat_liat_cash()
                buat_kembali()
            elif player_choice == "4":
                buat_convert_pesetas()
                buat_kembali()
            elif player_choice == "5":
                print_purchase_history()
                chart_buat_liat_history_beli(purchase_history)
            elif player_choice == "6":
                print("===================")
                print(" Come back anytime ")
                print("===================")
                raise SystemExit
            else:
                print("====================================")
                print(" Wrong selections or is unavaiable! ")
                print("====================================")
        except EOFError:
            print("Type Wisely Stranger!")
        except KeyboardInterrupt:
            print("Type Wisely Stranger!")

def non_vip_menu_player():
    while True:
        try:
            merchant_menu_non_vip()
            player_choice = (input(" Select your choice stranger! : "))
            if player_choice == "1":
                non_vip_weapons_buy()
                buat_kembali()
            elif player_choice == "2":
                non_vip_player_weapons()
                buat_kembali()
            elif player_choice == "3":
                buat_liat_voucher()
                buat_kembali()
            elif player_choice == "4":
                buat_liat_cash()
                buat_kembali()
            elif player_choice == "5":
                print_purchase_history()
                chart_buat_liat_history_beli(purchase_history)
            elif player_choice == "6":
                print("===================")
                print(" Come back anytime ")
                print("===================")
                raise SystemExit
            else:
                print("===================================")
                print(" Wrong selections or is unavaible! ")
                print("===================================")
        except EOFError:
            print("Type Wisely Stranger!")
        except KeyboardInterrupt:
            print("Type Wisely Stranger!")

def register_vip_player():
    register_account = input(" Register account first : ")
    buat_input_nama = input(" input your name : ")
    print("========================================")
    print(" You have succesfully joined membership ")
    print(":::::::::::::Membership:::::::::::::")
    print(f"Email : {register_account}")
    print(f"Nama  : {buat_input_nama} ")
    print(":::::::::::::::::VIP:::::::::::::::::")
    print(" Congrats, you have joined vip member! ")
    print("=======================================")

def login_player():
    while True:
        try:
            print("==============================================")
            nama = input(" Enter Character Name : ")
            pin = input(" Enter pin number      : ")
            print("==============================================")
            if nama in player.get("name"):
                find_name = player.get("name").index(nama)
                if pin == player.get("pin")[find_name]:
                    print(" Successfully logged in!")
                    print("========================")
                    break
                else:
                    print("======================================================")
                    print("Login failed! Character name not found or wrong input.")
                    print("======================================================")
        except EOFError:
            print("Type Wisely Stranger!")
        except KeyboardInterrupt:
            print("Type Wisely Stranger!")

while True:
    login_player()
    while True:
        try:
            buat_input_vip_member = input (" Are you vip member ? (Press x button for yes or press o button for no)  ")
            if buat_input_vip_member == "x":
                vip_menu_player()
            elif buat_input_vip_member == "o":
                while True:
                    buat_join_vip_member = input(" do you want join vip member (Press x button for yes or press o button for no)")
                    if buat_join_vip_member == "x":
                        register_vip_player()
                        vip_menu_player()
                    elif buat_join_vip_member == "o":
                        non_vip_menu_player()
                    else:
                        print("==========================================")
                        print(" Wrong input stranger! type wisely mate...")
                        print("==========================================")
                    
                
            else:
                print("==========================================")
                print(" Wrong input stranger! type wisely mate...")
                print("==========================================")
        except EOFError:
            print("Type Wisely Stranger!")
        except KeyboardInterrupt:
            print("Type Wisely Stranger!")

